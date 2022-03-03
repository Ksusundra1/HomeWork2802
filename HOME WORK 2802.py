# Задание 1
a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Задание 2
sp = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_sp = []

for i in range(len(sp)):
    if sp[i].isalpha() is True:
        new_sp.append(sp[i])
    elif sp[i].isdigit() is True and len(sp[i]) == 1:
            new_sp.append('"' + '0' + sp[i] + '"')
    elif sp[i].isdigit() is True and len(sp[i]) > 1:
            new_sp.append('"' + sp[i] + '"')
    else:
        s = []
        n = sp[i].split()
        for i in range(len(n)):
            if n[i].isdigit() is False:
                s.append(n[i])
            elif n[i].isdigit() is True:
                s.append('0', n[i])

        new_sp.append('"' + ','.join(s) + '"')

print(new_sp)
print(* new_sp)

# Задание 3
sp = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_sp = []

for i in range(len(sp)):
    if sp[i].isalpha() is True:
        new_sp.append(sp[i])
    elif sp[i].isdigit() is True and len(sp[i]) == 1:

        new_sp.append('"' + '0' + sp[i] + '"')
    elif sp[i].isdigit() is True and len(sp[i]) > 1:
        new_sp.append('"' + sp[i] + '"')
    elif sp[i][0] == "+":
        new_sp.append('"+' + '0' + sp[i][1:] + '"')

print(new_sp)
print(*new_sp)



# Задание 4
sp = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']
for i in range(len(sp)):
    n = sp[i].split()
    name = n[-1].title()
    print('Привет,', name + '!')

# Задание 5
import math
sp = [57.8, 46.51, 97, 18.54, 45.13, 36.5, 84.03, 12.38, 19.98, 20.22]
for i in range(len(sp)):
    rub = int(sp[i] // 1)
    coin = str(round(sp[i] % rub, 2))
    n = coin.find('.')
    coin_prise = coin[n +1:]
    if len(coin_prise) == 1:
        print(rub, 'руб.', coin_prise + '0', 'коп.')
    else:
        print(rub, 'руб.', coin_prise, 'коп.')

sp.sort()
print(sp)

new_sp =[]
for i in range(len(sp)):
    new_sp.append(max(sp))
    sp.remove(max(sp))
print(new_sp)

expensive = new_sp[:4]
expensive.sort()
print(expensive)
