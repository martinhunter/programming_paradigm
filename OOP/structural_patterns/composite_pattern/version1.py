from typing import List, Union

class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def display(self):
        print(f"File: {self.name} (Size: {self.size} KB)")

    def get_size(self) -> int:
        return self.size


class Folder:
    def __init__(self, name: str):
        self.name = name
        self.items: List[Union[File, 'Folder']] = []

    def add(self, item: Union[File, 'Folder']):
        self.items.append(item)

    def remove(self, item: Union[File, 'Folder']):
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
