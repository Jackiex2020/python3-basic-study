import json
data_dict = {"name": "xxx", "gender": "female"}

print(type(data_dict))  # <class 'dict'>
print(data_dict)

data_str = json.dumps(data_dict)
print(type(data_str))  # <class 'str'>
print(data_str)

data_dict_1 = json.loads(data_str)
print(type(data_dict_1))  # <class 'dict'>