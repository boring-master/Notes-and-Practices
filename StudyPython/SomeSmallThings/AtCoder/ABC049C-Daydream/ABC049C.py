S = input().strip()
words = ['dream','dreamer','erase','eraser']
i = len(S)-1
while i >= 0:
    match = False
    for word in words:
        if i - len(word) + 1 >= 0 and S[i-len(word)+1:i+1] == word:
            i -= len(word)
            match = True
            break
    if not match:
        print('NO')
        break
else:
    print('YES')