from abc import ABC, abstractmethod

# 抽象观察者
class Observer(ABC):
    @abstractmethod
    def update(self, symbol, price):
        pass

# 具体观察者：邮件通知
class EmailObserver(Observer):
    def update(self, symbol, price):
        print(f"Email notification: Stock {symbol} price updated to {price}")

# 具体观察者：短信通知
class SMSObserver(Observer):
    def update(self, symbol, price):
        print(f"SMS notification: Stock {symbol} price updated to {price}")

# 抽象主题
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# 具体主题：股票
class Stock(Subject):
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.symbol, self.price)

    def update_price(self, new_price):
        self.price = new_price
        print(f"Stock {self.symbol} price updated to {self.price}")
        self.notify_observers()

# 客户端代码
if __name__ == "__main__":
    stock = Stock("AAPL", 150)
    email_observer = EmailObserver()
    sms_observer = SMSObserver()

    stock.register_observer(email_observer)
    stock.register_observer(sms_observer)

    stock.update_price(155)
    stock.update_price(160)
