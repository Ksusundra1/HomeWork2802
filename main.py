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
if n > len(nouns):
    print("Столько нашутить я не могу. Давайте ограничимся меньшим количеством")
else:
    for i in range(n):
        st = " ".join(joke_maker()) # преобразуем список в строку

        joke_list.append(st)

    print(joke_list)
