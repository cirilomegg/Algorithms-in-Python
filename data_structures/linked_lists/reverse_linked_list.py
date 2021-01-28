class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = None

    def add(self, node):
        current = None

        if not self.head:
            self.head = node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = node

        return self.head

    def remove(self, node):
        current = self.head
        previous = None

        while current:
            if current == node:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next

                break

            previous = current
            current = current.next

        return self.head

    def print(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next

    def reverse(self):
        previous = None
        current = self.head
        next = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous

        return self.head


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add(Node("a"))
    linked_list.add(Node("b"))
    linked_list.add(Node("c"))
    linked_list.add(Node("d"))
    linked_list.print()  # a b c d

    linked_list.reverse()
    linked_list.print()  # d c b a
