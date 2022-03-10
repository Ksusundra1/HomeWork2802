# Задание 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Если перевод сделать невозможно, вернуть None.
numbers = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
} # Создали словарь

def numbers_translate(num_2): # Функция: если введенное числительное является лючем в словаре,
    if num in numbers:
        return numbers.get(num_2) # то возвращаем значение по данному ключу
    else:
        return 'None' # Если числительного нет в словаре в виде ключа - выводим None


num = input('Напишите числительное от 0 до 10: ')

print(numbers_translate(num))

# Задание 2. Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.


numbers = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def numbers_translate(num_2):
    num3 = num_2.lower() # Создаем переменную в нижнем регистре
    if num3 in numbers:
        if num_2[0].isupper(): # Проверяем первую букву на верхний регистр
            st = numbers.get(num3)
            return st.title() # Возвращаем занчение по ключу, где первая буква в Верхнем регистре, остальные - в нижнем
        else:
            return numbers.get(num_2) # Если ключ насчинается с нижнего регистра - выводим значение
    else:
        return 'None'


num = input('Напишите числительное от 0 до 10: ')

print(numbers_translate(num))

# Задание 3
names_dict = {} # Создаем пустой словарь
names = input('Введите имена через пробел без запятых:  ').split() # Вводим имена, разделяя их по пробелам в список


def names_sistem(name2):
    for i in range(len(names)):
        if names_dict.get(names[i][0]):                     # проверяем есть ли такой ключ уже
            lst = names_dict.get(names[i][0])               # выдёргиваем значение по ключу (список) если уже есть
            lst.append(names[i])                            # добавляем в список значение
            names_dict.setdefault(names[i][0], lst)         # обновляем словарь по ключу
        else:
            names_dict.setdefault(names[i][0], [names[i]])  # добавляем значение в виде списка

    return names_dict


print(names_sistem(names))

# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


joke_list = [] # Создаем общий список для n шуток


def joke_maker():
    joke = []  # Создаем пустой список для каждой шутки
    joke.append(random.choice(nouns)) # добавляем в шутку случайно выбраный элемент 1 списка
    joke.append(random.choice(adverbs)) # добавляем в шутку случайно выбраный элемент 2 списка
    joke.append(random.choice(adjectives)) # добавляем в шутку случайно выбраный элемент 3 списка
    return joke

n = int(input('Сколько шуток надобно? '))


for i in range(n):
    st = " ".join(joke_maker()) # преобразуем список в строку

    joke_list.append(st)

print(joke_list)


'''import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


joke_list = [] # Создаем общий список для n шуток


def joke_maker():
    joke = []  # Создаем пустой список для каждой шутки
    joke.append(random.choice(nouns)) # добавляем в шутку случайно выбраный элемент 1 списка
    joke.append(random.choice(adverbs)) # добавляем в шутку случайно выбраный элемент 2 списка
    joke.append(random.choice(adjectives)) # добавляем в шутку случайно выбраный элемент 3 списка
    return joke

n = int(input('Сколько шуток надобно? '))
if n > len(nouns):
    print("Столько нашутить я не могу. Давайте ограничимся меньшим количеством")
else:
    for i in range(n):
        st = " ".join(joke_maker()) # преобразуем список в строку

        joke_list.append(st)

    print(joke_list)
'''