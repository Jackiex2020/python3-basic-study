import pickle
data_dict = {"name": "xxx", "gender": "female"}
data_dumps = pickle.dumps(data_dict)
# <class 'bytes'>
print(type(data_dumps))
data_loads = pickle.loads(data_dumps)
# <class 'dict'>
print(type(data_loads))


# f = open('xxx.txt', 'wb')
# pickle.dump(data_dict, f)
# data = pickle.load('xxx.txt')
# f.close()