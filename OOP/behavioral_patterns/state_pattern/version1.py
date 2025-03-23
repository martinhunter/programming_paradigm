class Order:
    def __init__(self):
        self.state = "created"

    def pay(self):
        if self.state == "created":
            self.state = "paid"
            print("Order paid")
        else:
            print("Order already paid")

    def ship(self):
        if self.state == "paid":
            self.state = "shipped"
            print("Order shipped")
        else:
            print("Order not paid yet")

    def complete(self):
        if self.state == "shipped":
            self.state = "completed"
            print("Order completed")
        else:
            print("Order not shipped yet")

# 客户端代码
if __name__ == "__main__":
    order = Order()
    order.pay()
    order.ship()
    order.complete()
