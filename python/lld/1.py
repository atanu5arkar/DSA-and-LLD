class Car:
    """
    The first parameter of every method is reserved for an instance. By convention, it is named
    self. Python automatically passes the instance to self. This allows instances to keep track of
    their own state.

    Instantiating a class involves calling the constructor, which initializes the state of an
    instance.
    """

    def __init__(self, brand: str, color: str, fuel: float):
        self.brand = brand
        self.color = color
        self.fuel = fuel

    def move_a_mile(self):
        print("The car went a mile.")
        self.fuel -= 0.5


# Instance of a Car, an object
car1 = Car("Tata", "steel", 25)

# Accessing instance attributes
print(car1.brand)
print(car1.fuel)

# Mutate state
car1.move_a_mile()
print(car1.fuel)
