# VLC Rich Presence

[![Discord](https://img.shields.io/badge/Discord-Rich%20Presence-blue)](https://discord.com/developers/docs/rich-presence)

This project updates your Discord status with the media you're currently watching on **VLC Media Player**. It uses Discord's Rich Presence feature to display the media name and status.

---

## Features

- Automatically detects when VLC is running.
- Updates your Discord status with the currently playing media.
- Supports popular media formats (`.mkv`, `.mp4`, `.avi`, `.mov`, `.mp3`, `.flac`, `.wav`).
- Easy to set up and use.

---

## Installation

### Prerequisites

- Python 3.7 or higher.
- VLC Media Player installed on your system.
- A Discord application with Rich Presence enabled (to get your `CLIENT_ID`).

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/vlc-rich-presence.git
   cd vlc-rich-presence
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your `.env` file:**
   - Copy the example `.env` file:
     ```bash
     cp config/.env.example config/.env
     ```
   - Open `config/.env` and add your Discord application's `CLIENT_ID`:
     ```
     CLIENT_ID=your_discord_client_id_here
     ```

4. **Run the application:**
   ```bash
   python main.py
   ```

---

## Usage

1. Start VLC Media Player and open a media file.
2. Run the application using `python main.py`.
3. Your Discord status will automatically update to show the media you're watching.

To stop the application, press `Ctrl+C`.

---

## Configuration

### Environment Variables

- `CLIENT_ID`: Your Discord application's client ID. You can create one at the [Discord Developer Portal](https://discord.com/developers/applications).

### Supported Media Formats

The application supports the following media formats:
- Video: `.mkv`, `.mp4`, `.avi`, `.mov`
- Audio: `.mp3`, `.flac`, `.wav`

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.


---

## Acknowledgments

- [pypresence](https://github.com/qwertyquerty/pypresence) for the Discord Rich Presence library.
- [psutil](https://github.com/giampaolo/psutil) for process monitoring.
- [python-dotenv](https://github.com/theskumar/python-dotenv) for environment variable management.

