#Определить все языки публикаций и количество публикаций на каждом языке.
#Сохранить график в формате png

"""
Данная функция выводит все элементы xml
"""
import xml.etree.cElementTree as ET
import requests
import matplotlib.pyplot as plt
import numpy as np

def read_xml(xml_file):
    with open(xml_file, 'r', encoding='UTF-8') as file:
        tree = ET.parse(file)
        return tree

def xml_processing(xml_tree):
    # Итерация по определенное элементу
    langs = {}
    for lang in xml_tree.iter('LANG'):
        low_lang = lang.text.lower()
        if low_lang in langs:
            langs[low_lang] += 1
        else:
            langs[low_lang] = 1
    return langs

def translate_stats(languages):
    var_lang = {"eng" : "Английский",
                "chi" : "Китайский",
                "por" : "Португальский",
                "spa" : "Испанский",
                "rus" : "Русский",
                "fre" : "Французский",
                "rum" : "Румынский",
                "jpn" : "Японский",
                "hun" : "Венгерский",
                "dan" : "Датский",
                "ger" : "Немецкий"
                }
    new_dict = {}
    for language in languages:
        for lang in var_lang:
            if lang == language:
                new_dict[var_lang[lang]] = languages[lang]
    return new_dict
    
def show_pie(langs):
    fig, ax = plt.subplots(figsize=(6, 4), subplot_kw=dict(aspect="equal"))

    data = [int(langs[data]) for data in langs]
    languages = [data for data in langs]

    def func(pct, allvals):
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

    ax.legend(wedges, languages,
                title="Языки",
                loc="center left",
                bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=12, weight="bold")
    ax.set_title("Распространение языков в публикациях")
    
    file_name = 'languages.png'
    plt.savefig(file_name)
    plt.show()

def show_stats(langs):
    data = [int(langs[data]) for data in langs]
    languages = [data for data in langs]
    print("Языки и их публикации:")
    for i in range(len(data)):
        print("\t{} = {}".format(languages[i], data[i]))

def start():
    xml_file = 'data.xml'
    xml_tree = read_xml(xml_file)
    langs = xml_processing(xml_tree)
    langs = translate_stats(langs)
    show_stats(langs)
    show_pie(langs)

if __name__ == "__main__":
    start()
