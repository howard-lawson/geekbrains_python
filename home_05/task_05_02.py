"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке. """

with open("./files/task_02.txt") as f_obj:
    lines = 0
    for elem in f_obj.readlines():
        lines += 1

        total_word = 0
        flag = 0

        for words in elem:
            if words != ' ' and flag == 0:
                total_word += 1
                flag = 1
            elif words == ' ':
                flag = 0
        print(elem, len(elem), 'симв.', total_word, 'сл.')

print('Всего:', lines, 'стр.')
