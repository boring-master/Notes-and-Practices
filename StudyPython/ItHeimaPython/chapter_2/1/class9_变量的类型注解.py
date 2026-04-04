import json
import random

# 基础数据类型注解
var_1:int = 10
var_2:str = 'heima'
var_3:bool = True
# 类对象类型注解
class Student:
    pass
stu:Student = Student()
# 基础容器类型注解
my_list:list = [1,2,3]
my_tuple:tuple = (1,2,3)
my_dict:dict = {'a':1,'b':2}
# 容器类型详细注解
my_list:list[int] = [1,2,3]
my_tuple:tuple[int,str,bool] = (1,'黑马',True)
my_dict:dict[str,int] = {'a':1,'b':2}

# 在注释中进行类型注解
var_4 = random.randint(1,10) # type:int
var_5 = json.loads('{"name":"张三"}') # type:dict[str,str]
def func():
    return 10
var_6 = func() # type:int

# 限制
var_7:int = 'hello' # 不会报错
