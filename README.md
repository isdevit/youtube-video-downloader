# YouTube Video Downloader


YouTube Video Downloader is a Python application that allows you to download and convert YouTube videos to audio files. You can save your favorite YouTube videos and listen to them offline.

## Features

- Download high-resolution videos from YouTube.
- Convert downloaded videos to audio (MP3) format.
- Play downloaded videos and audio files directly within the application.
- Supports downloading from any valid YouTube video URL.

## Table of Contents

- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Disclaimer](#disclaimer)
- [License](#license)
- [Author](#author)

## Getting Started

1. **Clone this repository** to your local machine:

   ```bash
   git clone https://github.com/isdevit/youtube-video-downloader
   ```

2. **Change the working directory** to the project folder:

    ```bash
    cd youtube-video-downloader
    ```

3. **Install the required Python packages** using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set your preferred download directory** by modifying the `SAVE_DIR` variable in `main.py`. Replace `"Yours Save Directory Folder's Path e.g C:/Users/...."` with your desired directory.

5. **Run the application**:

    ```bash
    python main.py
    ```

6. **Copy and paste a valid YouTube video URL** into the application and click the "Download" button to start downloading.

7. After the download is complete, you can **convert the video to audio** by clicking the "Convert to Audio" button.

8. You can **play the downloaded video or audio** by clicking the respective "Play" buttons.

## Dependencies

- [pytube](https://python-pytube.readthedocs.io/en/latest/) for downloading YouTube videos.
- [moviepy](https://zulko.github.io/moviepy/) for video-to-audio conversion.
- [vlc](https://pypi.org/project/python-vlc/) for video and audio playback.
- [tkinter](https://docs.python.org/3/library/tkinter.html) for the graphical user interface (GUI).

## Usage

Include any specific instructions on how to use your application effectively, additional settings or configurations, and any other important information about its usage.

## Troubleshooting

- If you encounter issues with the application, make sure you have all the required dependencies installed.
- Ensure that the provided directory in `SAVE_DIR` exists on your system and is writable.

## Disclaimer

This project is for educational and personal use only. Please respect YouTube's terms of service and copyright regulations when downloading and using videos.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Ashish Khetal
