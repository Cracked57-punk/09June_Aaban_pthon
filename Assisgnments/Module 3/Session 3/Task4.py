"""
my_list = [1, 2, 3]
print(my_list[5])
my_dict = {'a': 1}
print(my_dict['b'])

Fix code.
"""
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index out of range.")
try :
    my_dict = {'a': 1}
    print(my_dict['b'])
except KeyError:
    print("Key not found.")