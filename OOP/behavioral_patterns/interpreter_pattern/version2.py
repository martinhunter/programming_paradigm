class ExpressionEvaluator:
    def __init__(self):
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }

    def evaluate(self, expression):
        tokens = expression.split()
        stack = []
        for token in tokens:
            if token in self.operators:
                b = stack.pop()
                a = stack.pop()
                result = self.operators[token](a, b)
                stack.append(result)
            else:
                stack.append(float(token))
        return stack[0]

# 客户端代码
if __name__ == "__main__":
    evaluator = ExpressionEvaluator()
    expression = "3 + 5"
    print(f"Result of '{expression}': {evaluator.evaluate(expression)}")

    expression = "2 * 4 + 3"
    print(f"Result of '{expression}': {evaluator.evaluate(expression)}")
