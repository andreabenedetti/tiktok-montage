# Download videos from TikTok and create montages
## Requirements
- [tiktok-scraper](https://www.npmjs.com/package/tiktok-scraper): Scraper to download videos from Tik Tok with various settings (from user, hashtags, sounds...)
- [ffmpeg](https://www.ffmpeg.org/download.html): Library to manipulate videos through a CLI
- Python dependencies:
  - `pip install numpy`
  - `pip install Pillow`
  - `pip install os`
  - `pip install natsort`

## Instructions
Install tiktok-scraper through npm

```
npm install tiktok-scraper
```

### Data gathering
Run tiktok-scraper with your settings, copy the links to the videos and download them (I use [DownThemAll](https://www.downthemall.net/) on Firefox)

### Extracting frames

Once you have your videos, open Terminal and go to the folder where they have been downloaded. Now, copy `extract-frames.sh` (inside the `src` folder; it currently runs only on macOS, but it's based on [this bat script](https://superuser.com/questions/1346297/extracting-frames-from-all-videos-in-a-directory-using-ffmpeg)) to your video directory and run it:

```
cd /path/to/video/folder
/path/to/video/folder % sh extract-frames.sh
```

It will create a folder named as each video: it will extract one frame *every two seconds*.

### Montage
Copy `stitch.py` to the folder of the video you want to create the *frametage* (frame montage) for.

```
cd /path/to/frame/folder
/path/to/frame/folder % python stitch.py
```
The script will generate a horizontal stitching of all the images inside the folder. It will be called as the folder and it will placed in its parent directory.

## Example result
![Example](images/example.png)
*Video frametage from the hashtag "coronavirus"*
