class Payment:
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paying ${amount} using Credit Card")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paying ${amount} using PayPal")

# 客户端代码
if __name__ == "__main__":
    payment = CreditCardPayment()
    payment.pay(100)

    payment = PayPalPayment()
    payment.pay(200)
