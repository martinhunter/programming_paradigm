# 字符类
class Character:
    def __init__(self, ch, font, color, size):
        self.ch = ch
        self.font = font
        self.color = color
        self.size = size

    def display(self):
        print(f"Character: {self.ch}, Font: {self.font}, Color: {self.color}, Size: {self.size}")

# 客户端代码
if __name__ == "__main__":
    characters = []

    for _ in range(1000):
        characters.append(Character('A', "Arial", "Red", 12))
        characters.append(Character('B', "Arial", "Red", 12))
        characters.append(Character('C', "Times New Roman", "Blue", 14))

    for c in characters:
        c.display()
