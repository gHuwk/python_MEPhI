import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import pymorphy2

# Страшный грех - глобальная переменная
morph = pymorphy2.MorphAnalyzer()

def get_filename():
    filename = input("Input filename: ")
    return filename

# Работает? Не трогай.
def unicode2str(string):
    try:
        return string.replace(u'\u2014', u'-').replace(u'\u2013', u'-').replace(u'\u2026', u'...').replace(u'\xab', u"'").replace(u'\xbb', u"'")
    except:
        return string

def to_ascii(string):
    try:
        string = string.replace("'", '').replace(" - ", '').replace("|", '')
        return string.decode('utf-8').encode("ascii", errors="ignore").decode()
    except:
        return ''

def is_asciiword(string):
    ascii_word = to_ascii(string)
    return len(ascii_word) > 2

# Pymorphy2
def normal_rus(w):
    res = morph.parse(w)
    for r in res:
        if 'NOUN' in r.tag:
            return r.normal_form
    return None

# Не нужно
def normal_eng(s):
    for sym in ("'s", '{', '}', "'", '"', '}', ';', '.', ',', '[', ']', '(', ')', '-', '/', '\\'):
        s = s.replace(sym, ' ')
    return s.lower().strip()

# Создает cчетчик слов из файла для дальнейшей работы. Аналог dict.
def create_Counter(filename):
    # Счетчик
    c_dict = Counter()
    file = open(filename, 'r')
    
    for line in file:
        sequence_list = clean_line(line).split()
        for word in sequence_list:
            if is_asciiword(word):
                normal = normal_eng(word)
                c_dict[normal] += 1
            else:
                normal = normal_rus(word)
                if normal is not None:
                    if exception_check(word):
                        c_dict[normal] += 1
                    else:
                        c_dict[word] += 1
    file.close()
    return c_dict

# Исключения, которые могут быть
def exception_check(word):
    exception = {"до", "из", "к", "на", "по", "от", "у", "за", "об", "ж", "ш-ш-ш", "и", "с", "в", "о", "а", "б", "я"}
    if word in exception:
        return False
    return True

# Чистит line, если все очень плохо и там какие-то запрещенные символы
def clean_line(line):
    line = unicode2str(line).lower()

    array = " абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz-"
    for i in line:
        if i not in array:
            # Можно было использовать срезы и писать свой replace. Но зачем?
            line = line.replace(i, ' ')
    line = line.strip()
    return line

def show_wordcloud(counter_obj):
    # Количество имеющихся
    total_count = len(counter_obj)
    # Самые встречаемые
    common = counter_obj.most_common(total_count)

    wc = WordCloud(width=2600, height=2200, background_color="white", relative_scaling=0.5,
                   collocations=False, min_font_size=10).generate_from_frequencies(dict(common))
    
    plt.axis("off")
    plt.figure(figsize=(9, 6))

    plt.imshow(wc, interpolation="bilinear")

    plt.title("Слова в тексте")
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()
    # Сохранение
    file_name = 'tag_cloud.png'
    plt.savefig(file_name)
    plt.show()

def main():
    input_file = get_filename()
    data = create_Counter(input_file)
    print(data)
    show_wordcloud(data)

if __name__ == '__main__':
    main()