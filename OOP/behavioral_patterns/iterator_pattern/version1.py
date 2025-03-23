class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def play(self):
        for song in self.songs:
            print(f"Playing: {song}")

# 客户端代码
if __name__ == "__main__":
    playlist = Playlist()
    playlist.add_song("Song 1")
    playlist.add_song("Song 2")
    playlist.add_song("Song 3")

    playlist.play()
