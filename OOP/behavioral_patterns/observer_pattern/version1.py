class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    def update_price(self, new_price):
        self.price = new_price
        print(f"Stock {self.symbol} price updated to {self.price}")

# 客户端代码
if __name__ == "__main__":
    stock = Stock("AAPL", 150)
    stock.update_price(155)
    stock.update_price(160)
