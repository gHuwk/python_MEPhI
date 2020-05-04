import json
from random import randint, choice


def read_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        return json.load(file)


def boolean_choice(json_data, field, template):
    results = {template: 0, 'other': 0}
    for item in json_data:
        value = item[field]
        if template in value:
            results[template] += 1
        else:
            results['other'] += 1
    print(results.items(), sep='\n')

def different_choice(json_data, field):
    results = {}
    for item in json_data:
        value = item[field]
        results[value] = results[value] + 1 if value in results.keys() else 1

    for i in results.items():
        print(i)


def count_recipes(json_data):
    results = {'отпускается по рецепту': 0, 'отпускается без рецепта': 0}
    template = 'без рецепта'
    for item in json_data:
        value = item['Условия отпуска']
        if template in value:
            results['отпускается без рецепта'] += 1
        else:
            results['отпускается по рецепту'] += 1
    print(results.items(), sep='\n')
    return


def create_json_data():
    surnames = ['Агапова', 'Афиногенова', 'Белалова', 'Беспалов', 'Трехглавов']
    data = []
    children_ages = [i for i in range(10)]
    total_children = [i for i in range(5)]
    for i in range(1000):
        surname = choice(surnames)
        sex = 'М' if surname[-1] == 'в' else 'Ж'
        age = randint(18, 60)
        weght = randint(40, 140)
        children = {}
        count_children = choice(total_children)
        for i in range(0,count_children):
            child_age = choice(children_ages)
            children[f'child_{i}_age'] =  child_age
        data.append({
            'surname': surname,
            'sex': sex,
            'age': age,
            'weight': weght,
            'children': children
        })
    return data

def save_json(file_path, data):
    # new_data = []
    # for item in data:
    #     new_data.append(
    #         {
    #             "title": item[1],
    #             "url": item[0]
    #         }
    #     )

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return file_path


def start():
    action = 'read'
    if action == 'read':
        file_path = 'data.json'
        json_data = read_json(file_path)
        count_recipes(json_data)
        # boolean_choice(json_data, 'Условия отпуска', 'без рецепта')
        # different_choice(json_data, 'Лекарственная форма')
        #print(f"Собраны и сохранены последние новости по пути: {file_path}")
    else:
        data = create_json_data()
        output_filename = save_json('output.json', data)
        print(f"Собраны и сохранены последние новости по пути: {output_filename}")

if __name__ == "__main__":
    start()
