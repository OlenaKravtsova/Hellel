coding: 'utf-8'
# 1) Напишіть ліст компрехеншин який формує список всіх чисел від 34 до 121 які діляться націло на 3 та на 2
# 2) Напишіть клас калькулятора де будуть 4 арифметичні дії плюс, мінус, додавання, множення - звичайні методи.
# і зробіть статік метод який буде виводити повідомлення, привіт я калькулятор.
# 3) Напишіть тестовий клас який буде тестити попередній калькулятор тільки додавання і ділення.
#  до кожної математичної дії зробіть 5 тестів(використовуйте параметрайз, не пишіть руками зайвого).
#  Зробіть класову фікстуру(класметод) для сетапа і тердауна сетпа буде писати повідомлення в файл коли ми запустили тест
#  та текстове повідомлення що ми стартанули. Тердаун буде писати повідомлення що ми закінчили і також час коли закінчили
#  використайте вже відому вам бібліотеку дататайм
#
# Не оцінюється
# Напишіть ліст компрехеншн який буде заповнювати матрицю 7 на 7 клітинок рандомними цифрами, для рандому використовуйте
# random.randint (рандом в колесах пайтона)

# # 1) Напишіть ліст компрехеншин (comprehantion) який формує список всіх чисел від 34 до 121 які діляться націло на 3 та на 2
list_numbers_divisible = [num for num in range(34, 122) if num % 3 == 0 and num % 2 == 0]
print(list_numbers_divisible)


# 2) Напишіть клас калькулятора де будуть 4 арифметичні дії плюс, мінус, додавання, множення - звичайні методи.
# і зробіть статік метод який буде виводити повідомлення, привіт я калькулятор.

class Calculator:
    general_message = "Привіт, я калькулятор"

# Конструктор класу, який ініціалізує об'єкт калькулятора з двома значеннями
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

# Метод для виконання операції додавання
    def add(self):
        return self.value1 + self.value2

# Метод для виконання операції віднімання
    def subtract(self):
        return self.value1 - self.value2

# Метод для виконання операції множення
    def multiply(self):
        return self.value1 * self.value2

# Метод для виконання операції ділення
    def divide(self):
        if self.value2 != 0:
            return self.value1 / self.value2
        else:
            return "Помилка: ділення на нуль"

#Статичний метод, який виводить статичне повідомлення
    @staticmethod
    def greet():
        print(Calculator.general_message)


# Приклад використання класу
calc = Calculator(10, 5)

# Вивід привітання
Calculator.greet()

# Використання різних арифметичних операцій
print("Додавання:", calc.add())
print("Віднімання:", calc.subtract())
print("Множення:", calc.multiply())
print("Ділення:", calc.divide())