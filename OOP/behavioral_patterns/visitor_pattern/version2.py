class TextDocument:
    def create(self):
        print("Creating text document")

    def edit1(self):
        print("Editing text document")

    def save1(self):
        print("Saving text document as .txt")

class PDFDocument:
    def create(self):
        print("Creating PDF document")

    def edit2(self):
        print("Editing PDF document")

    def save2(self):
        print("Saving PDF document as .pdf")

# 客户端代码
if __name__ == "__main__":
    text_doc = TextDocument()
    text_doc.create()
    text_doc.edit1()
    text_doc.save1()

    pdf_doc = PDFDocument()
    pdf_doc.create()
    pdf_doc.edit2()
    pdf_doc.save2()
