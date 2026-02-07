from django.contrib.auth.models import Group, User
from djangospotifydownloader.quickstart.models import SpotifyLink
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from djangospotifydownloader import settings

from djangospotifydownloader.quickstart.serializers import GroupSerializer, UserSerializer, LinkSerializer



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
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
def upload_link(request):
    if request.method == 'POST':
        print("Request data: ", request.data)
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Serializer data: ", serializer.data)
            from spotdl import Spotdl
            
            # Initialize spotDL
            # spotdl = Spotdl()
            #print("Spotdl initialized: ", spotdl)
            from djangospotifydownloader.quickstart.utils import get_spotify_access_token
            access_token = get_spotify_access_token()
            if access_token:
                print(f"Got access token: {access_token[:20]}...")  # Print first 20 chars for security
            else:
                print("Failed to get access token")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # try:
        #     from spotdl import Spotdl
        #     spotdl = Spotdl()

        #     spotdl.download(request.data.get('link'), output_path=str(settings.MEDIA_ROOT / 'downloads'))
        #     return Response({'message': 'Link downloaded successfully'}, status=status.HTTP_200_OK)
        # except Exception as e:
        #     print(e)
        #     return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)