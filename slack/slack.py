from slack_sdk import WebClient


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