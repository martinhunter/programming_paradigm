class TextEditor:
    def __init__(self):
        self.text = ""

    def edit(self, new_text):
        self.text = new_text
        print(f"Edited text: {self.text}")

# 客户端代码
if __name__ == "__main__":
    editor = TextEditor()
    editor.edit("Hello")
    editor.edit("Hello World")
