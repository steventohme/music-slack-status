from slack.slack import SlackClient
from spotify.spotify import SpotifyClient
import sys
import os
import time
from dotenv import load_dotenv

load_dotenv()

def main():
    if len(sys.argv) < 2 and os.getenv('SLACK_USER_ID') is None:
        print('Please provide a user id')
        sys.exit(1)
    elif len(sys.argv) < 2:
        user_id = os.getenv('SLACK_USER_ID')
    else:
        user_id = sys.argv[1]
    
    spotify = SpotifyClient()
    slack = SlackClient()
    status_emoji = ":notes:"
    status_expiration = 0


    while True:
        try:
            succeeded, status_text = spotify.get_song_status()
            if succeeded:
                slack.set_status(user_id, status_text, status_emoji, status_expiration)
        except Exception as e:
            print(f"Failed to set status: {e}")

        time.sleep(3)

if __name__ == "__main__":
    main()