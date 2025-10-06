# Встроенные модули
# Не импортируем то чем не пользуемся
# import math as m # приводим через as
# import math as m
#
# print(dir(m))
# from math import pi, e, sqrt
#
# print(f'Число Пи:', m.pi)
# print(f'Применим ceil r Pi:', m.ceil(m.pi))
# print(f'Основание натурального логарифма:', e)
# print(f'Квадратный корень из 225:', sqrt(225))
from random import choices

# ord и chr для работы только с символами
# Узнаём код по символу
# letter = 'r'
# code = ord(letter)
# print(code)
#
# # Узнаём символ по коду
# # « - 171
# # » - 187
# # ⚀ - 9856
# # ⚁ - 9857
# # ⚂ - 9858
# # ⚃ - 9859
# # ⚄ - 9860
# # ⚅ - 9861
# symbol = chr(9861)
# print(symbol)
#
# print(f'Кафе {chr(171)}Аист{chr(187)}')


# print(random.randint(1, 10))
# print(random.randrange(1,10,2))
from random import choice, choices, sample, shuffle
#
# # zars = list(range(9856, 9862)) # диапозон от до
# #
# # print(chr(choice(zars)), chr(choice(zars)))
#
# list = ['Вероятнее всего', 'Наверное', 'Пока не точно', 'Даже не думай',
#         'Хорошие преспективы']
#
# while (question := input('Ваш вопрос: ')) != 'хватит':
#     print(choice(list))
# # if len(list) > 0:
#     print(choices(list, k=3))  # С повторами
#     print(sample(list, k=2))  # Без повторов

# letters = list('qwertyuiopasdfghjklzxcvbnm')
# digits = list('0123456789')
# special = list('@_#$^')
# big_letter = list(map(lambda x: x.upper(), letters)) # Большие буквы делаем

# пароль из 8-ми символов ( маленькие и большие буквы, как минимкм один спец- символ и одна цифра)
def random_password() -> str:
    """
    Возвращает 8-ми значный случайный пароль
    :return: результат состоит из больших,
    маленьких букв, одной цифры и одного спец символа
    """
    letters = list('qwertyuiopasdfghjklzxcvbnm')
    digits = list('0123456789')
    special = list('@_#$^')
    big_letter = list(map(lambda x: x.upper(), letters))  # Большие буквы делаем

    three_letters = choices(letters, k=3) # Выбор 3-х маленьких букв
    three_big_letters = choices(big_letter, k=3) # Выбор 3-х больший букв
    one_digit = choice(digits) # Выбор 1-й случайной цифры
    one_special = choice(special) # Выбор 1-го случайного спец. символа

    # складываем случайныые выборки
    result = three_letters+ three_big_letters+[one_special]+[one_digit]
    #и "замешываем" их
    shuffle(result)

    return ''.join(result) # возвращаем результат в виде строки

print('Пять случайных паролей:')
for _ in range(5):
    print('\t',random_password())