import requests #type: ignore
from bs4 import BeautifulSoup #type:ignore
from dotenv import load_dotenv # type: ignore
import os
import spotipy  # type: ignore
from spotipy.oauth2 import SpotifyOAuth  # type: ignore
from datetime import datetime


load_dotenv() 
CLIENT_ID = os.getenv("CLIENT_ID") 
CLIENT_SECRET = os.getenv("CLIENT_SECRET") 

response = requests.get("https://www.billboard.com/charts/hot-100/")

response.raise_for_status()
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage,"html.parser")
song_names_spans = soup.select("li ul li h3")


song_names = [song.getText().strip() for song in song_names_spans]


#Spotify Authorization:
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://open.spotify.com/",
        client_id= CLIENT_ID,
        client_secret= CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = datetime.now().strftime("%Y-%m-%d")

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)







