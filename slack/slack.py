from slack_sdk import WebClient
from dotenv import load_dotenv
import os

load_dotenv()

class SlackClient:
    def __init__(self):
        token = os.getenv('SLACK_USER_TOKEN')

        client = WebClient(token=token)

        self.client = client

    def set_status(self, user_id:str,  status_text: str, status_emoji: str, status_expiration: int):
        try:
            self.client.users_profile_set(
                user=user_id,
                profile={
                    "status_text": status_text,
                    "status_emoji": status_emoji,
                }
            )
        except: 
            print(f"Failed to set status")
