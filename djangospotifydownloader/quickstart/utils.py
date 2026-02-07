import requests
import base64
import os
from django.conf import settings
import environ
import os


# So, according to spotify dev forum, this will have to be done after wednesday, 11th of February 2026 :(
def get_spotify_access_token():
    """
    Get an access token from Spotify API using client credentials flow.
    Returns the access token or None if request fails.
    """

    env = environ.Env()
    environ.Env.read_env(os.path.join(settings.BASE_DIR, '.env'))

    # Get credentials from environment variables
    client_id = env('SPOTIFY_CLIENT_ID')
    client_secret = env('SPOTIFY_CLIENT_SECRET')

    # Encode credentials for Basic Auth
    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    
    # Make POST request to Spotify token endpoint
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            'grant_type': 'client_credentials',
        },
    )
    
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get('access_token')
        print(f"Successfully obtained access token (expires in {token_data.get('expires_in')} seconds)")
        return access_token
    else:
        print(f"Error getting token: {response.status_code} - {response.text}")
        return None