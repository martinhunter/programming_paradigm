class BasePlayer:
    def play(self, file_name, file_size):
        pass


class Mp3Player(BasePlayer):
    def play(self, file_name, user):
        print(f"Playing MP3 file: {file_name} {user}")


class PlayerClient:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_player(self):
        if self.file_name.endswith() == "mp3":
            player = Mp3Player()
        else:
            raise Exception()
        return player

    def start_play(self, user):
        player = self.get_player()
        player.play(self.file_name, user)


client = PlayerClient('/home/abc.mp3')
client.start_play("Bob")
