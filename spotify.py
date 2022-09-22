import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID=''
SPOTIPY_CLIENT_SECRET=''

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET
))

results = sp.search(q='cpm22', limit=1)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name']+" "+track['uri'])