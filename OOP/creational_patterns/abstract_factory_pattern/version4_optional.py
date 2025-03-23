from abc import ABC, abstractmethod  # 导入抽象基类


class IChecker(ABC):
    @abstractmethod
    def check(self, value):
        pass


class CheckerA(IChecker):
    def check(self, value):
        print('check', self.__class__.__name__)
        return True


class CheckerB(CheckerA):
    def check(self, value):
        print('check', self.__class__.__name__)
        return True

    def c2(self, value):
        pass


class CheckerC(CheckerB):
    def check(self, value):
        print('check', self.__class__.__name__)
        return True

    def c3(self, value):
        pass


class IType(ABC):
    @abstractmethod
    def func1(self):
        pass

    @abstractmethod
    def func2(self):
        pass

    @abstractmethod
    def func3(self):
        pass

    def func2_3(self):
        self.func2()
        self.func3()


class TypeA(IType):
    def func1(self):
        print('typeA, func1')

    def func2(self):
        print('typeA, func2')

    def func3(self):
        print('typeA, func3')


class TypeB(TypeA):
    def func3(self):
        print('typeB, func3')
        self.func4()

    def func4(self):
        print('typeB, func4')


class TypeC(TypeB):
    def func1(self):
        print('typeC, func1')
        self.func5()

    def func5(self):
        print('typeC, func5')


class TaskFactory:
    def __init__(self, mapping):
        self.mapping = mapping

    def get_checker(self):
        return self.mapping['checker']()

    def get_type(self):
        return self.mapping['type']()


# APIS
def task_abstract_factory(task_type):
    if task_type == 'TypeA':
        mapping = {
            'checker': CheckerA,
            'type': TypeA
        }
    elif task_type == 'TypeB':
        mapping = {
            'checker': CheckerB,
            'type': TypeB
        }
    elif task_type == 'TypeC':
        mapping = {
            'checker': CheckerC,
            'type': TypeC
        }
    else:
        raise Exception
    return TaskFactory(mapping)


if __name__ == '__main__':
    value = 22
    factory = task_abstract_factory('TypeC')  # compare with version 1
    checker = factory.get_checker()
    result = checker.check(value)
    if result:
        instance = factory.get_type()
        instance.func1()
        instance.func2_3()
