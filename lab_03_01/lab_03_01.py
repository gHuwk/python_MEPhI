# Чисто для отладки
def simple_read(filename):
    file = open(filename, 'r')

    print("Filename: ", file.name)
    print("MODE: ", file.mode)

    counter = 0
    for line in file:
        if counter < 5:
            print(line, end = ' ')
            counter += 1
        else:
            answer = input("Do you want to continue? Y/N: ")
            if answer == 'Y':
                counter = 0
            else:
                break
    print("Reading is over")
    file.close()

def get_filename():
    filename = input("Input filename: ")
    return filename

# Число слов с гласной и согласной
def count_of_words(dict):
    vowels = 0
    consonants = 0
    all_w = 0
    for key in dict:
        if key[0] in "аоэиуыеёюяaeiouyАОЭИУЕЁЮЯAEIOUY":
            vowels += dict[key]
        else:
            consonants += dict[key]
        # vowels + comsonants. Для лишней проверки
        all_w += dict[key]

    print("\nЧисло гласных: {}\nЧисло согласных: {}\nОбщее число слов: {}".format(vowels, consonants, all_w))
    return vowels, consonants

# Создает словарь слов из файла для дальнейшей работы
def create_dictionary(filename):
    # Словарь
    dict = {}
    file = open(filename, 'r')
    
    for line in file:
        line = clean_line(line)
        sequence_list = line.split()
        for word in sequence_list:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
    file.close()
    return dict

# Чистит line, если все очень плохо и там какаие-то запрещенные символы
def clean_line(line):
    # Тут можно было искать соотвтествие ASCII кодовой таблице посредству вычислений, но зачем?
    array = " абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz-АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЧЦШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in line:
        if i not in array:
            # Можно было использовать срезы и писать свой replace. Но зачем?
            line = line.replace(i, ' ')
    line = " ".join(line.strip().split())
    #print(line)
    return line

def print_dictionary_to_file(dict):
    file = open("./output.txt", 'w')

    for key in dict:
        string = str(key) + ' - ' + str(dict[key]) + '\n'
        file.write(string)
    
    file.close()

def main():
    dictionary = create_dictionary(get_filename())
    #dictionary = create_dictionary("./current.txt")
    count_of_words(dictionary)
    print_dictionary_to_file(dictionary)

if __name__ == '__main__':
    main()