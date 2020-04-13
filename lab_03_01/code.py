# Python3 код для демонстрации
# извлечь слова из строки
# используя регулярное выражение (findall ())

import re

  
# инициализирующая строка

test_string = "Geeks-for-geeks,    is best @# Computer Science Portal.!!!"

  
# печать оригинальной строки

print ("The original string is : " +  test_string)

  
# используя регулярное выражение (findall ())
# извлечь слова из строки

res = re.findall(r'\w+', test_string)

  
# результат печати

print ("The list of words is : " +  str(res)) 
