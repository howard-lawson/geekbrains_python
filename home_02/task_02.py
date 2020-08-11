# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у
# пользователя, а указать явно, в программе.

home_list = [2, "text", 63.1, None, True]

for elem in home_list:
    print(type(elem))


def type_func(sign):
    for sign in range(len(home_list)):
        print(type(home_list[sign]))
    return

type_func()

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
# 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().


start_array = int(input("Введите число элементов в списке: "))
end_array = []
step = 0
zero = 0

while step < start_array:
    end_array.append(input("Следующее значение: "))
    step += 1

print(end_array)

for elem in range(int(len(end_array) / 2)):
    end_array[zero], end_array[zero + 1] = end_array[zero + 1], end_array[zero]
    zero += 2
print(end_array)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.
#
user_input_month = int(input("[Список] Введите месяц в виде чиcла от 1 до 12: "))

# реализация списком
winter_list = [12, 1, 2]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
autumn_list = [9, 10, 11]

if user_input_month in winter_list:
    print("На дворе зима!")
elif user_input_month in spring_list:
    print("На дворе весна!")
elif user_input_month in summer_list:
    print("На дворе лето!")
elif user_input_month in autumn_list:
    print("На дворе осень!")
else:
    print("В году 12 месяцев, введите число от 1 до 12")

user_input_month = int(input("[Словарь] Введите месяц в виде чиcла от 1 до 12: "))
#
# # реализация словарем
seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

for key in seasons.keys():
    if user_input_month in seasons[key]:
        print("На дворе {}!".format(key))

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_input = input("Напишите любое предложение: ")
user_word = []
num = 0

for el in range(user_input.count(' ') + 1):
    user_word = user_input.split()

    if len(str(user_input)) <= 10:
        num += 1
        print(f" {num} {user_word[el]}")
    else:
        num += 1
        print(f" {num} {user_word[el][0:10]} ")


# а еще можно вот так

result = '\n'.join([
    f'{idx} - {word[:10]}'
    for idx, word in enumerate(input().split(' '))
    if word
])
print(result)

'''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя 
необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них. 

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2. 
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
'''

my_list = [9, 3, 5, 1, 2]

print(f"Рейтинг - {my_list}")

take_rate = int(input('Установите значение рейтинга: '))

while take_rate != "exit":
    for rate in range(len(my_list)):
        if my_list[rate] == take_rate:
            my_list.insert(rate + 1, take_rate)
            break
        elif my_list[0] < take_rate:
            my_list.insert(0, take_rate)
        elif my_list[-1] > take_rate:
            my_list.append(take_rate)
        elif my_list[rate] > take_rate > my_list[rate + 1]:
            my_list.insert(rate + 1, take_rate)
    print(f"текущий список - {my_list}")
    digit = int(input("Установите значение рейтинга: "))
