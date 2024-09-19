
# Parent class (Base class)
class Course:
    def contact_details(self):
        print("The head office is located in Cape Town.")

# Subclass (Derived class)
class OOPCourse(Course):
    def __init__(self, description="OOP Fundamentals", trainer="Mr Anon A. Mouse"):
        # Constructor with default values
        self.description = description
        self.trainer = trainer

    def trainer_details(self):
        # Method to print course description and trainer details
        print(f"This course is about: {self.description}")
        print(f"The trainer for this course is: {self.trainer}")

    def show_course_id(self):
        # Method to print the course ID
        print("The course ID number is: #12345")


# Create an object of the OOPCourse subclass
course_1 = OOPCourse()

# Call the methods
course_1.contact_details()    # Prints head office location
course_1.trainer_details()    # Prints course description and trainer name
course_1.show_course_id()     # Prints course ID
