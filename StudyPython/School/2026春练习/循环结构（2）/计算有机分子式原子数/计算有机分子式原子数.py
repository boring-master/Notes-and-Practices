b = input()
n = len(b)
count=0
for i in range(n):
    if i+1 < n and b[i + 1].islower():
        continue
    elif b[i].isdigit():
        continue
    if b[i] in 'CHNO':
        if i+1<n and b[i+1].isdigit():
            count += int(b[i+1])
        else:
            count += 1
print(count)