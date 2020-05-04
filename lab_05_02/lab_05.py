import json
from random import randint, choice
from collections import OrderedDict

def read_json(json_file):
    #Читка
    with open(json_file, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def print_list_max(list_max):
    
    if len(list_max) == 1:
        print("Препарат, который хранится дольше остальных:")
    else:
        print("Препараты, которые хранится дольше остальных:")
    for item, time in list_max:
        time = time / 48
        print("Название: " + item + "\tСрок хранения: " + str(time) + "лет")
        
def get_dates(json_data, field):
    results = {}
    for item in json_data:
        value = item[field]
        name = item['Торговое наименование лекарственного препарата']
        if value != "":
            results[name] = convert_date(value)
    return results

def print_ignored(results):
    print("IGNORED")
    for item in results:
        if results[item] is None:
            print(item + " NONE")
        if results[item] == 0:
            print(item + " 0")
            
def get_maximal_dates(numbers):
    mx_tuple = max(numbers.items(),key = lambda x:x[1]) #max function will return a (key,value) tuple of the maximum value from the dictionary
    max_list =[i for i in numbers.items() if i[1]==mx_tuple[1]] #my_tuple[1] indicates maximum dictionary items value
    if len(max_list) > 3:
        max_list = max_list[:3]
    
    return max_list
    
def convert_date(string):
    # Парсит и конвертирует в месяцы
    string = string.lower()
    string = ' '.join(string.split())
    #print(string)
    year = ["года", "лет", "г"]
    mounth = ["месяца", "месяцев", "мес", "м"]
    week = ["недель", "нед", "недели", "н"]
    spl = [',',';','/','\\','-']
    numeric = {"одиннадцать": "11",
               "один": "1",
               "одна": "1",
               "два": "2",
               "две": "2",
               "три": "3",
               "четыре": "4",
               "пять": "5",
               "шесть": "6",
               "восемь": "8",
               "семь": "7",
               "девять": "9",
               "десять": "10",
               "двеннацать": "12"}
    # Особые моменты
    string = string.replace("1,5 года", "18 месяцев").replace("полтора года", "18 месяцев")
    string = string.replace("1.5 года", "18 месяцев").replace("полгода", "6 месяцев")
    string = string.replace("2.5 года", "30 месяцев").replace("3.5 года", "42 месяца")
    string = string.replace("3,5 года", "42 месяца").replace("2,5 года", "30 месяцев")
    # Болото. Работает - не трогай
    for item in spl:
        string = string.replace(item, '')
    string = string.split()
    
    for i in range(len(string)):
        if string[i][-1] == '.':
            string[i] = string[i][:-1]
        if string[i][0] == '.':
            string[i] = string[i][1:]
    for i in range(len(string)):
        if string[i] in numeric:
            string[i] = numeric[string[i]]        
    weeks = 0
    index = 0
    trig_y = True
    trig_m = True
    trig_w = True
    # Оптимизировать
    for cell in string:
        if trig_y:
            if cell in year:
                
                if string[index - 1].isdigit():
                    weeks += int(string[index - 1]) * 12 * 4
                else:
                    weeks = 0
                    break
                trig_y = False
            elif cell == "год":
                weeks += 12 * 4
                trig_y = False
        index += 1
    index = 0
    if not trig_y:
        return weeks
    for cell in string:
        if trig_m: 
            if cell in mounth:
                if string[index - 1].isdigit():
                    weeks += int(string[index - 1]) * 4 
                else:
                    weeks = 0
                    break
                trig_m = False
            elif cell == "месяц":
                weeks += 4
                trig_m = False
        index += 1
    index = 0
    if not trig_m:
        return weeks
    for cell in string: 
        if trig_w:
            if cell in week:
                if string[index - 1].isdigit():
                    weeks += int(string[index - 1]) 
                else:
                    weeks = 0
                    break
                trig_w = False
            elif cell == "неделя":
                weeks += 1
                trig_w = False
        index += 1
    return weeks

def start():
    file_path = 'data.json'
    json_data = read_json(file_path)
    results = get_dates(json_data, 'Срок годности')
    #print_ignored(results) # Данные с ошибками в тексте.
    list_max = get_maximal_dates(results)
    print_list_max(list_max)
    
if __name__ == "__main__":
    start()
