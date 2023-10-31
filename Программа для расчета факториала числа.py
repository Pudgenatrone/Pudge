# Функция для вычисления факториала числа
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Запрос числа у пользователя
num = int(input("Введите число: "))

# Вычисление и вывод факториала
result = factorial(num)
print(f"Факториал числа {num} равен {result}")
