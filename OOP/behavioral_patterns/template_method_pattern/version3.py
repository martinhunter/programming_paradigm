from abc import ABC, abstractmethod

# 抽象元素
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# 具体元素：圆形
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

    def accept(self, visitor):
        visitor.visit_circle(self)

# 具体元素：矩形
class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

    def accept(self, visitor):
        visitor.visit_rectangle(self)

# 抽象访问者
class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass

# 具体访问者：计数器
class ShapeCounter(Visitor):
    def __init__(self):
        self.circle_count = 0
        self.rectangle_count = 0

    def visit_circle(self, circle):
        self.circle_count += 1

    def visit_rectangle(self, rectangle):
        self.rectangle_count += 1

# 具体访问者：面积计算器
class ShapeAreaCalculator(Visitor):
    def __init__(self):
        self.total_area = 0

    def visit_circle(self, circle):
        self.total_area += 3.14 * 10 * 10  # Assuming radius is 10

    def visit_rectangle(self, rectangle):
        self.total_area += 10 * 20  # Assuming width is 10, height is 20

# 客户端代码
if __name__ == "__main__":
    shapes = [Circle(), Rectangle(), Circle()]

    for shape in shapes:
        shape.draw()

    counter = ShapeCounter()
    area_calculator = ShapeAreaCalculator()

    for shape in shapes:
        shape.accept(counter)
        shape.accept(area_calculator)

    print(f"Circles: {counter.circle_count}, Rectangles: {counter.rectangle_count}")
    print(f"Total area: {area_calculator.total_area}")
