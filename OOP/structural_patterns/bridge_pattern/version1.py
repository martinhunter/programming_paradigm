class AlipayPayment:
    def process_payment(self, amount):
        print(f"Processing online payment of ${amount:.2f}")
        # 模拟在线支付的费用
        fee = amount * 0.02
        print(f"Online payment fee: ${fee:.2f}")
        print(f"Total amount paid: ${amount + fee:.2f}")

    def pay(self, amount):
        print(f"Processing Alipay Auth...")
        self.process_payment(amount)


if __name__ == "__main__":
    alipay_payment = AlipayPayment()

    alipay_payment.pay(200.0)
