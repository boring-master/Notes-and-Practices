# 数字翻译成英文程序
def unit_to_word(u):  # 将0～9的数字转换成英文，并返回转换后的英文
# 请在下面编写代码
# ********** Begin ********** #
    units = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }
    return units[u]
# ********** End ********** #
# 请不要修改下面的代码
# noinspection SpellCheckingInspection
def tens_to_word(t):  # 利用unit_to_word，将10～19、
# 以及20～99的十位部分数字转换成英文，并返回转换后的英文
# 请在下面编写代码
# ********** Begin ********** #
    if 10 <= t <= 19:
        teens = {
            10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
            15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
        }
        return teens[t]
    elif 20 <= t <= 99:
        tens_digit = t // 10
        tens_words = {
            2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
            6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
        }
        return f'{tens_words[tens_digit]} {unit_to_word(t%10)}'
    else:
        return unit_to_word(t)

# ********** End ********** #
# 请不要修改下面的代码

# noinspection SpellCheckingInspection
def hundreds_to_word(h):  # 利用unit_to_word、tens_to_word进行转换，并返回转换后结果的函数
# 请在下面编写代码
# ********** Begin ********** #
    bai = h //100
    shige = h % 100
    if bai == 0:
        return tens_to_word(shige)
    else:
        nbai = unit_to_word(bai) + ' hundred'
        nshige = tens_to_word(shige)
        return f'{nbai} and {nshige}'
# ********** End ********** #
# 请不要修改下面的代码
test = eval(input())
print(test, "==>", hundreds_to_word(test))

