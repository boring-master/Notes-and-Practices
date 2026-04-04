class Student:
    name = None
    def say_hi(self):
        print(f'大家好，我是{self.name}，请大家多多关照')
    def say_hi2(self,msg):
        print(f'大家好，我是{self.name}，{msg}')
stu = Student()
stu.name = '总经理'
stu.say_hi()
stu2 = Student()
stu2.name = '辣椒酱'
stu2.say_hi2('还挺不错的')

