# 1. Поработайте с переменными, создайте несколько, выведите на экран
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

# Создайте несколько, выведите на экран
print("Это самый обычный вывод значений двух присвоенных переменних:")
a = 1
b = 2

print("Переменная a: {0}\nПеременная b: {1}\n".format(a, b))

# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

first_question = int(input("Введите число а: "))
second_question = int(input("Введите число b: "))
third_question = str(input("Как, к вам можно обращаться? "))

print("Ваши значения: ", first_question, second_question, third_question)

print("Число а: {0}, число b: {1}, Ваше имя: {2}".format(first_question, second_question, third_question))

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

convert_time = int(input("Введите время (в секундах): "))

print("{0:02d}:{1:02d}:{2:02d}".format((convert_time // 3600), (convert_time - (convert_time // 3600) * 3600) // 60,
                                       (convert_time % 60)))

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.

number = int(input("Введите число (n): "))
string_number = str(number)

second_string_number = string_number + string_number
third_string_number = string_number + string_number + string_number

sum_number = number + int(second_string_number) + int(third_string_number)

print("Сумма выражения n + nn + nnn = ", sum_number)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите число x = "))
last_number = number % 10
number = number // 10

while number > 0:
    if number % 10 > last_number:
        last_number = number % 10
    number = number // 10

print(last_number)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

print("Привет друг, сейчас мы разберемся с финаносвыми показателями, поеали!")
revenue = int(input("Введите показатель выручки за 2019 год, в рублях: "))
cost = int(input("Введите показатель издережек за 2019 год, в рублях: "))

# считаем прибыль = выручука - издержки
profit = revenue - cost

if revenue > cost:
    print("Положительная динамика! Мы получили прибыль – {0:,} и можем расчитать рентабельность...".format(profit))

    # считаем рентабельность = прибыль / выручка
    print("Показатель рентабельности составляет: %.2f" % (profit / revenue))

else:
    print("Кажется у нас убыток...")

# запросим численность сотрудников
print("Теперь, определите прибыль фирмы в расчете на одного сотрудника!")

staff_count = int(input("Введите количество сотрудников: "))

print("Производительность на 1 ед. составила - %.2f рублей." % (profit / staff_count))

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
# спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который
# результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня.

first_day = int(input("Введите количество километров первого дня: "))
your_aim = int(input("Введите вашу цель: "))
counter = 1

# while your_aim - first_day > 0:
#     first_day = first_day + (first_day * 0.1)
#     counter += 1
# print(counter)

while your_aim - first_day > 0:
    first_day = first_day + (first_day * 0.1)
    counter += 1
    print("День по счету: %.0f-й Сегодня ты прошел: %.2f" % (counter, first_day))

print("Миссия выполнена на {} день!".format(counter))