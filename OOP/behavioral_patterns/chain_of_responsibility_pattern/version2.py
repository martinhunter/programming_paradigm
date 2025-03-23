class SupportTicket:
    def __init__(self, level, description):
        self.level = level
        self.description = description

class SupportHandler:
    def __init__(self, level):
        self.level = level

    def handle(self, ticket):
        if ticket.level <= self.level:
            if self.level == 1:
                print(f"Junior Support: Handling ticket: {ticket.description}")
            elif self.level == 2:
                print(f"Mid Support: Handling ticket: {ticket.description}")
            elif self.level == 3:
                print(f"Senior Support: Handling ticket: {ticket.description}")
        else:
            print(f"Cannot handle ticket: {ticket.description}. Passing to next level.")
            # Simulate passing to next level
            next_handler = SupportHandler(self.level + 1)
            next_handler.handle(ticket)


# 客户端代码
if __name__ == "__main__":
    ticket1 = SupportTicket(1, "Low priority issue")
    ticket2 = SupportTicket(2, "Medium priority issue")
    ticket3 = SupportTicket(3, "High priority issue")

    handler = SupportHandler(1)
    handler.handle(ticket1)
    handler.handle(ticket2)
    handler.handle(ticket3)
