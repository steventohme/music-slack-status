from slack_sdk import WebClient

def set_status(client: WebClient, status_text: str, status_emoji: str):
    try:
        client.users_profile_set(
            profile={
                "status_text": status_text,
                "status_emoji": status_emoji,
            }
        )
    except: 
        print(f"Failed to set status")