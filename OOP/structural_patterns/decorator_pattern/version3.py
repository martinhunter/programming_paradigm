from abc import ABC, abstractmethod


class FileProcessor(ABC):
    @abstractmethod
    def process(self, file_path: str):
        pass


class FileReader(FileProcessor):
    def process(self, file_path: str):
        with open(file_path, 'r') as file:
            return file.readlines()


class FileProcessorDecorator(FileProcessor):
    def __init__(self, wrapped: FileProcessor):
        self.wrapped = wrapped

    def process(self, file_path: str):
        return self.wrapped.process(file_path)


class LineCountDecorator(FileProcessorDecorator):
    def process(self, file_path: str):
        lines = self.wrapped.process(file_path)
        line_count = len(lines)
        return lines, line_count


class WordCountDecorator(FileProcessorDecorator):
    def process(self, file_path: str):
        lines, line_count = self.wrapped.process(file_path)
        word_count = sum(len(line.split()) for line in lines)
        return lines, line_count, word_count


if __name__ == '__main__':
    file_path = 'example.txt'
    processor = FileReader()
    processor = LineCountDecorator(processor)
    processor = WordCountDecorator(processor)

    lines, *counts = processor.process(file_path)
    for line in lines:
        print(line, end='')

    if counts:
        print(f'\nTotal lines: {counts[0]}')
    if len(counts) > 1:
        print(f'Total words: {counts[1]}')
