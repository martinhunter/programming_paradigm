from abc import ABC, abstractmethod

# 中介者接口
class Mediator(ABC):
    @abstractmethod
    def send(self, message, user):
        pass

# 具体中介者：聊天室
class ChatRoom(Mediator):
    def __init__(self):
        self.users = []

    def register_user(self, user):
        self.users.append(user)

    def send(self, message, user):
        for u in self.users:
            if u != user:
                u.receive_message(message)

# 用户类
class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send_message(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send(message, self)

    def receive_message(self, message):
        print(f"{self.name} receives: {message}")

# 客户端代码
if __name__ == "__main__":
    chat_room = ChatRoom()

    user1 = User("Alice", chat_room)
    user2 = User("Bob", chat_room)
    user3 = User("Charlie", chat_room)

    chat_room.register_user(user1)
    chat_room.register_user(user2)
    chat_room.register_user(user3)

    user1.send_message("Hello Bob!")
    user2.send_message("Hi Alice!")
    user3.send_message("Hello everyone!")
