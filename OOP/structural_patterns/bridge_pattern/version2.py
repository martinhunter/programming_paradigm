class RedCircle:
    def draw(self):
        print("绘制红色圆形")


class BlueCircle:
    def draw(self):
        print("绘制蓝色圆形")


class RedRectangle:
    def draw(self):
        print("绘制红色矩形")


class BlueRectangle:
    def draw(self):
        print("绘制蓝色矩形")


# 使用示例
red_circle = RedCircle()
blue_rectangle = BlueRectangle()

red_circle.draw()  # 输出：绘制红色圆形
blue_rectangle.draw()  # 输出：绘制蓝色矩形
