class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def update_price(self, new_price):
        self.price = new_price
        print(f"Stock {self.symbol} price updated to {self.price}")
        for subscriber in self.subscribers:
            subscriber.notify(self.symbol, self.price)

class Subscriber:
    def notify(self, symbol, price):
        pass

class EmailSubscriber(Subscriber):
    def notify(self, symbol, price):
        print(f"Email notification: Stock {symbol} price updated to {price}")

class SMSSubscriber(Subscriber):
    def notify(self, symbol, price):
        print(f"SMS notification: Stock {symbol} price updated to {price}")

# 客户端代码
if __name__ == "__main__":
    stock = Stock("AAPL", 150)
    email_subscriber = EmailSubscriber()
    sms_subscriber = SMSSubscriber()

    stock.add_subscriber(email_subscriber)
    stock.add_subscriber(sms_subscriber)

    stock.update_price(155)
    stock.update_price(160)
