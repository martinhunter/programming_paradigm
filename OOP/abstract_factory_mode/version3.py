class CheckerA:
    def check(self, value):
        pass


class CheckerB(CheckerA):
    def check(self, value):
        pass

    def c2(self, value):
        pass


class CheckerC(CheckerB):
    def check(self, value):
        pass

    def c3(self, value):
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


class TypeC(TypeB):
    def func1(self):
        pass

    def func5(self):
        pass


def get_checker_instance(task_type):
    if task_type == 'TypeA':
        instance = CheckerA()
    elif task_type == 'TypeB':
        instance = CheckerB()
    elif task_type == 'TypeC':
        instance = CheckerC()
    else:
        raise Exception
    return instance


def get_type_instance(task_type):
    if task_type == 'TypeA':
        instance = TypeA()
    elif task_type == 'TypeB':
        instance = TypeB()
    elif task_type == 'TypeC':
        instance = TypeC()
    else:
        raise Exception
    return instance


# APIS
def func1(task_type, value):
    checker = get_checker_instance(task_type)
    result = checker.check(value)
    if result:
        instance = get_type_instance(task_type)
        instance.func1()


def func2(task_type, value):
    checker = get_checker_instance(task_type)
    result = checker.check(value)
    if result:
        instance = get_type_instance(task_type)
        instance.func2()


def func2_3(task_type, value):
    checker = get_checker_instance(task_type)
    result = checker.check(value)
    if result:
        instance = get_type_instance(task_type)
        instance.func2()
        instance.func3()
