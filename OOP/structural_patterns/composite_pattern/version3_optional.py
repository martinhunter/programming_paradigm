from abc import ABC, abstractmethod
from typing import List

# 抽象组件接口
class UIComponent(ABC):
    @abstractmethod
    def paint(self):
        pass

    @abstractmethod
    def add(self, component):
        pass

    @abstractmethod
    def remove(self, component):
        pass

# 叶子节点：具体组件
class Button(UIComponent):
    def __init__(self, label: str):
        self.label = label

    def paint(self):
        print(f"Painting Button: {self.label}")

    def add(self, component):
        raise NotImplementedError("Button cannot have children")

    def remove(self, component):
        raise NotImplementedError("Button cannot have children")

# 复合节点：容器组件
class Panel(UIComponent):
    def __init__(self):
        self.children: List[UIComponent] = []

    def paint(self):
        print("Painting Panel")
        for child in self.children:
            child.paint()

    def add(self, component: UIComponent):
        self.children.append(component)

    def remove(self, component: UIComponent):
        self.children.remove(component)

# 客户端代码
if __name__ == "__main__":
    main_panel = Panel()
    button1 = Button("Button 1")
    button2 = Button("Button 2")

    main_panel.add(button1)
    main_panel.add(button2)

    # 模拟绘制
    main_panel.paint()
