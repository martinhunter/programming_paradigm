class Attr1:
    def __init__(self, name):
        self.name = name


class Item:
    def __init__(self, attr1):
        self.attr1 = attr1

    def transform(self):
        return '{} lol'.format(self.attr1.name)


# API
def display():
    attr1 = Attr1('attr1')
    instance = Item(attr1)
    content = instance.transform()
    return content


if __name__ == '__main__':
    content = display()
    print(content)
