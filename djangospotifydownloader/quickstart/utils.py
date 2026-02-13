"""
Utils for the djangospotifydownloader project. This file contains the functions that are used to get the access token from Spotify API and the Spotdl instance.
"""

import base64
import os

import environ
import requests
from django.conf import settings
from spotdl import Spotdl


# So, according to spotify dev forum, this will have to be done after wednesday, 11th of February 2026 :(
def get_spotify_access_token():
    """
    Get an access token from Spotify API using client credentials flow.
    Returns the access token or None if request fails.
    """

    # Get credentials from environment variables
    client_id ,client_secret = get_spotify_client_id_and_secret()

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
        json=True,
        timeout=1000,
    )
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get('access_token')
        print(f"Successfully obtained access token (expires in {token_data.get('expires_in')} seconds)")
        return access_token
    return None

def get_spotify_client_id_and_secret():
    """
    Get the Spotify client ID and secret from the environment variables.
    Returns a list with the client ID and secret.
    """
    env = environ.Env()
    environ.Env.read_env(os.path.join(settings.BASE_DIR, '.env'))
    return [env('SPOTIFY_CLIENT_ID'),
            env('SPOTIFY_CLIENT_SECRET')]

# Global Spotdl instance
_spotdl_instance = None

def get_spotdl_instance():
    """
    Get or initialize the global Spotdl instance.
    Returns the same instance if already initialized.
    """
    global _spotdl_instance # pylint: disable=global-statement
    if _spotdl_instance is None:
        client_id, client_secret = get_spotify_client_id_and_secret()
        _spotdl_instance = Spotdl(
            client_id=client_id,
            client_secret=client_secret,
            user_auth=False,
            no_cache=None
        )

    return _spotdl_instance
