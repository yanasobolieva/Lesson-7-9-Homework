# First approach without using dictionary comprehension
def triples(some_list):
    temp_dict = {}
    for x in some_list:
        if x % 3 == 0:
            temp_dict[x] = True
        else:
            temp_dict[x] = False
    return temp_dict


assert triples([3, 7, 12]) == {3: True, 12: True, 7: False}
assert triples([9, 1, 2, 5, 9, 33]) == {1: False, 2: False, 5: False, 9: True, 33: True}

print(triples([3, 7, 12]) == {3: True, 12: True, 7: False})
print(triples([9, 1, 2, 5, 9, 33]) == {1: False, 2: False, 5: False, 9: True, 33: True})


# Second approach using dictionary comprehension
def triples_1(some_list):
    return {x: x % 3 == 0 for x in some_list}


assert triples_1([3, 7, 12]) == {3: True, 12: True, 7: False}
assert triples_1([9, 1, 2, 5, 9, 33]) == {1: False, 2: False, 5: False, 9: True, 33: True}

print(triples_1([3, 7, 12]) == {3: True, 12: True, 7: False})
print(triples_1([9, 1, 2, 5, 9, 33]) == {1: False, 2: False, 5: False, 9: True, 33: True})
