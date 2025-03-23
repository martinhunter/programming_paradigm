class AlipayPayment:
    def __init__(self, implementor):
        self.implementor = implementor

    def pay(self, amount):
        print(f"Processing Alipay Auth...")
        self.implementor.process_payment(amount)


class OnlinePaymentImplementor:
    def process_payment(self, amount):
        print(f"Processing online payment of ${amount:.2f}")
        # 模拟在线支付的费用
        fee = amount * 0.02
        print(f"Online payment fee: ${fee:.2f}")
        print(f"Total amount paid: ${amount + fee:.2f}")


if __name__ == "__main__":
    online_implementor = OnlinePaymentImplementor()

    alipay_payment = AlipayPayment(online_implementor)

    alipay_payment.pay(200.0)
