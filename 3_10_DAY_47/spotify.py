import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_config import ClientID,Clientsecret,USERNAME
from bs4 import BeautifulSoup
import requests

song_titles=[]

date=input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_songs = soup.findAll(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only", id="title-of-a-story")
print(f'ALL SONG: {all_songs}')

try:
    number_one = soup.find(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet", id="title-of-a-story").getText()
    print(number_one)
    number_one = number_one.replace("\n", "")
    song_titles = [song.getText().replace("\n", "") for song in all_songs]
    song_titles.insert(0, number_one)

except AttributeError as e:
    print("error")
    print(e)


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

song_uris = []
year = date.split("-")[0]

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
try:
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
except spotipy.exceptions.SpotifyException as e:
    print(e)
