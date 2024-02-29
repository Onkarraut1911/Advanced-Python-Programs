class Student(object):
    def __init__(self , n , r):    #constructor
        self.name = n
        self.roll = r

    def disp(self):                 # instance method
        print("Student Name: ",self.name)
        print("Student Roll: ",self.roll)

# passing members of one class to another class
        
class User(object):
    @staticmethod       #decorator
    def show(s):         # static method
        print("User Name : ",s.name)
        print("User Roll : ",s.roll)
        s.disp()

# creating object of student class
stu = Student('Rahul',101)
User.show(stu)