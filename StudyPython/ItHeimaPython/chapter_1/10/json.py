# import json
# data = [{'name':'早点睡','age':11},{'name':'我的车','age':13},{'name':'真心话','age':16}]
# json_str = json.dumps(data,ensure_ascii=False)
# print(type(json_str))
# print(json_str)

# import json
# d = {'name':'总经理','addr':'台北'}
# json_str = json.dumps(d,ensure_ascii=False)
# print(type(json_str))
# print(json_str)

# import json
# json_str = '[{"name":"早点睡","age":11},{"name":"我的车","age":13},{"name":"真心话","age":16}]'
# li = json.loads(json_str)
# print(type(li))
# print(li)

import json
s = '{"name":"总经理","addr":"台北"}'
d = json.loads(s)
print(type(d))
print(d)

