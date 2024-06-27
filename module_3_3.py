def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
#
# print_params()
# print_params(b = 25)
# print_params(c = [1,2,3])

values_list = ["June", 27, True]
values_dict = {"a": 26, 'b': "May", "c": False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

def append_to_list(*item, list_my=None):
    if list_my is None:
        list_my = []
        list_my.append(item)
        print(list_my)


append_to_list(2,3,4)
append_to_list(2)