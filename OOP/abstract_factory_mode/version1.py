# APIS
class CheckerA:
    def check(self, value):
        pass


class TypeA:
    def func1(self):
        pass

    def func2(self):
        pass

    def func3(self):
        pass


if __name__ == '__main__':
    value = 22
    checker = CheckerA()
    result = checker.check(value)
    if result:
        instance = TypeA()
        instance.func1()
        instance.func2()
