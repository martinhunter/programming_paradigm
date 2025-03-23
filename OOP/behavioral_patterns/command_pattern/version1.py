class TextEditor:
    def __init__(self):
        self.text = ""

    def insert_text(self, text):
        self.text += text
        print(f"Inserted text: {text}")
        print(f"Current text: {self.text}")

    def delete_text(self, length):
        self.text = self.text[:-length]
        print(f"Deleted {length} characters")
        print(f"Current text: {self.text}")

# 客户端代码
if __name__ == "__main__":
    editor = TextEditor()
    editor.insert_text("Hello")
    editor.insert_text(" World")
    editor.delete_text(5)
