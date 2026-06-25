#Base Class
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
    
    def login(self):
        print(f"{self.name} has logged in.")
    def logout(self):
        print(f"{self.name} has logged out.")

    def display_profile(self):
        print("User Profile")
        print("User Id: ", self.user_id)
        print("Name: ", self.name)
        print("Email: ", self.email)

#Student Class
class Student(User):
    def __init__(self, user_id, name, email, reg_no, course):
        super().__init__(user_id, name, email)
        self.reg_no = reg_no
        self.course = course
    
    def display_profile(self):
        super().display_profile()
        print("Registration Number: ", self.reg_no)
        print("Course: ", self.course)

#Supervisor Class
class Supervisor(User):
    def __init__(self, user_id, name, email, company_name, employee_id):
        super().__init__(user_id, name, email)
        self.company_name = company_name
        self.employee_id = employee_id
    
    def display_profile(self):
        super().display_profile()
        print("Company: ", self.company_name)
        print("Employee ID: ", self.employee_id)

#Multiple Inheritance
class StudentRepresentative(Student, Supervisor):
    def __init__(self, user_id, name, email, reg_no, course, company_name, employee_id):
        User.__init__(self, user_id, name, email)

        self.reg_no = reg_no
        self.course = course
        self.company_name = company_name
        self.employee_id = employee_id

    #Method Overriding
    def display_profile(self):
        print("Student Rep Profile:")
        print("User Id: ", self.user_id)
        print("Name: ",self.name)
        print("Email: ", self.email)
        print("Registration Number: ", self.reg_no)
        print("Course: ", self.course)
        print("Company: ", self.company_name)
        print("Employee ID: ", self.employee_id)

#Creating Objects
student = Student(
    "U001", "Shahidah", "kalanzi@gmail.com", "24/U/0000", "Software Engineering"
)

supevisor = Supervisor(
    "U002", "Elias", "elias23@yahoo.com", "Google Developers ltd", "EMP1000"
)

rep = StudentRepresentative(
    "U003", "Sarah", "kibuli@gmail.com",
      "24/U/08901",
      "Software Engineering",
      "Makerere Innovations",
      "EMP2000"
)

student.display_profile()
print()

supevisor.display_profile()
print()

rep.display_profile()
print()

rep.login()
rep.logout()

#Method resolution Order
print("Method Resolution Order:")
for cls in StudentRepresentative.mro():
    print(cls.__name__)


