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

    def cancel(self):
        if self.state == "created":
            self.state = "cancelled"
            print("Order cancelled")
        else:
            print("Order cannot be cancelled")

    def rollback(self):
        if self.state == "paid":
            self.state = "created"
            print("Order rolled back to created state")
        elif self.state == "shipped":
            self.state = "paid"
            print("Order rolled back to paid state")
        elif self.state == "completed":
            self.state = "shipped"
            print("Order rolled back to shipped state")
        else:
            print("Order cannot be rolled back")

# 客户端代码
if __name__ == "__main__":
    order = Order()
    order.pay()
    order.ship()
    order.complete()
    order.cancel()
    order.rollback()
