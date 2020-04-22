import openpyxl
import matplotlib.pyplot as plt

def get_filename():
    filename = input("Input filename: ")
    return filename

def get_data_salary(filename):
    # Создадим контейнер
    posts = {}
    # Откроем файл
    source_book = openpyxl.load_workbook(filename)
    # Data
    sheet = source_book['Data']
    pairs = sheet['G2':'H4495']
    for c1, c2 in pairs:
        if c1.value in posts:
            posts[c1.value][0] += 1
            posts[c1.value][1] += c2.value
        else:
            posts[c1.value] = [1, c2.value]
    return posts

def average_salary(posts):
    for everyone in posts:
        posts[everyone] = posts[everyone][1]/posts[everyone][0]
    return posts

def show_bar(posts):
    # Object Counter не стал использовать, так как по сути тот же словарь
    heights = [posts[item] for item in posts]      #counter_obj.values()
    bars = [item for item in posts]   #counter_obj.keys()
    y_pos = range(len(bars))
    
    # Хотел красивые границы сделать.
    find_max, find_min = round(max(heights)), round(min(heights))
    plt.ylim(find_min - 1000, find_max + 1000)

    # Повороты
    plt.bar(y_pos, heights, align='center', alpha=1)
    plt.xticks(y_pos, bars, rotation=90)
    # Лейблы
    plt.ylabel('Средняя заработная плата')
    plt.title('График зависимости средней зарплаты от должности')

    # Сохраняем
    file_name = 'attitude_to_earnings.png'
    plt.savefig(file_name)
    plt.show()

def main():
    input_file = get_filename()
    average_salary_data = average_salary(get_data_salary(input_file))
    show_bar(average_salary_data)

if __name__ == '__main__':
    main()