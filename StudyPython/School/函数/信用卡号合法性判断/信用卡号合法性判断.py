# 信用卡的验证程序
def validCreditCard(card_number):
    """
    验证8位信用卡号码是否合法
    参数:card_number (str): 8位信用卡号码字符串
    返回:bool: 如果卡号合法返回True，否则返回False
    """
    # 请在下面编写代码
    # ********** Begin ********** #
    lst = [int(i) for i in card_number]
    fir = 0
    sec = 0
    for num in range(7,0,-2):
        fir += lst[num]
    for num in range(-2,-9,-2):
        if lst[num] * 2 > 9:
            sec += (lst[num] * 2 // 10 + lst[num] * 2 % 10)
        else:
            sec += lst[num] * 2
    if (fir + sec) % 10 == 0:
        return True
    else:
        return False
    # ********** End ********** #

# 请不要修改下面的代码
# 主程序
while True:
    card_number = input()  # 从键盘输入
    card_number = card_number.strip()  # 去掉首尾空格
    # 输入"q"或"Q"结束循环
    if card_number == "q" or card_number == "Q":
        break
    # 检查输入字符串长度是否为8或是否含有非数字字符
    elif len(card_number) != 8 or not card_number.isdigit():
        print("input error,again!")
        continue
    else:
        print(validCreditCard(card_number))  # 函数调用输出结果

