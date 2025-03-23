from abc import ABC, abstractmethod

# 迭代器接口
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# 具体迭代器：正序迭代器
class ForwardIterator(Iterator):
    def __init__(self, playlist):
        self.playlist = playlist
        self.index = 0

    def has_next(self):
        return self.index < len(self.playlist.songs)

    def next(self):
        if self.has_next():
            song = self.playlist.songs[self.index]
            self.index += 1
            return song
        else:
            raise StopIteration

# 具体迭代器：倒序迭代器
class ReverseIterator(Iterator):
    def __init__(self, playlist):
        self.playlist = playlist
        self.index = len(self.playlist.songs) - 1

    def has_next(self):
        return self.index >= 0

    def next(self):
        if self.has_next():
            song = self.playlist.songs[self.index]
            self.index -= 1
            return song
        else:
            raise StopIteration

# 播放列表类
class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def create_iterator(self, reverse=False):
        if reverse:
            return ReverseIterator(self)
        else:
            return ForwardIterator(self)

# 客户端代码
if __name__ == "__main__":
    playlist = Playlist()
    playlist.add_song("Song 1")
    playlist.add_song("Song 2")
    playlist.add_song("Song 3")

    forward_iterator = playlist.create_iterator()
    while forward_iterator.has_next():
        print(f"Playing: {forward_iterator.next()}")

    print("\nPlaying in reverse order:")
    reverse_iterator = playlist.create_iterator(reverse=True)
    while reverse_iterator.has_next():
        print(f"Playing: {reverse_iterator.next()}")
