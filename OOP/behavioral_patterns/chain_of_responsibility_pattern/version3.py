from abc import ABC, abstractmethod

# 请求类
class SupportTicket:
    def __init__(self, level, description):
        self.level = level
        self.description = description

# 处理器接口
class SupportHandler(ABC):
    def __init__(self, level, next_handler=None):
        self.level = level
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, ticket):
        pass

# 具体处理器：初级支持
class JuniorSupportHandler(SupportHandler):
    def handle(self, ticket):
        if ticket.level <= self.level:
            print(f"Junior Support: Handling ticket: {ticket.description}")
        elif self.next_handler:
            self.next_handler.handle(ticket)

# 具体处理器：中级支持
class MidSupportHandler(SupportHandler):
    def handle(self, ticket):
        if ticket.level <= self.level:
            print(f"Mid Support: Handling ticket: {ticket.description}")
        elif self.next_handler:
            self.next_handler.handle(ticket)

# 具体处理器：高级支持
class SeniorSupportHandler(SupportHandler):
    def handle(self, ticket):
        if ticket.level <= self.level:
            print(f"Senior Support: Handling ticket: {ticket.description}")
        elif self.next_handler:
            self.next_handler.handle(ticket)

# 客户端代码
if __name__ == "__main__":
    ticket1 = SupportTicket(1, "Low priority issue")
    ticket2 = SupportTicket(2, "Medium priority issue")
    ticket3 = SupportTicket(3, "High priority issue")

    junior_handler = JuniorSupportHandler(1)
    mid_handler = MidSupportHandler(2)
    senior_handler = SeniorSupportHandler(3)

    junior_handler.next_handler = mid_handler
    mid_handler.next_handler = senior_handler

    junior_handler.handle(ticket1)
    junior_handler.handle(ticket2)
    junior_handler.handle(ticket3)
