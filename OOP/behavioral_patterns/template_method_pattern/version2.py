class Circle:
    def draw(self):
        print("Drawing a circle")

    def area(self):
        return 3.14 * 10 * 10  # Assuming radius is 10

class Rectangle:
    def draw(self):
        print("Drawing a rectangle")

    def area(self):
        return 10 * 20  # Assuming width is 10, height is 20

class ShapeCounter:
    def __init__(self):
        self.circle_count = 0
        self.rectangle_count = 0

    def count(self, shape):
        if isinstance(shape, Circle):
            self.circle_count += 1
        elif isinstance(shape, Rectangle):
            self.rectangle_count += 1

class ShapeAreaCalculator:
    def __init__(self):
        self.total_area = 0

    def calculate(self, shape):
        self.total_area += shape.area()

# 客户端代码
if __name__ == "__main__":
    shapes = [Circle(), Rectangle(), Circle()]

    for shape in shapes:
        shape.draw()

    counter = ShapeCounter()
    for shape in shapes:
        counter.count(shape)

    print(f"Circles: {counter.circle_count}, Rectangles: {counter.rectangle_count}")

    area_calculator = ShapeAreaCalculator()
    for shape in shapes:
        area_calculator.calculate(shape)

    print(f"Total area: {area_calculator.total_area}")
