import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_config import ClientID,Clientsecret,USERNAME

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=ClientID,
        client_secret=Clientsecret,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME,
    )
)
user_id = sp.current_user()["id"]