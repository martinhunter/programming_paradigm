from abc import ABC, abstractmethod

# 抽象表达式
class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

# 具体表达式：数字
class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value

# 具体表达式：加法
class Addition(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

# 具体表达式：减法
class Subtraction(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)

# 具体表达式：乘法
class Multiplication(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) * self.right.interpret(context)

# 具体表达式：除法
class Division(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) / self.right.interpret(context)

# 解释器上下文
class Context:
    def __init__(self, expression):
        self.expression = expression

# 客户端代码
if __name__ == "__main__":
    context = Context(None)

    # 构建表达式树
    expression = Addition(
        Number(3),
        Multiplication(
            Number(2),
            Number(4)
        )
    )

    print(f"Result of '3 + 2 * 4': {expression.interpret(context)}")

    expression = Subtraction(
        Number(10),
        Division(
            Number(8),
            Number(2)
        )
    )

    print(f"Result of '10 - 8 / 2': {expression.interpret(context)}")
