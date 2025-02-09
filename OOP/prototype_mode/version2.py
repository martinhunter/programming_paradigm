class Item:
    def __init__(self, attr1, attr2, simple_attr3):
        self.complex_attr1 = self.long_time_init_attr1(attr1)
        self.complex_attr2 = self.long_time_init_attr2(attr2)
        self.simple_attr3 = simple_attr3

    def long_time_init_attr1(self, attr1):
        return 'LONG_TIME_TASK:' + attr1

    def long_time_init_attr2(self, attr2):
        return 'LONG_TIME_TASK:' + attr2

    def show(self):
        print(self.complex_attr1, self.complex_attr2, self.simple_attr3)


# API
def run():
    simple_attrs = ['s1', 's2', 's3']

    for attr in simple_attrs:
        item = Item('one', 'two', attr)
        item.show()


if __name__ == '__main__':
    run()
