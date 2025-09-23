class MinStack:
    """ Each operation is performed in O(1) time """

    def __init__(self):
        self.items = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.items.append(val)

        # Maintain an ordered list of possible minimums
        if not len(self.min_stack) or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        top = self.items.pop()
        if top == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.items[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]


min_stack = MinStack()

print(min_stack.push(2))
print(min_stack.push(1))
print(min_stack.push(0))
print(min_stack.get_min())
print(min_stack.top())
print(min_stack.pop())
print(min_stack.get_min())
