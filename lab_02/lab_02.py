# Решение влоб
from random import randint
from math import sin, log, factorial

def main():
    print("Введите int k > 0:")
    k = int(input())
    if k > 0:
        x = x_from(k)
        print("X = ", x)
        ret_z = z(x, k)
        print("№{} из последовательности: {}".format(k, ret_z))
        print("Сумма первых {} членов:".format(k))
        print()
        # Решение влоб
        print("Медленный способ:", stupid_summa(x, k))
        print()
        # Решение через модификацию рекурентного соотношенияы
        print("Умный способ:", clever_summa(x, k))
        table(z, x, k)
    else:
        print("Некорректный k")

def z(x, k):
    d = 2 * k + 1
    p = x * k
    sign = ((-1) ** k)
    return (sign * (x ** d) * sin(p))/(factorial(k) * d)

def x_from(k):
    # В задании укаана функция randint. Принимат на вход int, int. Вззял round
    return randint(round(log(k + 1)), 2 * k)

def stupid_summa(x, k):
    # Решение итеративно складывая
    summa = 0
    i = 1
    while(i <= k):
        summa += z(x, i)
        print(z(x, i))
        i += 1
    return summa

def factor_from(x, n):
    return ((-1) * (x ** 2) * ((2 * n + 1) * sin(n * x + x)))/(((2*n + 3) * sin(n * x)) * n + 1)

def clever_summa(x, k):
    cache = z(x, 1)
    summa = 0
    factor = factor_from(x, k)
    i = 1
    while (i <= k):
        summa += cache
        cache *= factor
        print(cache)
        i += 1
    return summa

def table(func, x, k):
    i = 1
    while (i <= k):
        print("{}   {}".format(i, func(x, i)))
        i += 1
main()

