"""5. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
по нему. Вывести словарь на экран.

Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

import re

out = {}

with open("./files/task_05.txt", "r") as f_obj:
    for lines in f_obj.readlines():
        name, info_name = lines.split(":")
        hours = re.findall(r'\d+', info_name)
        out[name] = sum([int(i) for i in hours])

print(out)
