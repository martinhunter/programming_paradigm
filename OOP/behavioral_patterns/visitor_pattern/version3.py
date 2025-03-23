from abc import ABC, abstractmethod

# 抽象文档类
class Document(ABC):
    def process_document(self):
        self.create()
        self.edit()
        self.save()

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def save(self):
        pass

# 具体文档类：文本文档
class TextDocument(Document):
    def create(self):
        print("Creating text document")

    def edit(self):
        print("Editing text document")

    def save(self):
        print("Saving text document as .txt")

# 具体文档类：PDF文档
class PDFDocument(Document):
    def create(self):
        print("Creating PDF document")

    def edit(self):
        print("Editing PDF document")

    def save(self):
        print("Saving PDF document as .pdf")

# 客户端代码
if __name__ == "__main__":
    text_doc = TextDocument()
    text_doc.process_document()

    pdf_doc = PDFDocument()
    pdf_doc.process_document()
