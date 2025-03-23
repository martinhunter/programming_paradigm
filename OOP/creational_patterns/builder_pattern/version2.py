class Attr1:
    def __init__(self, name):
        self.name = name


class Attr2:
    def __init__(self, name):
        self.name = name


class Attr3:
    def __init__(self, name):
        self.name = name


class Attr4:
    def __init__(self, name):
        self.name = name


class Item:
    def __init__(self, attr1, attr2, attr3, attr4):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
        self.attr4 = attr4

    def transform(self):
        return '{} {} {} {}'.format(self.attr1.name, self.attr2.name, self.attr3.name, self.attr4.name)


# API
def display_1_2():
    attr1 = Attr1('attr1')
    attr2 = Attr2('attr2')
    instance = Item(attr1, attr2, None, None)
    content = instance.transform()
    return content


def display_1_3():
    attr1 = Attr1('attr1')
    attr3 = Attr2('attr3')
    instance = Item(attr1, None, attr3, None)
    content = instance.transform()
    return content


if __name__ == '__main__':
    content = display_1_2()
    print(content)

    content = display_1_3()
    print(content)
