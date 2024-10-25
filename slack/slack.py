from slack_sdk import WebClient
from dotenv import load_dotenv
import sys
import os

load_dotenv()

def set_status(client: WebClient, user_id:str,  status_text: str, status_emoji: str, status_expiration: int):
    try:
        client.users_profile_set(
            user=user_id,
            profile={
                "status_text": status_text,
                "status_emoji": status_emoji,
            }
        )
    except: 
        print(f"Failed to set status")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <user-id> '<song-name>'")
        sys.exit(1)

    token = os.getenv('SLACK_USER_TOKEN')

    client = WebClient(token=token)

    status_text = f"Listening to: {sys.argv[2]}"
    status_emoji = ":notes:"
    status_expiration = 0

    user_id = sys.argv[1]
    set_status(client, user_id, status_text, status_emoji, status_expiration)

if __name__ == "__main__":
    main()