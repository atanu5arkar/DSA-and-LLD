class Node:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_to_head(self, value) -> None:
        node = Node(value, self.head)
        self.head = node

        if not self.tail:
            self.tail = self.head

    def add_to_tail(self, value) -> None:
        node = Node(value, None)

        if not self.tail:
            self.head = self.tail = node
            return
        
        self.tail.next = node
        self.tail = node

    def traverse(self) -> None:
        pass


ll = LinkedList()

ll.add_to_head(20)
ll.add_to_tail(10)
