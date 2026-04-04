class Phone:
    IMEI = None
    producer = 'IT'
    def call_by_5g(self):
        print('5g通话')
class myphone(Phone):
    producer = 'HM'
    def call_by_5g(self):
        print('开启CPU单核模式')
        # 方式一
        # print(f'父类的厂商是：{Phone.producer}')
        # Phone.call_by_5g(self)
        # 方式二
        print(f'父类的厂商是：{super().producer}')
        super().call_by_5g()
        print('关闭CPU单核模式')
phone = myphone()
phone.call_by_5g()
print(phone.producer)

