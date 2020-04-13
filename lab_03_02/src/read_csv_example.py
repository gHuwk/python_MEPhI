import csv
from itertools import islice
import numpy


"""
Функция определяет, в каком городе сколько человек погибло и выжило и их процентное соотношение
"""
def func1(data):
    cities = {}
    for i in islice(data,1,len(data),1):
        city = i[8]
        is_survived = int(i[0])
        if city not in cities:
            cities[city] = [0, 0]
        cities[city][is_survived] += 1

    for city, count in cities.items():
        dead = round(count[0]/sum(count)*100)
        alive = 100 - dead
        print(f'{city}: {count[0]}({dead}%) человек умерло, {count[1]}({alive}%) человек выжило')

"""Функция определяет, сколько человек какого возраста умерло"""
def func2(data):
    ages = {}
    for i in islice(data, 1, len(data), 1):
        is_survived = bool(int(i[0]))
        age = int(float(i[2]))
        if age not in ages:
            ages[age] = 0
        if is_survived:
            ages[age] += 1

    list_keys = list(ages.keys())
    list_keys.sort()
    for age in list_keys:
        print(f'возраст (лет): {age}, умерло(человек): {ages[age]}')


"""Функция определяет средний возраст погибших"""
def func3(data):
    ages = []
    for i in islice(data, 1, len(data), 1):
        is_survived = bool(int(i[0]))
        age = int(float(i[2]))
        if not is_survived:
            ages.append(age)
    summa = 0
    for i in ages:
        summa += i
    mean_age = round(summa/len(ages),1)
    print(mean_age)
    """
    # Также существуют эквивалентые способы записи
    mean_age = round(numpy.mean(ages),1)
    print(mean_age)
    """

def csv_read(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = [row for row in reader]
        return data

def main():
    path_csv = 'example.csv'
    data = csv_read(path_csv)
    func1(data)
    func2(data)
    func3(data)


if __name__ == '__main__':
    main()

