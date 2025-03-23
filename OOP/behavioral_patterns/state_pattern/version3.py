from abc import ABC, abstractmethod

# 抽象状态
class OrderState(ABC):
    @abstractmethod
    def pay(self, order):
        pass

    @abstractmethod
    def ship(self, order):
        pass

    @abstractmethod
    def complete(self, order):
        pass

    @abstractmethod
    def cancel(self, order):
        pass

    @abstractmethod
    def rollback(self, order):
        pass

# 具体状态：已创建
class CreatedState(OrderState):
    def pay(self, order):
        order.state = PaidState()
        print("Order paid")

    def ship(self, order):
        print("Order not paid yet")

    def complete(self, order):
        print("Order not paid yet")

    def cancel(self, order):
        order.state = CancelledState()
        print("Order cancelled")

    def rollback(self, order):
        print("Order cannot be rolled back")

# 具体状态：已支付
class PaidState(OrderState):
    def pay(self, order):
        print("Order already paid")

    def ship(self, order):
        order.state = ShippedState()
        print("Order shipped")

    def complete(self, order):
        print("Order not shipped yet")

    def cancel(self, order):
        order.state = CancelledState()
        print("Order cancelled")

    def rollback(self, order):
        order.state = CreatedState()
        print("Order rolled back to created state")

# 具体状态：已发货
class ShippedState(OrderState):
    def pay(self, order):
        print("Order already paid")

    def ship(self, order):
        print("Order already shipped")

    def complete(self, order):
        order.state = CompletedState()
        print("Order completed")

    def cancel(self, order):
        order.state = CancelledState()
        print("Order cancelled")

    def rollback(self, order):
        order.state = PaidState()
        print("Order rolled back to paid state")

# 具体状态：已完成
class CompletedState(OrderState):
    def pay(self, order):
        print("Order already paid")

    def ship(self, order):
        print("Order already shipped")

    def complete(self, order):
        print("Order already completed")

    def cancel(self, order):
        order.state = CancelledState()
        print("Order cancelled")

    def rollback(self, order):
        order.state = ShippedState()
        print("Order rolled back to shipped state")

# 具体状态：已取消
class CancelledState(OrderState):
    def pay(self, order):
        print("Order cannot be paid")

    def ship(self, order):
        print("Order cannot be shipped")

    def complete(self, order):
        print("Order cannot be completed")

    def cancel(self, order):
        print("Order already cancelled")

    def rollback(self, order):
        print("Order cannot be rolled back")

# 订单类
class Order:
    def __init__(self):
        self.state = CreatedState()

    def pay(self):
        self.state.pay(self)

    def ship(self):
        self.state.ship(self)

    def complete(self):
        self.state.complete(self)

    def cancel(self):
        self.state.cancel(self)

    def rollback(self):
        self.state.rollback(self)

# 客户端代码
if __name__ == "__main__":
    order = Order()
    order.pay()
    order.ship()
    order.complete()
    order.cancel()
    order.rollback()
