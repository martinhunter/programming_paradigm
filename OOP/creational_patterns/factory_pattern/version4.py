from abc import ABC, abstractmethod  # 导入抽象基类


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


# APIS
def type_factory(task_type):
    if task_type == 'TypeA':
        instance = TypeA()
    elif task_type == 'TypeB':
        instance = TypeB()
    elif task_type == 'TypeC':
        instance = TypeC()
    else:
        raise Exception
    return instance


if __name__ == '__main__':
    instance = type_factory('TypeC')   # compare with version 1
    instance.func1()
    instance.func2_3()
