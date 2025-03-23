class RealSubject:
    def request(self):
        print("RealSubject: Handling request.")

# 客户端代码
def log_request():
    print("Logging: Request is being made.")

def authenticate():
    print("Authentication: Verifying access.")

# 在客户端中直接添加功能
authenticate()
log_request()
subject = RealSubject()
subject.request()
