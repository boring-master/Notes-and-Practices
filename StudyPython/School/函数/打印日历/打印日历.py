def day(y, m, d):  # 计算y年m月d日是星期几
    # 请在下面编写代码
    # ********** Begin ********** #
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14-m) // 12) - 2
    d0 = (d + x + (31 * m0) // 12) % 7
    # ********** End ********** #
    # 请不要修改下面的代码
    return d0

def isLeapYear(year):  # 判断year年是否闰年
    # 请在下面编写代码
    # ********** Begin ********** #
    # ********** End ********** #
    # 请不要修改下面的代码
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calendar(y, m):  # 打印y年m月日历
    print('       {}年{}月'.format(y, m))
    print('Su\tM\tTu\tW\tTh\tF\tSa')
    # 请在下面编写代码调用函数计算y年m月1日是星期几保存在变量date中
    # ********** Begin ********** #
    date = day(y, m, 1)
    # ********** End ********** #
    days = 0  # 初始化y年m月的天数为0
    # 请在下面编写代码计算y年m月的天数
    # ********** Begin ********** #
    if m == 2:
        if isLeapYear(y):
            days = 29
        else:
            days = 28
    elif m in (1 , 3 , 5 , 7 , 8 , 10 , 12):
        days = 31
    else:
        days = 30
    # ********** End ********** #
    count = date  # y年m月1日是星期几
    for i in range(date):
        print('\t', end='')
    for d in range(1, days + 1):
        print(str(d) + '\t', end="")
        count = (count + 1) % 7
        if count == 0:
            print()
    print()
    # 请不要修改下面的代码
print('-' * 27)
for (y, m) in [(2017, 8), (2017, 10), (2015, 8), (2017, 2), (2016, 2)]:
    calendar(y, m)
    print('-' * 27)
