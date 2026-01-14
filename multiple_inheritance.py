class Teacher:
    def __init__(self,salary):
        self.salary = salary
    def teach(self):
        return "Teaching students."
class Student:
    def __init__(self,grade):
        self.grade = grade
    def study(self):
        return "Studying for exams."
    
class TeachingAssistant(Teacher, Student):
    def __init__(self, salary, grade):
        super().__init__(salary)
        Student.__init__(self, grade)
    def assist(self):
        return "Assisting in classes and labs."
    
ta = TeachingAssistant(50000, 'A')
print(ta.teach())          # From Teacher class
print(ta.study())         # From Student class
print(ta.assist())        # From TeachingAssistant class
print(f"TA Salary: ${ta.salary}, TA Grade: {ta.grade}")