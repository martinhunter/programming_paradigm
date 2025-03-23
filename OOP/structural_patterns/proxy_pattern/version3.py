class RealSubject:
    def request(self):
        print("RealSubject: Handling request.")


class Proxy:
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def authenticate(self):
        print("Authentication: Verifying access.")

    def log_request(self):
        print("Logging: Request is being made.")

    def request(self):
        self.authenticate()
        self.log_request()
        self.real_subject.request()


# 客户端代码
real_subject = RealSubject()
proxy = Proxy(real_subject)
proxy.request()
