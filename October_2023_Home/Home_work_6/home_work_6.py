# Домашка
# Візьміть дві задачі з попередніх уроків, перша легка по вирішенню (декілька стрічок),
# друга більш складна і перепишіть їх на функції. Памятайте про Атамарність та god object.
# Там де написано що користувач має щось ввести то перероблюємо на функція приймає.
# Подивіться може можна за допомогою функції спростити код.
# В домашку вставте будь ласка опис задачі (далі(один з наступних уроків)
# буде домашка вашу домашку покрити тестами, але ми трохи поміняємо варіанти).
# розширення функцій які існують VS власний функціонал

# # lesson_1
# # 3.Цілочисельне ділення: Користувач вводить два числа. Вивести, скільки разів перше число ділиться на друге без залишку.
# numeric_1 = input(int("Введіть перше число: "))
# numeric_2 = input(int("Введіть друге число: "))
# result = numeric_1 // numeric_2
# print(result)
# print(type(result))

# # Задача 1.
# # Функція обрахування
# def divide_numbers(numeric_1 : int, numeric_2: int):
#     result = numeric_1 // numeric_2
#     return result
#
# # Функція для виведення результату
# def format_result(result):
#     formatted_string = f"Ваш результат ділення: {result}"
#     return formatted_string
#
# # Виклик функції для ділення чисел
# result_numeric = divide_numbers(numeric_1=101, numeric_2=25)
#
# # Виклик функції для форматування результату
# new_string = format_result(result=result_numeric)
#
# # Вивід результату
# print(new_string)


# # lesson_4
# Задача 2
# Уявимо що до нас прийшов наш друг або подруга і попросили написати додаток для покупок в магазині
# що б можна було скласти список продуктів та коли купуєш викреслювати(для викреслення питайте номер елемента,
# # що б видалити по індексу треба його передати
# # в pop list_a.pop(0) - видалить нульовий індекс, памятайте що користувач не знає що в нас індекси починаються з нуля)
# # Також нам відомо що цей список має пять або більше елементів.
# # Після кожного видалення елементу виводьте наш оновлений список.
# # Після 5 видалень перевірте чи список пустий якщо не пустий напишіть що ось ще є продукти, якщо пусти то напишіть про це.
# # Також після цього кроку запропонуйте користувачу написати ще продуктів та додати його в кошик.
# # і виведіть їх на екран. Але цього разу вже без видалень.
# # кроки:
# # Спочатку пропонуємо користувачу ввести продукти.
# # Робимо 5 запитів на видалення
# # Перевіряємо корзину
# # Пропонуємо додати продукти
# # Виводмо список і прощаємось

# # Задача 2.
# # Функція приймає список product_list і виводить його елементи та відповідні індекси.
# def display_list_and_indexes(product_list):
#     indexes = list(range(1, len(product_list) + 1)) #щоб індексація починалася з 1
#     print("Список продуктів:", product_list)
#     print("Індекси продуктів:", indexes)
#
# # Функція приймає список product_list і index, а потім видаляє елемент за вказаним індексом.
# def remove_element_by_index(product_list, index):
#     if 1 <= index <= len(product_list):
#         product_list.pop(index - 1)
#         print("Оновлений список продуктів:", product_list)
#     else:
#         print("Невірний індекс. Спробуйте ще раз.")
#
# # Функція main починається з отримання списку від користувача.
# def main():
#     user_input = input("Введіть список продуктів через пробіл: ")
#     shopping_list = user_input.split()
#
# # Відображення списку та індексів та видалення елементів за індексами.
#     for _ in range(5):
#         display_list_and_indexes(shopping_list)
#         index_to_remove = int(input("Введіть індекс для видалення: "))
#         remove_element_by_index(shopping_list, index_to_remove)
#
# # Оновлений список після циклу видалення.
#     if not shopping_list:
#         print("У корзині порожньо!")
#     else:
#         print("У корзині ще є продукти:", shopping_list)
#
# # Додавання нових елементів до списку
#     add_to_list = input("Бажаєте додати в список? Якщо ні, пропустіть цей крок: ")
#     shopping_list.extend(add_to_list.split())
#
#     if shopping_list:
#         print("У корзині:", shopping_list)
#     else:
#         print("Кошик пустий. До побачення!")
#
# # Робота функції завершена.
# main()