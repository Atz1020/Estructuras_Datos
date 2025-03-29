from model.ticket import Ticket
from model.node import Node

class TicketController:
    def __init__(self):
        self.head: Node = None

    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, ticket: Ticket) -> None:
        new_node = Node(ticket, ticket.priority)
        if self.is_empty() or self.head.priority < new_node.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority >= new_node.priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self) -> Ticket:
        if self.is_empty():
            return None
        ticket = self.head.data
        self.head = self.head.next
        return ticket

    def peek(self) -> Ticket:
        return self.head.data if not self.is_empty() else None

    def get_all(self) -> list[Ticket]:
        tickets = []
        current = self.head
        while current:
            tickets.append(current.data)
            current = current.next
        return tickets
