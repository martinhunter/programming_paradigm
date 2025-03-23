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
    def __init__(self, attr1=None, attr2=None, attr3=None, attr4=None):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
        self.attr4 = attr4

    def transform(self):
        return '{} {} {} {}'.format(self.attr1.name, self.attr2.name, self.attr3.name, self.attr4.name)


# API
class ItemBuilderBuilder:
    @staticmethod
    def build_item_1_2():
        attr1 = Attr1('attr1')
        attr2 = Attr2('attr2')
        builder = ItemBuilder(attr1=attr1, attr2=attr2)
        return builder

    @staticmethod
    def build_item_1_3():
        attr1 = Attr1('attr1')
        attr3 = Attr2('attr3')
        builder = ItemBuilder(attr1=attr1, attr3=attr3)
        return builder


if __name__ == '__main__':
    builder = ItemBuilderBuilder.build_item_1_2()
    builder.show_attrs()

    builder = ItemBuilderBuilder.build_item_1_3()
    builder.show_attrs()
