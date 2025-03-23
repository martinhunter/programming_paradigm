class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def insert_text(self, text):
        self.history.append((self.text, "insert"))
        self.text += text
        print(f"Inserted text: {text}")
        print(f"Current text: {self.text}")

    def delete_text(self, length):
        self.history.append((self.text, "delete"))
        self.text = self.text[:-length]
        print(f"Deleted {length} characters")
        print(f"Current text: {self.text}")

    def undo(self):
        if self.history:
            last_text, action = self.history.pop()
            if action == "insert":
                self.text = last_text
                print(f"Undo insert: {self.text}")
            elif action == "delete":
                self.text = last_text
                print(f"Undo delete: {self.text}")
        else:
            print("No more actions to undo")

    def redo(self):
        if self.history:
            last_text, action = self.history.pop()
            if action == "insert":
                self.text = last_text
                self.insert_text(last_text[len(self.text):])
            elif action == "delete":
                self.text = last_text
                self.delete_text(len(last_text) - len(self.text))
        else:
            print("No more actions to redo")

# 客户端代码
if __name__ == "__main__":
    editor = TextEditor()
    editor.insert_text("Hello")
    editor.insert_text(" World")
    editor.delete_text(5)
    editor.undo()
    editor.redo()
    editor.undo()
    editor.undo()
