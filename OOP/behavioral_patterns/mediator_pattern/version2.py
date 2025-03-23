class User:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

    def send_message(self, message, recipient):
        for friend in self.friends:
            if friend.name == recipient:
                friend.receive_message(message)
                break

    def receive_message(self, message):
        print(f"{self.name} receives: {message}")

# 客户端代码
if __name__ == "__main__":
    user1 = User("Alice")
    user2 = User("Bob")
    user3 = User("Charlie")

    user1.add_friend(user2)
    user1.add_friend(user3)
    user2.add_friend(user1)
    user2.add_friend(user3)
    user3.add_friend(user1)
    user3.add_friend(user2)

    user1.send_message("Hello Bob!", "Bob")
    user2.send_message("Hi Alice!", "Alice")
    user3.send_message("Hello everyone!", "Alice")
