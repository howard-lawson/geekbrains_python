import random


def salary(total=0, bonus=0):
    """
    :param total: величина зарплаты
    :param bonus: премия сотрудника
    :return: сумма вознаграждения
    """
    try:
        total = int(total)
        bonus = int(bonus)

        if total > 0 and bonus > 0:
            total = (total * .87) + bonus
            return total
        else:
            print("Допустимы только положительные числа")
    except TypeError:
        print("Зарплата вводится в числовом эквиваленте!")


""""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


def second_task():
    gen_list = [random.randint(1, 10) for _ in range(10)]
    print(gen_list)

    final_list = [
        gen_list[el]
        for el in range(1, len(gen_list))
        if gen_list[el] > gen_list[el - 1]
    ]

    print(final_list)


def uniques(it):
    seen = set()
    for val in it:
        if val not in seen:
            yield val
        seen.add(val)

