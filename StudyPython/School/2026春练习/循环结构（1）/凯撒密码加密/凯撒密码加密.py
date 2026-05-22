
#凯撒密码加密
plaincode= input("")  #输入明文
result = ''
for i in plaincode:
    a = ord(i)
    if 'A' <= i <= 'Z':
        a += 3
        if a > 90:
            a -= 26
        result += chr(a)
    elif 'a' <= i <= 'z':
        a += 3
        if a > 122:
            a -= 26
        result += chr(a)
    else:
        result += i
print(result)