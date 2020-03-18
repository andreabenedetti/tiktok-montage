# Download videos from TikTok and create montages
## Requirements
- [tiktok-scraper](https://www.npmjs.com/package/tiktok-scraper): Scraper to download videos from Tik Tok with various settings (from user, hashtags, sounds...)
- [ffmpeg](https://www.ffmpeg.org/download.html): Library to manipulate videos through a CLI
- Python dependencies:
  - `pip install numpy`
  - `pip install Pillow`
  - `pip install os`
  - `pip install natsort`

## Protocol
Install tiktok-scraper through npm

```
npm install tiktok-scraper
```

Run tiktok-scraper with your settings, copy the links to the videos and download them (I use [DownThemAll](https://www.downthemall.net/) on Firefox)

Once you have your videos, open Terminal and go to the folder where they have been downloaded. Now, copy `extract-frames.sh` (inside the `src` folder, currently runs only on macOS, but based on [this bat script](https://superuser.com/questions/1346297/extracting-frames-from-all-videos-in-a-directory-using-ffmpeg)) to your video directory and run it:

```
cd /path/to/video/folder
/path/to/video/folder % sh extract-frames.sh
```

It will create a folder named as each video: it will extract one frame *every two seconds*.
