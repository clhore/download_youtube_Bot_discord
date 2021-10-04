# encoding: utf-8

# library
import youtube_dl
import json


# create class
class YTdowload:
    def __init__(self, url: str or list, conf: dict, file=str()):
        # declare variable
        self.video_url = url
        self.conf = conf
        self.video_info = {"title": "error extract info"}
        if file != "":  # check variable file
            self.rute = file
        else:
            self.rute = file

    def lista(self, mode='audio'):
        ruteList = list()
        if mode == 'audio':
            for url in self.video_url:
                self.video_url = url
                rute = self.audio()
                ruteList.append(rute)
        if mode == 'video':
            try:
                resolution = self.conf["resolution"]
            except:
                resolution = "mp4_640_360"
            for url in self.video_url:
                self.video_url = url
                rute = self.video(resolution)
                ruteList.append(rute)
        return ruteList

    def audio(self):
        try:
            video_info = self.extract_info()
            filename = f'{video_info["title"]}.mp3'
            filename = self.text_replace(filename)
            filename = f'{self.rute}{filename}'
            options = {
                'format': 'bestaudio/best',
                'keepvideo': False,
                'outtmpl': filename,
            }
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([video_info['webpage_url']])
            return filename
        except youtube_dl.utils.DownloadError:
            print(f'download error: {self.video_url} | audio')

    def video(self, resolution: str):
        try:
            video_info = self.extract_info()
            resolution = self.extract_resolution(resolution)
            filename = f'{video_info["title"]}-{resolution["name"]}.mp4'
            filename = self.text_replace(filename)
            filename = f'{self.rute}{filename}'
            options = {
                "format": resolution["id"],
                "outtmpl": filename,
                # ignoreerrors=True
                # quiet=True
            }

            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([self.video_url])
            print(filename)
            return filename
        except youtube_dl.utils.DownloadError:
            print(f'download error: {self.video_url} | {resolution}')

    def extract_info(self):
        try:
            video_info = youtube_dl.YoutubeDL().extract_info(
                url=self.video_url, download=False
            )
            return video_info
        except youtube_dl.utils.DownloadError:
            print(f'extract info error: {self.video_url}')

    @staticmethod
    def text_replace(text: str):
        text = text.replace("'", '').replace('"', '') \
            .replace('#', '').replace(',', '') \
            .replace('|', '').replace('/', '')
        text.encode('utf-8')
        return text

    @staticmethod
    def extract_resolution(resolution: str):
        try:
            list_resolution = {
                "mp4_144p": '160',
                "mp4_240p": '133',
                "mp4_360p": '134',
                "mp4_480p": '135',
                "mp4_720p": '136',
                "mp4_1080p": '137',
                "gp3_176_144": '17',  # 3gp: 176*144
                "gp3_320_240": '36',
                "flv": '5',
                "webm": '43',
                "mp4_640_360": '18'  # 640 * 360
            }
            resolution = {
                "id": list_resolution[f'{resolution}'],
                "name": resolution
            }
            return resolution
        except Exception as e:
            print('Error resolution selected')
            print(e)
            # default resolution
            resolution = {"id": 18, "name": "640"}
            return resolution