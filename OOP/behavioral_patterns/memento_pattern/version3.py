class Memento:
    def __init__(self, text):
        self.text = text

class TextEditor:
    def __init__(self):
        self.text = ""

    def edit(self, new_text):
        self.text = new_text
        print(f"Edited text: {self.text}")

    def create_memento(self):
        return Memento(self.text)

    def restore_from_memento(self, memento):
        self.text = memento.text
        print(f"Restored text: {self.text}")

class Caretaker:
    def __init__(self, editor):
        self.editor = editor
        self.mementos = []

    def backup(self):
        self.mementos.append(self.editor.create_memento())

    def undo(self):
        if self.mementos:
            memento = self.mementos.pop()
            self.editor.restore_from_memento(memento)
        else:
            print("No more actions to undo")

    def redo(self):
        if self.mementos:
            memento = self.mementos[-1]
            self.editor.restore_from_memento(memento)
        else:
            print("No more actions to redo")

# 客户端代码
if __name__ == "__main__":
    editor = TextEditor()
    caretaker = Caretaker(editor)

    editor.edit("Hello")
    caretaker.backup()
    editor.edit("Hello World")
    caretaker.backup()

    caretaker.undo()
    caretaker.redo()
