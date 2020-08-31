"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
окончании ввода данных свидетельствует пустая строка.
"""

file_name = input('Как назовем файл: ')
open_file = open(file_name + '.txt', 'w')

while True:
    text_input = input("[>>] ")

    if text_input == '':
        break
    open_file.write(text_input + '\n')
open_file.close()
