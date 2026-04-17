# 创建并初始化score_dict字典
score_list=['姓名','语文','英语','数学','体育']
# 请按下面的注释提示添加代码，完成相应功能
#1.根据上面的列表创建score_dict字典并初始化，得到如任务描述中的字典，字典中的值从键盘输入
###### Begin ######
sum = 0
score_dict = dict.fromkeys(score_list,0)
for key in score_dict.keys():
    temp = input()
    if temp.isdigit():
        temp = eval(temp)
        sum += temp
    score_dict[key] = temp
#######  End #######
# 请按下面的注释提示添加代码，完成相应功能
#2.请在此添加代码，计算张三同学的总分，并将总分作为新的键值对加入，最后输出score_dict的所有键值对
###### Begin ######
score_dict['总分'] = sum
for key,value in score_dict.items():
    print(key,value)
#######  End #######
