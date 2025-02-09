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
def func1(task_type):
    instance = get_type_instance(task_type)
    instance.func1()


def func2(task_type):
    instance = get_type_instance(task_type)
    instance.func2()


def func2_3(task_type):
    instance = get_type_instance(task_type)
    instance.func2()
    instance.func3()
