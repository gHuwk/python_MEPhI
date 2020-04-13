def main():
    print("Введите строки (окончание ввода - пустая строка):")
    array_strings = get_data()
    print_answer(find_largest(array_strings),
                 find_shortest(array_strings))

def print_answer(longest, shortest):
    if longest:
        print('Самая длинная числовая строка: "{}", сумма цифр = {}'.format(longest, get_sum(longest)))
    else:
        print('Числовых строк нет.')
    if shortest:
        print('Самая короткая строка с заданным условием: "{}"'.format(shortest))
    else:
        print('Самой короткой строки с заданным условием нет.')
    
def get_data():
    array_strings = []
    while True:
        cache = input()
        if cache:
            array_strings.append(cache)
        else:
            break
    return array_strings

def find_shortest(array_strings):
    largest_lence = get_max_lence(array_strings)
    shortest = ""
    for word in array_strings:
        if not word.isdigit() and not word.isalpha():
            current = get_count_nums(word)
            if current < largest_lence and 2 * current < len(word):
                shortest = word 
    return shortest

def find_largest(array_strings):
    largest = ""
    for word in array_strings:
        if word.isdigit() and len(word) > len(largest):
            largest = word
    return largest
   

def get_sum(string_only_nums):
    summa = 0
    for i in string_only_nums:
        summa += int(i)
    return summa

def get_max_lence(array_strings):
    max = 0
    for word in array_strings:
        if max < len(word):
            max = len(word)
    return max

def get_count_nums(string):
    count = 0
    for char in string:
        if '0' <= char <= '9':
            count += 1
    return count

main()