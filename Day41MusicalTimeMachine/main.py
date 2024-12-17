from bs4 import BeautifulSoup
from requests import *
import spotipy
from spotipy import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

user_preference = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = get(url = "https://www.billboard.com/charts/hot-100/" + user_preference, headers = header)

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
# print(song_names_spans)
song_names = [song.getText().strip() for song in song_names_spans]

#Spotify
CLIENT_ID = "bbfda6b573674fd4afb792ddd09feb9c"
CLIENT_SECRET = "5515e8a866814225905efebab6b3fd70"

sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        redirect_uri = "http://example.com",
        scope = "playlist-modify-private",
        cache_path = "token_save.txt",
        show_dialog = True,
        username = "Sayed Mubaris Hashimi"
    )
 )
user_id = sp.current_user()["id"]
print(user_id)
song_uris = []
year = user_preference.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user = user_id, name = f"{user_preference} Billboard 100", public = False)
print(playlist)

sp.playlist_add_items(playlist_id = playlist["id"], items = song_uris)
