
 # Step 1: Take user inputs
name = input("Enter the person's name: ")
age = int(input("Enter the person's age: "))
hair_colour = input("Enter the person's hair colour: ")
eye_colour = input("Enter the person's eye colour: ")

# Step 2: Define the Adult class
class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    # Method to check if the person can drive
    def can_drive(self):
        print(f"{self.name} is old enough to drive.")

# Step 3: Define the Child class (subclass of Adult)
class Child(Adult):
    # Overriding the can_drive method
    def can_drive(self):
        print(f"{self.name} is too young to drive.")

# Step 4: Logic to determine if the person is an adult or a child
if age >= 18:
    # Create an Adult instance
    person = Adult(name, age, hair_colour, eye_colour)
else:
    # Create a Child instance
    person = Child(name, age, hair_colour, eye_colour)

# Step 5: Call the can_drive method
person.can_drive()
