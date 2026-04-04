def print_file_info(file_name):
    '''
    将给定路径的文件内容输出到控制台中
    :param file_name:即将读取的文件路径
    :return:None
    '''
    f = None
    try:
        f = open(file_name,'r',encoding='utf-8')
        content = f.read()
        print('文件的全部内容如下：')
        print(content)
    except Exception as e:
        print(f'程序出现异常了，原因是：{e}')
    finally:
        if f:        # 如果变量是None，表示False，如果有任何内容，就是True
            f.close()
# if __name__ == '__main__':
#     print_file_info('D:/bill.txt')
'''bill.txt
name,date,money,type,remarks
总经理，2022-01-01，100000，消费，正式
总经理，2022-01-02，300000，收入，正式
总经理，2022-01-03，100000，消费，测试
辣椒酱，2022-01-01，300000，收入，正式
辣椒酱，2022-01-02，100000，消费，测试
辣椒酱，2022-01-03，100000，消费，正式
辣椒酱，2022-01-04，100000，消费，测试
辣椒酱，2022-01-05，500000，收入，正式
中西医，2022-01-01，100000，消费，正式
中西医，2022-01-02，500000，收入，正式
中西医，2022-01-03，900000，收入，测试
网络化，2022-01-01，500000，消费，正式
网络化，2022-01-02，300000，消费，测试
网络化，2022-01-03，900000，收入，正式
领导好，2022-01-01，300000，消费，测试
领导好，2022-01-02，100000，消费，正式
领导好，2022-01-03，300000，消费，正式
'''
def append_to_file(file_name,data):
    '''
    将指定的数据追加到指定的文件中
    :param file_name:指定的文件路径
    :param data:指定的数据
    :return:None
    '''
    f = open(file_name,'a',encoding='utf-8')
    f.write(data)
    f.write('\n')
if __name__ == '__main__':
    append_to_file('D:/test_append.txt','黑马程序员')