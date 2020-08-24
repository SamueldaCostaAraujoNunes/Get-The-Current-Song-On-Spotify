import spotipy.util as util
import spotipy
import time 
import Credentials

scope = "user-read-currently-playing"
Credentials.SetCreditentials()

token = util.prompt_for_user_token(username='', scope=scope)
track = spotipy.Spotify(token).current_user_playing_track()#JSON to Dict

nameTrack = track['item']['name'] 
artistsTrack = track['item']['artists'][0]['name']
albumTrack = track['item']['album']['name']
progressTrack = track['progress_ms']/1000
durationTrack = track['item']['duration_ms']/1000
statusTrack = track['is_playing']

print(f"Nome: {nameTrack}")
print(f"Artista: {artistsTrack}")
print(f"Album: {albumTrack}")
print(f"Porcentagem já ouvida: {int((progressTrack/durationTrack)*100)}%")