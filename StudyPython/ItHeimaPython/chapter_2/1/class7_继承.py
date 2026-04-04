# class Phone:
#     IMEI = None
#     producer = 'HM'
#     def call_by_4g(self):
#         print('4g通话')
# class Phone2022(Phone):
#     face_id = '10001'
#     def call_by_5g(self):
#         print('2022新功能：5g通话')
# phone = Phone2022()
# print(phone.producer)
# phone.call_by_5g()
# phone.call_by_4g()

class Phone:
    IMEI = None
    producer = 'IT'
    def call_by_4g(self):
        print('4g通话')
class NFCreader:
    nfc_type = '第五代'
    producer = 'HM'
    def read_card(self):
        print('NFC读卡')
    def write_card(self):
        print('NFC写卡')
class myphone(Phone, NFCreader):
    pass
phone = myphone()
phone.call_by_4g()
phone.read_card()
print(phone.producer)

