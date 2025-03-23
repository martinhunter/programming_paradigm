from abc import ABC, abstractmethod


# 命令接口
class Command(ABC):
    def __init__(self, editor):
        self.editor = editor

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def redo(self):
        pass


# 具体命令：插入文本
class InsertTextCommand(Command):
    def __init__(self, editor, text, position):
        super().__init__(editor)
        self.text = text
        self.position = position
        self.previous_text = ""

    def execute(self):
        self.previous_text = self.editor.text[self.position:self.position + len(self.text)]
        self.editor.text = self.editor.text[:self.position] + self.text + self.editor.text[self.position:]
        print(f"Inserted text: '{self.text}' at position {self.position}")
        print(f"Current text: '{self.editor.text}'")

    def undo(self):
        self.editor.text = self.editor.text[:self.position] + self.previous_text + self.editor.text[
                                                                                   self.position + len(self.text):]
        print(f"Undo insert: '{self.text}' at position {self.position}")
        print(f"Current text: '{self.editor.text}'")

    def redo(self):
        self.execute()
        print(f"Redo insert: '{self.text}' at position {self.position}")
        print(f"Current text: '{self.editor.text}'")


# 具体命令：删除文本
class DeleteTextCommand(Command):
    def __init__(self, editor, length, position):
        super().__init__(editor)
        self.length = length
        self.position = position
        self.deleted_text = ""

    def execute(self):
        self.deleted_text = self.editor.text[self.position:self.position + self.length]
        self.editor.text = self.editor.text[:self.position] + self.editor.text[self.position + self.length:]
        print(f"Deleted {self.length} characters from position {self.position}")
        print(f"Current text: '{self.editor.text}'")

    def undo(self):
        self.editor.text = self.editor.text[:self.position] + self.deleted_text + self.editor.text[self.position:]
        print(f"Undo delete: '{self.deleted_text}' at position {self.position}")
        print(f"Current text: '{self.editor.text}'")

    def redo(self):
        self.execute()
        print(f"Redo delete: '{self.deleted_text}' at position {self.position}")
        print(f"Current text: '{self.editor.text}'")


# 编辑器类
class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []
        self.redo_history = []

    def insert_text(self, text, position):
        command = InsertTextCommand(self, text, position)
        command.execute()
        self.history.append(command)
        self.redo_history.clear()  # Clear redo history when a new action is performed

    def delete_text(self, length, position):
        command = DeleteTextCommand(self, length, position)
        command.execute()
        self.history.append(command)
        self.redo_history.clear()  # Clear redo history when a new action is performed

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
            self.redo_history.append(command)
        else:
            print("No more actions to undo")

    def redo(self):
        if self.redo_history:
            command = self.redo_history.pop()
            command.redo()
            self.history.append(command)
        else:
            print("No more actions to redo")


# 客户端代码
if __name__ == "__main__":
    editor = TextEditor()
    editor.insert_text("Hello", 0)
    editor.insert_text(" World", 5)
    editor.delete_text(5, 5)
    editor.undo()
    editor.redo()
    editor.undo()
    editor.redo()
