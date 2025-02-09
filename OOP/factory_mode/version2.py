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
def func1(task_type):
    if task_type == 'TypeA':
        instance = TypeA()
    elif task_type == 'TypeB':
        instance = TypeB()
    else:
        raise Exception
    instance.func1()


def func2(task_type):
    if task_type == 'TypeA':
        instance = TypeA()
    elif task_type == 'TypeB':
        instance = TypeB()
    else:
        raise Exception
    instance.func2()
