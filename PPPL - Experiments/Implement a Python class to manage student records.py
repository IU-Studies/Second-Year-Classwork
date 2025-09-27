# Implement a Python class to manage student records, demonstrating inheritance and basic error handling for invalid inputs.

class Person:
    def __init__(self, name, age):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer.")
        
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)

        if not student_id or not isinstance(student_id, str):
            raise ValueError("Student ID must be a non-empty string.")

        self.student_id = student_id
        self.grades = {}

    def add_grade(self, subject, grade):
        if not subject or not isinstance(subject, str):
            raise ValueError("Subject must be a non-empty string.")
        if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
            raise ValueError("Grade must be a number between 0 and 100.")

        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        grades_str = ", ".join(f"{subject}: {grade}" for subject, grade in self.grades.items())
        return f"{super().__str__()}, Student ID: {self.student_id}, Grades: {{{grades_str}}}"

try:
    student = Student("John", 20, "S123")
    student.add_grade("Math", 85)
    student.add_grade("Science", 90)
    print(student)
    print(f"Average Grade: {student.get_average_grade():.2f}")

except ValueError as e:
    print(f"Error: {e}")




""" 
#Simple Approach

class Person:
    def __init__(self, name, age):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer.")

        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average(self):
        total = sum(self.grades.values())
        count = len(self.grades)
        return total / count if count > 0 else 0

# Example use
try:
    s = Student("Anna", 17, "S001")
    s.add_grade("Math", 90)
    s.add_grade("English", 80)

    print(s.name, s.age, s.student_id)
    print("Grades:", s.grades)
    print("Average:", s.get_average())
except ValueError as e:
    print("Error:", e)

"""
