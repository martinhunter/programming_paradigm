class RealSubject:
    def request(self):
        print("RealSubject: Handling request.")


# 客户端代码
subject = RealSubject()
subject.request()  # 输出：RealSubject: Handling request.
