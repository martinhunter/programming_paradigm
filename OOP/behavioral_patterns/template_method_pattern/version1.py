class Circle:
    def draw(self):
        print("Drawing a circle")

class Rectangle:
    def draw(self):
        print("Drawing a rectangle")

class ShapeCounter:
    def __init__(self):
        self.circle_count = 0
        self.rectangle_count = 0

    def count(self, shape):
        if isinstance(shape, Circle):
            self.circle_count += 1
        elif isinstance(shape, Rectangle):
            self.rectangle_count += 1

# 客户端代码
if __name__ == "__main__":
    shapes = [Circle(), Rectangle(), Circle()]

    for shape in shapes:
        shape.draw()

    counter = ShapeCounter()
    for shape in shapes:
        counter.count(shape)

    print(f"Circles: {counter.circle_count}, Rectangles: {counter.rectangle_count}")
