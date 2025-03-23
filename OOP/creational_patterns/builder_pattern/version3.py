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


class ItemBuilder:
    def __init__(self):
        self.attr1 = None
        self.attr2 = None
        self.attr3 = None
        self.attr4 = None

    def set_attr1(self, value):
        self.attr1 = value
        return self

    def set_attr2(self, value):
        self.attr2 = value
        return self

    def transform(self):
        return '{} {} {} {}'.format(self.attr1.name, self.attr2.name, self.attr3.name, self.attr4.name)


# API
class DisplayDirector:
    @staticmethod
    def display_1_2():
        builder = ItemBuilder()
        builder.set_attr1(
            Attr1('attr1')
        ).set_attr2(
            Attr2('attr2')
        )
        content = builder.transform()
        return content

    @staticmethod
    def display_1_3_4():
        builder = ItemBuilder()
        builder.set_attr1(Attr1('attr1'))
        builder.attr3 = Attr3('attr3')
        builder.attr4 = Attr3('attr4')
        content = builder.transform()
        return content


if __name__ == '__main__':
    content = DisplayDirector.display_1_2()
    print(content)

    content = DisplayDirector.build_item_1_3_4()
    print(content)
