def evaluate(expression):
    return eval(expression)

# 客户端代码
if __name__ == "__main__":
    expression = "3 + 5"
    print(f"Result of '{expression}': {evaluate(expression)}")

    expression = "2 * (4 + 3)"
    print(f"Result of '{expression}': {evaluate(expression)}")
