import xml.etree.cElementTree as ET
import requests

def url_request(url, url_type):
    response = requests.get(url)
    if url_type == 'xml':
        print(response.text)
    elif url_type == 'json':
        print(response.json())


"""
Данная функция выводит все элементы xml
"""
def show(xml_tree):
    root = xml_tree.getroot()
    for child in root:
        for tag in child:
            print(tag.tag, tag.text, sep='-->')
        print()


def xml_processing(xml_tree):
    # show(xml_tree)
    # Итерация по определенное элементу
    countries = {}
    for country in xml_tree.iter('LANG'):
        if country.text in countries:
            countries[country.text] += 1
        else:
            countries[country.text] = 1
    print(countries)

    # Получение записи по индексу
    root = xml_tree.getroot()
    print(root[0][0].text)

    #Использование xpath
    countries = xml_tree.findall('LANG')
    countries_xpath = xml_tree.findall('.//LANG')
    print(len(countries), len(countries_xpath))



def read_xml(xml_file):
    with open(xml_file, 'r', encoding='UTF-8') as file:
        tree = ET.parse(file)
        return tree


def create_xml_data():
    return []

def save_xml(file_path, data):
    pass


def start():
    action = 'read'
    if action == 'read':
        xml_file = 'data.xml'
        xml_tree = read_xml(xml_file)
        xml_processing(xml_tree)
    elif action == 'url':
        xml_url = 'http://ip-api.com/xml/24.48.0.1'
        url_request(xml_url, 'xml')
        json_url = 'http://ip-api.com/json/24.48.0.1'
        url_request(json_url, 'json')


if __name__ == "__main__":
    start()
