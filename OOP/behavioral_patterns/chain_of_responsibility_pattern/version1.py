class SupportTicket:
    def __init__(self, level, description):
        self.level = level
        self.description = description

class SupportHandler:
    def __init__(self, level):
        self.level = level

    def handle(self, ticket):
        if ticket.level <= self.level:
            print(f"Handling ticket: {ticket.description}")
        else:
            print(f"Cannot handle ticket: {ticket.description}. Passing to next level.")

# 客户端代码
if __name__ == "__main__":
    ticket1 = SupportTicket(1, "Low priority issue")
    ticket2 = SupportTicket(2, "Medium priority issue")
    ticket3 = SupportTicket(3, "High priority issue")

    handler = SupportHandler(2)
    handler.handle(ticket1)
    handler.handle(ticket2)
    handler.handle(ticket3)
