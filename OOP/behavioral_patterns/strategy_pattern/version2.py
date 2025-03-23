class Payment:
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        if self.validate(amount):
            print(f"Paying ${amount} using Credit Card")
        else:
            print("Payment failed: Invalid amount")

    def validate(self, amount):
        return amount > 0

class PayPalPayment(Payment):
    def pay(self, amount):
        if self.validate(amount):
            print(f"Paying ${amount} using PayPal")
        else:
            print("Payment failed: Invalid amount")

    def validate(self, amount):
        return amount > 0

class BankTransferPayment(Payment):
    def pay(self, amount):
        if self.validate(amount):
            print(f"Paying ${amount} using Bank Transfer")
        else:
            print("Payment failed: Invalid amount")

    def validate(self, amount):
        return amount > 0

class PaymentContext:
    def __init__(self):
        self.payment_method = None

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def pay(self, amount):
        if self.payment_method:
            self.payment_method.pay(amount)
        else:
            print("No payment method set")

# 客户端代码
if __name__ == "__main__":
    context = PaymentContext()

    context.set_payment_method(CreditCardPayment())
    context.pay(100)

    context.set_payment_method(PayPalPayment())
    context.pay(200)

    context.set_payment_method(BankTransferPayment())
    context.pay(300)

    context.set_payment_method(CreditCardPayment())
    context.pay(-50)  # Invalid amount
