from slack.slack import SlackClient
from spotify.spotify import SpotifyClient
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: poetry run python main.py <user-id>")
        sys.exit(1)


    spotify = SpotifyClient()

    status_text = spotify.get_song_status()
    status_emoji = ":notes:"
    status_expiration = 0

    user_id = sys.argv[1]
    slack = SlackClient()
    slack.set_status(user_id, status_text, status_emoji, status_expiration)

if __name__ == "__main__":
    main()