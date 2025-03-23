from abc import ABC, abstractmethod


# 规定好两个抽象类交互的接口

# 支付实现接口
class PaymentImplementor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


# 抽象支付类
class Payment(ABC):
    def __init__(self, implementor):
        self.implementor = implementor

    @abstractmethod
    def pay(self, amount):
        pass


# 具体支付类
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Processing credit card payment...")
        self.implementor.process_payment(amount)


class AlipayPayment(Payment):
    def pay(self, amount):
        print(f"Processing Alipay payment...")
        self.implementor.process_payment(amount)


class WeChatPayment(Payment):
    def pay(self, amount):
        print(f"Processing WeChat payment...")
        self.implementor.process_payment(amount)


class ApplePayPayment(Payment):
    def pay(self, amount):
        print(f"Processing Apple Pay payment...")
        self.implementor.process_payment(amount)


# 具体实现类
class OnlinePaymentImplementor(PaymentImplementor):
    def process_payment(self, amount):
        print(f"Processing online payment of ${amount:.2f}")
        # 模拟在线支付的费用
        fee = amount * 0.02
        print(f"Online payment fee: ${fee:.2f}")
        print(f"Total amount paid: ${amount + fee:.2f}")


class OfflinePaymentImplementor(PaymentImplementor):
    def process_payment(self, amount):
        print(f"Processing offline payment of ${amount:.2f}")
        # 模拟线下支付的费用
        fee = amount * 0.01
        print(f"Offline payment fee: ${fee:.2f}")
        print(f"Total amount paid: ${amount + fee:.2f}")


class ThirdPartyPaymentImplementor(PaymentImplementor):
    def process_payment(self, amount):
        print(f"Processing third-party payment of ${amount:.2f}")
        # 模拟第三方支付的费用
        fee = amount * 0.03
        print(f"Third-party payment fee: ${fee:.2f}")
        print(f"Total amount paid: ${amount + fee:.2f}")


class BankTransferImplementor(PaymentImplementor):
    def process_payment(self, amount):
        print(f"Processing bank transfer of ${amount:.2f}")
        # 模拟银行转账的费用
        fee = amount * 0.015
        print(f"Bank transfer fee: ${fee:.2f}")
        print(f"Total amount paid: ${amount + fee:.2f}")


# 客户端代码
if __name__ == "__main__":
    # 创建不同的支付实现
    online_implementor = OnlinePaymentImplementor()
    offline_implementor = OfflinePaymentImplementor()
    third_party_implementor = ThirdPartyPaymentImplementor()
    bank_transfer_implementor = BankTransferImplementor()

    # 创建不同的支付方式
    credit_card_payment = CreditCardPayment(online_implementor)
    alipay_payment = AlipayPayment(offline_implementor)
    wechat_payment = WeChatPayment(third_party_implementor)
    apple_pay_payment = ApplePayPayment(bank_transfer_implementor)

    # 执行支付操作
    print("=== Payment 1 ===")
    credit_card_payment.pay(100.0)

    print("\n=== Payment 2 ===")
    alipay_payment.pay(200.0)

    print("\n=== Payment 3 ===")
    wechat_payment.pay(150.0)

    print("\n=== Payment 4 ===")
    apple_pay_payment.pay(300.0)
