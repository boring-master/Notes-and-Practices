# # __str__
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f'Student类对象，name：{self.name}，age:{self.age}'
# stu = Student('总经理',31)
# print(stu)
# print(str(stu))

# # __lt__
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __lt__(self,other):
#         return self.age < other.age
# stu1 = Student('总经理',31)
# stu2 = Student('辣椒酱',36)
# print(stu1 < stu2)
# print(stu1 > stu2)

# # __le__
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __le__(self,other):
#         return self.age <= other.age
# stu1 = Student('总经理',31)
# stu2 = Student('辣椒酱',36)
# print(stu1 <= stu2)
# print(stu1 >= stu2)

# __eq__
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __eq__(self,other):
        return self.age == other.age
stu1 = Student('总经理',31)
stu2 = Student('辣椒酱',36)
print(stu1 == stu2)

