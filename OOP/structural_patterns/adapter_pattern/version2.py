import time


class BasePlayer:
    def play(self, file_name, file_size):
        pass


class Mp3Player(BasePlayer):
    def play(self, file_name, user):
        print(f"Playing MP3 file: {file_name} {user}")


class ThirdPartyMp4Player:
    # 第三方库不可更改代码
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def play_mp4(self, file_name, extra, user):
        print(f"Playing MP4 file: {file_name} {user} Time: {self.timestamp}, Extra: {extra}")


class PlayerClient:
    def __init__(self, file_name):
        self.file_name = file_name

    def start_play(self, user):
        if self.file_name.endswith() == "mp3":
            player = Mp3Player()
            player.play(self.file_name, user)
        elif self.file_name.endswith() == "mp4":
            player = ThirdPartyMp4Player(time.time())
            player.play_mp4(self.file_name, 'EX', user)
        else:
            raise Exception()


client = PlayerClient('/home/abc.mp3')
client.start_play("Bob")
