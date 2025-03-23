class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def edit(self, new_text):
        self.history.append(self.text)
        self.text = new_text
        print(f"Edited text: {self.text}")

    def undo(self):
        if self.history:
            self.text = self.history.pop()
            print(f"Undo: {self.text}")
        else:
            print("No more actions to undo")

    def redo(self):
        if self.history:
            last_text = self.history.pop()
            self.text = last_text
            print(f"Redo: {self.text}")
        else:
            print("No more actions to redo")

# 客户端代码
if __name__ == "__main__":
    editor = TextEditor()
    editor.edit("Hello")
    editor.edit("Hello World")
    editor.undo()
    editor.redo()
