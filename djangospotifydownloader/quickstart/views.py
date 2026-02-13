"""
Views for the djangospotifydownloader project.
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import HttpResponse, JsonResponse
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view

from djangospotifydownloader.quickstart.models import SpotifyLink
from djangospotifydownloader.quickstart.serializers import GroupSerializer, LinkSerializer, UserSerializer
from djangospotifydownloader.quickstart.utils import get_spotdl_instance, get_spotify_access_token


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = get_user_model().objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class LinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows links to be viewed or edited.
    """

    queryset = SpotifyLink.objects.all().order_by("created_at")
    serializer_class = LinkSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['POST'])
def spotify_callback(request):
    """
    Callback for the Spotify API.
    """
    if request.method == 'POST':
        print("Request data: ", request.data)
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            link = serializer.data.get('link')
            if not link:
                return HttpResponse("Link is required", status=status.HTTP_400_BAD_REQUEST)

            print("Serializer data: ", serializer.data)

            # Initialize spotDL
            # spotdl = Spotdl()
            #print("Spotdl initialized: ", spotdl)
            access_token = get_spotify_access_token()
            return fetch_spotify_link(link, access_token)

    #In case there is not a POST request, we return an error
    return JsonResponse({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)



def fetch_spotify_link(link:str, access_token):
    """
    Fetch a Spotify link and return the songs.
    """

    if not access_token:
        return JsonResponse({'error': 'Failed to get access token'}, status=status.HTTP_400_BAD_REQUEST)
    spotdl = get_spotdl_instance()

    songs = spotdl.search([link])

    # song, path = spotdl.download(songs[0])
    # print(song, path)
    if songs:
        songs_json = [song.json for song in songs]
        spotify_link = SpotifyLink.objects.create(link=link, songs=songs_json)
        return JsonResponse({'song': songs_json, 'link': link, 'spotify_link': spotify_link.id	}, status=status.HTTP_200_OK)
    return JsonResponse({'error': 'Failed to fetch songs'}, status=status.HTTP_400_BAD_REQUEST)
