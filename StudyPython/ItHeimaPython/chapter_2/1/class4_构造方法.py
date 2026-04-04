# class Student:
#     name = None
#     age = None
#     tel = None
#     def __init__(self, name, age, tel):
#         self.name = name
#         self.age = age
#         self.tel = tel
#         print(f'Student类创建了一个类对象')
# stu = Student('总经理','31','123456')
# print(stu.name)
# print(stu.age)
# print(stu.tel)

for i in range(1,11):
    print(f'当前录入第{i}位学生信息，总共10位')
    class Stu:
        def __init__(self, name, age, address):
            self.name = name
            self.age = age
            self.address = address
    stu = Stu(name = input('请输入姓名：'),age = input('请输入年龄：'),address = input('请输入地址：'))
    print(f'第{i}位学生录入完成，信息为【姓名：{stu.name}，年龄：{stu.age}，地址：{stu.address}】')


