coding: 'utf-8'
# 1) Створіть клас Студент, в ньому обявіть дві змінні імя де збережети імя студента, та список його оцінок.
# створіть два метода в цьому класі, перший метод який буде вітатись і при вітання використовувати імя студента.
# другий метод буде виводити оцінки. Методи виводять результат через прінти.
# Створіть два екземпляра цього класу, в другому екземплярі змніть імя на своє(не міняючи нічого в класі). Вивідіть дві
# функції цих екземплярів, що б кожен студент привітався та сказав свої оцінки.

# # Клас студентів та їх дані
# class Student:
#     name = "Oleg"
#     grades = [2, 5]
#
#     # Метод вітання зі студентом
#     def say_hello(self):
#         print(f"Привіт, {self.name}!")
#
#     # Метод виводу оцінок
#     def result_grades(self):
#         print(f"Твої оцінки: {self.grades}")
#
# # Створення першого екземпляра
# obj_1 = Student()
# obj_1.say_hello()
# obj_1.result_grades()
#
# # Створення другого екземпляра з власним ім'ям
# obj_2 = Student()
# obj_2.name = "Olena"
# obj_2.say_hello()
# obj_2.grades = [88, 2, 9]
# obj_2.result_grades()



# 2) Напишіть 5 тестів з затримкою в 2 секунди кожен, один з тестів повинен мати унікальне імя.
#  Запустіть їх за домогою pytest-xdist ліби в 5 потоків.
#  Запустіть цей ваш унікальний тест з маркером -k
#  додайте скірншоти виконання (не забудьте додавати -v, що б я бачив що ви проганяли) і біля скріншотів пропишіть команди
#  які ви використовували.
# py -m pytest -v -n=5
# py -m pytest -k "test_first" -v
# py -m pytest -k "test_second" -v
# py -m pytest -k "test_third" -v
# py -m pytest -k "test_wait" -v
# py -m pytest -k "test_fifth" -v

# 3) обновіть requirements.txt




