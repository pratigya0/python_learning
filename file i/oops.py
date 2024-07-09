"""to map with real world scenarios, we started using objects in code.
    this is called object-oriented programming."""


# this is nothing we need to work with class & object in python


# class student:
#     name = "khushi"
# s1 = student()      #object(making actual thing)
# print(s1.name)

# class student:

#     def __int__(self, name, marks) :
#         self.name = name
#         self.marks = marks
#         print("add new student in database")
#
# # s1 = student("khu", 55)
# print(s1.name, s1.marks)
#
# s2 = student("ayu", 89)
# print(s2.name, s2.marks)

'''class oops:
    college_name = "lnct" #same thing for all the college 
    #default constructors
    """ def __init__(self):
         pass"""

    def __init__(self, fullname, age):  # parameterized constructors
        self.name = fullname
        self.your = age
        print("hello there")


s1 = oops("sunil", 56)
print(s1.name, s1.your, oops.college_name)'''


#=============class & instance attributes(any variable)===========
#isinstance(its value is different every time we define it and it define under the object attribute).

################ METHODS ################
'''methods are the function that belong to object'''

#Q. Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("Hi", self.name, "Your avg score is: ", sum/3)

s1 = student("tony", [56, 78, 41])
s1.get_avg()

s1.name = "jiya"
s1.get_avg()


#=========Static Method============
'''Methods that don’t use the self parameter (work at class level)'''
# class student:
#     @staticmethod #decorator
#     def college():
#         print("ABC college")


#Question from oops part1
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit method
    def debit(self, amount):
        self.balance -= amount
        print(("Rs.", amount, "was debited"))
        print("total balance = ", self.get_balance())


    def credit(self, amount):
        self.balance += amount
        print(("Rs.", amount, "was credited "))
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
print(acc1.balance)
print(acc1.account_no)





















