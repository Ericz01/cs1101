import json

my_dict = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red', 'mango': 'yellow', 'grapes': ['black', 'green']}

s = json.dumps(my_dict)
d = json.loads(s)
print(my_dict)
print(s)
print(d)