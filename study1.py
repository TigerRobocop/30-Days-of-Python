# def parse_lists(list):
#     str_items = []
#     num_items = []

#     for i  in list:
#         if isinstance(i, float) or isinstance(i, int):
#             num_items.append(i)
#         elif isinstance(i, str):
#             str_items.append(i)
#         else:
#             pass
    
#     return str_items, num_items

def parse_lists(list):
    str_items = []
    num_items = []
    for item in list:
        if isinstance(item, float) or isinstance(item, int):
            num_items.append(item)
        elif isinstance(item, str):
            str_items.append(item)
        else:
            pass
    return str_items, num_items


items = ["mike", "phone", 321.32, 32332.44, "justin", "Bag", "Cliff Bars", 123]

str_items = []
num_items = []

for i  in items:
    if isinstance(i, float) or isinstance(i, int):
        num_items.append(i)
    elif isinstance(i, str):
        str_items.append(i)
    else:
        pass


print(str_items)
print(num_items)

def parse_lists(list):
    str_items = []
    num_items = []

    for i  in list:
        if isinstance(i, float) or isinstance(i, int):
            num_items.append(i)
        elif isinstance(i, str):
            str_items.append(i)
        else:
            pass
    
    return str_items, num_items


print(parse_lists(items))

def my_sum(items):
    total = 0
    for i in items:
        if isinstance(i, float) or isinstance(i, int):
            total += i
    return total

def my_avg(list):
    sum_items = my_sum(list)
    ct_items = count_items(list)
    return sum_items / (ct_items * 1.0)

def count_items(list):
    total = 0
    for i in items:
        if isinstance(i, float) or isinstance(i, int):
            total += 1
    return total

import datetime

today = datetime.date.today()