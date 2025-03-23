# 字符享元类
class CharacterFlyweight:
    _pool = {}

    def __new__(cls, font, color, size):
        key = (font, color, size)
        if key not in cls._pool:
            instance = super(CharacterFlyweight, cls).__new__(cls)
            instance.font = font
            instance.color = color
            instance.size = size
            cls._pool[key] = instance
        return cls._pool[key]

    def display(self, ch):
        print(f"Character: {ch}, Font: {self.font}, Color: {self.color}, Size: {self.size}")

# 客户端代码
if __name__ == "__main__":
    characters = []

    for _ in range(1000):
        characters.append(CharacterFlyweight("Arial", "Red", 12))
        characters.append(CharacterFlyweight("Arial", "Red", 12))
        characters.append(CharacterFlyweight("Times New Roman", "Blue", 14))

    for c in characters:
        c.display('A')
