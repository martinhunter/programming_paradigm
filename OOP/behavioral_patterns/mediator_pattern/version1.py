class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, message):
        print(f"{self.name} sends: {message}")

    def receive_message(self, message):
        print(f"{self.name} receives: {message}")

# 客户端代码
if __name__ == "__main__":
    user1 = User("Alice")
    user2 = User("Bob")

    user1.send_message("Hello Bob!")
    user2.receive_message("Hello Bob!")

    user2.send_message("Hi Alice!")
    user1.receive_message("Hi Alice!")
