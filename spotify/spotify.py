import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()


class SpotifyClient:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-read-playback-state"))

    def get_currently_playing(self):
        result = self.sp.current_user_playing_track()
        song_name = result['item']['name']
        artist_name = result['item']['artists'][0]['name']
        progress_ms = result['progress_ms']
        duration_ms = result['item']['duration_ms']
        return song_name, artist_name, progress_ms, duration_ms

    def create_song_progress_bar(self, progress_ms: int, duration_ms: int, width=10):
        """
        Create a text-based progress bar for song progress.
        
        Args:
            progress_ms (int): Current progress in milliseconds
            duration_ms (int): Total duration in milliseconds
            width (int): Width of the progress bar in characters
            
        Returns:
            tuple: (progress_bar, timestamp)
        """
        # Calculate progress percentage
        progress = min(progress_ms / duration_ms, 1.0)
        filled_length = int(width * progress)
        
        # Create the progress bar
        bar = "▓" * filled_length + "░" * (width - filled_length)
        
        # Format timestamps
        current_time = self.format_time(progress_ms)
        total_time = self.format_time(duration_ms)
        
        return f"[{bar}] {current_time}/{total_time}"

    def format_time(self, ms: int):
        """Convert milliseconds to MM:SS format"""
        total_seconds = int(ms / 1000)
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def get_song_status(self):
        song_name, artist_name, progress_ms, duration_ms = self.get_currently_playing()
        progress_bar = self.create_song_progress_bar(progress_ms, duration_ms)
        return f"{song_name} - {artist_name}\n{progress_bar}"