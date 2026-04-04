# class Phone:
#     __current_voltage = None
#     def __keep_single_core(self):
#         print('让CPU以单核模式运行')
# phone = Phone()
# phone.__keep_single_core()      # 报错
# print(phone.__current_voltage)  # 报错

# class Phone:
#     __current_voltage = 0
#     def __keep_single_core(self):
#         print('让CPU以单核模式运行')
#     def call_by_5g(self):
#         if self.__current_voltage >= 1:
#             print('5g通话已开启')
#         else:
#             self.__keep_single_core()
#             print('电量不足，无法使用5g通话，已设置为单核运行进行省电')
# phone = Phone()
# phone.call_by_5g()

class Phone:
    __is_5g_enable = True
    def __check_5g(self):
        if self.__is_5g_enable:
            print('5g开启')
        else:
            print('5g关闭，使用4g网络')
    def call_by_5g(self):
        self.__check_5g()
        print('正在通话中')
phone = Phone()
phone.call_by_5g()