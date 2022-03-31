import requests #импортировала всё нужное по условию
from datetime import datetime
from decimal import *

def exchange(money):
    money = money.apper() # единый регистр ввода ключа
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text # забираю с заданного API xml
    if money not in response:
        return None #Если такого ключа в xml нет - возврашаем ничего
    tugrik = response[response.find('<Value>', response.find(money)) + 7:response.find('<Value>', response.find(money))] # Ищем в xml значение ввеженной валюте-ключу
    dates = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.') # ищу дату, её обрамляют кавычки, разделяю в список по точкам
    day, month, year = map(int, dates)
    date = datetime(day = day, month = month, year = year) # переменная дата
    return f"{Decimal(tugrik.replace(',', '.'))}, {datetime(date)}" # возвращает значение с заменой запятой на точку и дату

if __name__ == '__main__':
    import sys
    print(sys.argv)