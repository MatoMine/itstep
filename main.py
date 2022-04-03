class Student:
    amount_of_student=0
    def __init__(self, height=160):
        self.height=height
        Student.amount_of_students+=1
    def grow(self, height=170):
        self.height+=height
nick=Student()
nick.grow(height=15)
print(kate.height)
print(nick.height)


