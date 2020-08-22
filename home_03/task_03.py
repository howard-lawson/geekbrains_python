import re

"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def test(a, b):
    """
    :param a: первое число
    :param b: второе число
    :return: вывод результата
    """

    try:
        return a / b
    except ZeroDivisionError:
        return 0


print(test(4, 2))

print('*' * 50)
print('Вторая задача')
print('*' * 50)

"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, 
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой. 
"""

user_data_dict = {
    'name': 'Василий',
    'surname': 'Иванович',
    'year': '1992',
    'city': 'Москва',
    'email': 'vasya@mail.ru',
    'phone': '+7999090909'
}


def user_data(name='Василий', surname='Иванович', year='1992', city='Москва', email='vasya@mail.ru',
              phone='+7999090909'):
    print(f"\n Пользовательские данные: Имя: {name} \n Отчество: {surname} \n Год рождения: {year} \n Город: {city} \n "
          f"Почта: {email} \n Телефон: {phone}")


user_data(**user_data_dict)

print('*' * 50)
print('Третья задача')
print('*' * 50)

"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух 
аргументов. 
"""


def position_arg(x, y, z):
    my_dict = [x, y, z]
    my_dict.sort()
    return my_dict[1] + my_dict[2]


print("Сумму наибольших двух аргументов: ", position_arg(5, 4, 1))

print('*' * 50)
print('Четвертая задача')
print('*' * 50)

"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить 
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания 
необходимо обойтись без встроенной функции возведения числа в степень. 
"""


def math(x, y):
    count = 1
    result = 1

    if x > 0 and y < 0:
        while count <= abs(y):
            result *= x
            count += 1
        print(1 / result)
        return
    else:
        print(f"Переменная Х принимает ТОЛЬКО действительное положительное число\nПеременная Y - целое отрицательное "
              f"число!")


math(3, -4)

"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма 
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных 
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение 
программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих 
чисел к полученной ранее сумме и после этого завершить программу. 
"""
print('*' * 50)
print('Пятая задача')
print('*' * 50)

# def user_sum():
#     total_result = 0
#
#     while True:
#         user_input = input('Введите число или # чтобы завершить программу: ').split()
#         current_sum = 0
#
#         for element in range(len(user_input)):
#             if user_input[element] == '#':
#                 break
#             else:
#                 current_sum = current_sum + int(user_input[element])
#         total_result = total_result + current_sum
#         print(f'Ваша сумма - {total_result}')
#     print(f'Общая сумма - {total_result}')
#
#
# user_sum()

'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, 
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. 
'''


def int_func(user_input):
    error_text = "Русские символы запрещены!"
    alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
                "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    for char in user_input:
        if char in alphabet:
            return error_text
        else:
            return user_input.title()


user_input = input()
print(int_func(user_input))

