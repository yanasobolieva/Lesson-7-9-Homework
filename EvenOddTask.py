def evenodd_1(some_list):
    temp_list = []
    if len(some_list) % 2 == 0:
        temp_list = [x for x in some_list if x % 2 == 0]
    else:
        temp_list = [x for x in some_list if x % 2 != 0]
    return temp_list


assert evenodd_1([3, 7, 12]) == [3, 7]
assert evenodd_1([3, 7, 12, 7]) == [12]

print(evenodd_1([3, 7, 12]) == [3, 7])
print(evenodd_1([3, 7, 12, 7]) == [12])
