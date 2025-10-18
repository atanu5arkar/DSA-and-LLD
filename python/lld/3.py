"""
Abstraction refers to a program structure where what an object does is revealed,
but not how it does it. For example, consider your laptop. You do not need to know
anything about its internals to switch it on, because it only requires pressing a
button.
"""


class Circle:
    __pi = 3.14

    def __init__(self, radius: float = 0) -> None:
        self.radius = radius

    def area(self):
        return self.__pi * self.radius**2


circ = Circle(5)

# No need for knowing how the area is calculated
print(circ.area())
