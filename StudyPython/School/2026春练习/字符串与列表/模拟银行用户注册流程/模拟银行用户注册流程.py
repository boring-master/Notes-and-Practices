def Invalid_Password(password):
    """
    #功能：完成密码有效性判断
    #参数password : 密码字符串
    #Returns  密码有效则返回True,否则 False
    """
    ####begin#####
    if len(password) < 6:
        return False
    if not any(i.islower() for i in password):
        return False
    if not any(i.isupper() for i in password):
        return False
    if not any(i.isdigit() for i in password):
        return False
    if not any(i in set('@！#￥%……&*') for i in password):
        return False
    return True
    #####ends#######


# 主程序调用,认真看懂主程序代码,不要删除
count = 0  # 统计输入次数,初始化为0
Regist_Name = input()  # 请输入用户名
while True:
    Regist_Password1 = input()  # 请输入用户注册密码
    if (Invalid_Password(Regist_Password1) == 1):  # 函数调用判断输入密码是否有效
        Regist_Password2 = input()  # 请确认注册密码
        if Regist_Password1 == Regist_Password2:
            print("注册成功")
            print(f"用户名:{Regist_Name},密码:{Regist_Password1}")
            break
        else:
            print("两次密码不一致,重新输入")
    else:
        print("注册密码格式错误,请重新输入")
    count += 1
    if count == 3:
        print("3次密码输入错误,sorry,注册失败!")
        break


