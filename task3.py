import math

# Для нахождения конечных нулей факториала воспользуемся функцией из теории чисел
# Источник: https://brilliant.org/wiki/trailing-number-of-zeros/

def zeros(n):
    tailing_zeros = 0
    temp_five = 5

    if n > 0:
        k = math.floor(math.log(n, 5)) # кол-во итераций цикла
    else:
        return 0

    for i in range (1, k + 1):
        tailing_zeros += math.floor(n / temp_five)
        temp_five *= 5
    return tailing_zeros

assert zeros(0) == 0
assert zeros(1) == 0
assert zeros(2) == 0
assert zeros(3) == 0
assert zeros(4) == 0
assert zeros(6) == 1
assert zeros(30) == 7
assert zeros(60) == 14
