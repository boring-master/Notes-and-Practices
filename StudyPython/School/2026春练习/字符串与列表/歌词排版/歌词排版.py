def songs_format(songs):
    """
    参数songs : 只包含汉字与空格的字符串
    Returns 歌词列表，包含排版好的歌词
    -------
    """
    ##############begin###########
    # 1 去掉songs中的首尾空格
    songs.strip()
    # 2 将字符串转换成列表保存在 songsList变量中
    # 提示：可用字符串的split函数
    songsList = songs.split(' ')
    # 3将歌曲列表中多余的空格去掉
    i = 0
    while i < len(songsList):
        if songsList[i] == '':
            songsList.remove('')
        else:
            i += 1
    # 4 以上面的字符串列表为基础，找出最长的那一个字符串，以它为长度基准，其它字符串居中对齐左补中文句号。
    # 对齐公式：(最长行的长度-当前行的长度)//2为左补句号数
    mlen = max(len(song) for song in songsList)
    tempList = []
    for song in songsList:
        nsong = '。'*((mlen-len(song))//2)+song
        tempList.append(nsong)
    songsList = tempList
    # 5返回歌曲列表
    return songsList
##############end##########

# 主程序完成函数调用
title = input()  # 歌曲标题
songs = input()  # 歌曲歌词，仅包含逗号和中文
songslst = songs_format(songs)  # 函数调用歌词排版函数
# 6将歌曲标题title加入歌曲首行,输出整首歌曲
######begin########
print(title)
for song in songslst:
    print(song)
#######ends########