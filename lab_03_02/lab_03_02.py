import csv
import openpyxl as XSL
from itertools import islice

def get_filename():
    filename = input("Input filename: ")
    return filename

def csv_read(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = [row for row in reader]
        return data

# Определить самую высокооплачиваемую должность (максимальная средняя зарплата)
def max_average_salary(data):
    # Использовал тот же абстрактный способ.
    posts = {}
    # Распаковка
    for container in islice(data, 1, len(data), 1):
        #posts[container[6]] = container[7]
        if container[6] in posts:
            posts[container[6]][0] += int(container[7])
            posts[container[6]][1] += 1
        else:
            posts[container[6]] = [int(container[7]), 1]
    # Простое нахождение среднего и замена dict aka posts
    for post in posts:
        posts[post] = float(posts[post][0]) / posts[post][1]
    # Нахождение greatest - лучшей заработной платы по ключу.
    # По факту можно было использовать нахождение по ключу-значению. Но так быстрее.
    greatest = ""
    max_salary = -1
    for post in posts:
        if greatest == "":
            greatest = post
            max_salary = posts[post]
        else:
            if max_salary < posts[post]:
                greatest = post
                max_salary = posts[post]
    return greatest, max_salary

# Записывает исходные данные в формат xlsx
def xlsx_write(data):
    filename = "Agapov.xlsx"
    # Инициализируем
    book = XSL.Workbook()
    # Добавляем лист с именем Data
    data_sheet = book.create_sheet('Data')
    data_sheet.append(data[0])
    # Так как некоторые поля - числа, то переводим в int
    for container in islice(data, 1, len(data), 1):
        container[3] = int(container[3])
        container[4] = int(container[4])
        container[7] = int(container[7])
        data_sheet.append(container)
    # Сохраняем с необходимым названием.
    book.save(filename)

def main():
    path_csv = get_filename()
    data = csv_read(path_csv)
    greatest, max_salary = max_average_salary(data)
    print("Cамая высокооплачиваемая должность:")
    print("\t{} - {}".format(greatest, max_salary))
    print("Создание .xlsx формата...")
    xlsx_write(data)
    print("Завершено. Файл 'Agapov.xlsx' добавлен.")

if __name__ == '__main__':
    main()