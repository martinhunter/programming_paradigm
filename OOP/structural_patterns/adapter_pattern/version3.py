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


# 适配器类（Adapter），将不同的播放接口统一为统一接口
class Mp4PlayerAdapter:
    def __init__(self):
        self.adaptee = ThirdPartyMp4Player(time.time())

    @staticmethod
    def convert_file(file_name):
        return 'xx-{}-xx'.format(file_name)

    def play(self, file_name, user):
        new_file_name = self.convert_file(file_name)
        extra = 'EX'
        self.adaptee.play_mp4(new_file_name, extra, user)


class PlayerClient:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_player(self):
        if self.file_name.endswith() == "mp3":
            player = Mp3Player()
        elif self.file_name.endswith() == "mp4":
            player = Mp4PlayerAdapter()
        else:
            raise Exception()
        return player

    def start_play(self, user):
        player = self.get_player()
        player.play(self.file_name, user)


client = PlayerClient('/home/abc.mp3')
client.start_play("Bob")
