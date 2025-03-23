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
    c1 = Character('A', "Arial", "Red", 12)
    c2 = Character('B', "Arial", "Red", 12)
    c3 = Character('C', "Times New Roman", "Blue", 14)

    c1.display()
    c2.display()
    c3.display()
