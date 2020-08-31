"""4. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран."""

file_name = input("Введите имя файла: ")
with open(f"./files/{file_name}", "w") as f_obj:
    f_obj.write(' '.join([str(i) for i in range(1, 20)]))

with open(f"./files/{file_name}") as f_obj:
    print(sum([int(i) for i in f_obj.readline().split(" ")]))
