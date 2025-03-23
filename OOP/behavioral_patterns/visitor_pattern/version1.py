class Document:
    def create(self):
        print("Creating document")

    def edit(self):
        print("Editing document")

    def save(self):
        print("Saving document")

# 客户端代码
if __name__ == "__main__":
    doc = Document()
    doc.create()
    doc.edit()
    doc.save()
