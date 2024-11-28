class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []

    def add_marks(self, mark):
        self.marks.append(mark)

    def calculate_average(self):
        if len(self.marks) > 0:
            return sum(self.marks) / len(self.marks)
        else:
            return 0

    def display_results(self):
        average_marks = self.calculate_average()
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Average Marks: {average_marks:.2f}")



student1 = Student("Nandini", "1")
student1.add_marks(85)
student1.add_marks(90)
student1.add_marks(78)
student1.display_results()

student2 = Student("Kavya", "3")
student2.add_marks(92)
student2.add_marks(88)
student2.display_results()
