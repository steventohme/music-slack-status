import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-read-playback-state"))


def get_currently_playing():
    result = sp.current_user_playing_track()
    song_name = result['item']['name']
    artist_name = result['item']['artists'][0]['name']
    progress_ms = result['progress_ms']
    duration_ms = result['item']['duration_ms']
    return song_name, artist_name, progress_ms, duration_ms

def format_time(ms: int):
    """Convert milliseconds to MM:SS format"""
    total_seconds = int(ms / 1000)
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"

