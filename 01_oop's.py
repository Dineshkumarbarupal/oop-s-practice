# class Student:      # this is a class 
#     name = "karan"

# s1 = Student()      # this is a object
# print(s1.name)

# s2 = Student()      # this is a object
# print(s2.name)      


# class Student:
#     def __init__(self):
#         print("Hello from __init__ function")

# s1 = Student()   # output = Hello from __init__ function


# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# s1 = Student("dinesh", 19)

# print(f"student {s1.name} his age {s1.age} year.")



# methods in oop's


# class Student:
#     def __init__(self,name,age):
#         self.sname = name
#         self.sage = age

#     def student(self):
#        print("hello from method") 

# s1 = Student("dinesh",19)
# print(s1.sname)
# print(s1.sage)
# s1.student()


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @staticmethod
    def welcome():
        print("hello from staticmathod")

   

s1 = Student("dinesh",19)
print(s1.name,s1.age)

s1.welcome()











