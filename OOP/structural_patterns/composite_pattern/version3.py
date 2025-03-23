from abc import ABC, abstractmethod
from typing import List, Union


class FileSystemComponent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass


class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    def display(self):
        print(f"File: {self.name} (Size: {self.size} KB)")

    def get_size(self) -> int:
        return self.size


class Folder(FileSystemComponent):
    def __init__(self, name: str):
        super().__init__(name)
        self.items: List[FileSystemComponent] = []

    def add(self, item: FileSystemComponent):
        self.items.append(item)

    def remove(self, item: FileSystemComponent):
        self.items.remove(item)

    def display(self):
        print(f"Folder: {self.name}")
        for item in self.items:
            item.display()

    def get_size(self) -> int:
        total_size = 0
        for item in self.items:
            total_size += item.get_size()
        return total_size
