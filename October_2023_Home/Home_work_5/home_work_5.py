# Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9(включно).
# (так як робили на уроці). Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
#
# Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити
# (додавання, віднімання, множення, ділення). і виведіть йому цю табличку.

# multiplication_table = {}
# addition_table = {}
# subtraction_table = {}
# division_table = {}
#
# # Заповнення словників значеннями
# for i in range(2, 10):
#     for j in range(2, 10):
#         multiplication_table[f"{i}*{j}"] = i * j
#         addition_table[f"{i}+{j}"] = i + j
#         subtraction_table[f"{i}-{j}"] = i - j
#         division_table[f"{i}/{j}"] = i / j
#         # print(multiplication_table)
#
# # Збір всіх словників в один загальний словник
# calculate_dict = {
#     '+': addition_table,
#     '-': subtraction_table,
#     '*': multiplication_table,
#     '/': division_table
# }
# # print(calculate_dict)
#
# user = input("Яку табличку ви хочете побачити? Введіть одну з операцій: '+', '-', '*', '/': ")
# if user in calculate_dict:
#     # Отримання та виведення таблички для обраної операції
#     selected_table = calculate_dict[user]
#     for key, value in selected_table.items():
#         print(f"{key} = {value}")
# else:
#     print("Ви ввели некоректну операцію. Будьте уважні.")
