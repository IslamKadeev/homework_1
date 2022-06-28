from itertools import combinations_with_replacement

def get_list_elements_multiplication(array):
    multiplication = 1
    for element in array:
        multiplication *= element
    return multiplication

def find_count_and_max(primesL, r, limit):
    max = 0
    multiplication = get_list_elements_multiplication(primesL)
    count = 0
    combinations = combinations_with_replacement(primesL, r)
    stop = False

    if multiplication <= limit:
        for combination in combinations:
            if primesL.issubset(combination):
                multiplication = get_list_elements_multiplication(combination)
                if multiplication <= limit:
                    count += 1
                    stop = True
                    if max < multiplication:
                        max = multiplication
        return [count, max, stop]
    else:
        return []


def count_find_num(primesL, limit):
    primesL = set(primesL)
    r = len(primesL)
    temp_result = find_count_and_max(primesL, r, limit)
    
    if temp_result == list():
        return []
    else:
        result = [temp_result[0], temp_result[1]]

    while temp_result[-1]: # find_count_and_max returns bool flag
        r += 1
        temp_result = find_count_and_max(primesL, r, limit)
        result[0] += temp_result[0]
        if result[1] < temp_result[1]:
            result[1] = temp_result[1]

    return result

primesL = [2, 5, 7]
limit = 500
assert count_find_num(primesL, limit) == [5, 490]

primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []



