# 🎵 Music Slack Status 🎵

Welcome to **music-slack-status**! This groovy project syncs your current Spotify jam with your Slack status, so your colleagues always know what tunes you're vibing to. 🎧

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.11+
- [Poetry](https://python-poetry.org/) for dependency management

### Installation

1. **Clone the repo:**
    ```sh
    git clone https://github.com/yourusername/music-slack-status.git
    cd music-slack-status
    ```

2. **Install dependencies:**

    ```sh
    poetry install
    ```

3. **Set up your environment variables:**

    Copy the `.env.example` to `.env` and fill in your credentials:

    ```sh
    cp .env.example .env
    ```

    Edit the [.env](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fsteventohme%2FDesktop%2Fmusic-slack-status%2F.env%22%2C%22path%22%3A%22%2FUsers%2Fsteventohme%2FDesktop%2Fmusic-slack-status%2F.env%22%2C%22scheme%22%3A%22file%22%7D%7D) file with your favorite editor and add your Slack and Spotify credentials:

    ```env
    SLACK_USER_TOKEN=xoxp-your-slack-token
    SLACK_USER_ID=your-slack-user-id
    SPOTIPY_CLIENT_ID=your-spotify-client-id
    SPOTIPY_CLIENT_SECRET=your-spotify-client-secret
    SPOTIPY_REDIRECT_URI=https://localhost:8888/callback
    ```

### Running the Project

1. **Fire up the script:**

    ```sh
    poetry run python main.py
    ```

    Or, if you prefer to specify the Slack user ID directly:

    ```sh
    poetry run python main.py your-slack-user-id
    ```

2. **Authenticate with Spotify**

3. **Watch the magic happen!!**

## 🌟 Contributing
Feel free to fork this project and submit pull requests. Let's make this project even more awesome together! 🤘

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
