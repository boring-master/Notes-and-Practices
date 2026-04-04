s=input().split()
if s[1]==0:
    print(0)
else:
    print(int((int(s[0])*int(s[1])-int(s[2]))/int(s[1])))