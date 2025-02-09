class CheckerA:
    def check(self, value):
        pass


class CheckerB(CheckerA):
    def check(self, value):
        pass

    def c2(self, value):
        pass


class TypeA:
    def func1(self):
        pass

    def func2(self):
        pass

    def func3(self):
        pass


class TypeB(TypeA):
    def func3(self):
        pass

    def func4(self):
        pass


# APIS
def func1(task_type, value):
    if task_type == 'TypeA':
        checker = CheckerA()
        result = checker.check(value)
    elif task_type == 'TypeB':
        checker = CheckerB()
        result = checker.check(value)
    else:
        raise Exception

    if result:
        if task_type == 'TypeA':
            instance = TypeA()
        elif task_type == 'TypeB':
            instance = TypeB()
        else:
            raise Exception
        instance.func1()


def func2(task_type, value):
    if task_type == 'TypeA':
        checker = CheckerA()
        result = checker.check(value)
        if result:
            instance = TypeA()
            instance.func2()
    elif task_type == 'TypeB':
        checker = CheckerB()
        result = checker.check(value)
        if result:
            instance = TypeB()
            instance.func2()
    else:
        raise Exception
