def number_sequence(start, end, even=True):
    for number in range(start, end + 1):
        if even and number % 2 == 0:
            yield number
        elif not even and number % 2 != 0:
            yield number

# Ввод данных с обработкой ошибок
try:
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
except ValueError:
    print("Ошибка: начало и конец диапазона должны быть целыми числами.")
    exit()

# Проверка корректности диапазона
if start > end:
    print("Ошибка: начало диапазона не может быть больше конца.")
    exit()

choice = input("Введите тип последовательности (четные / нечетные): ").lower()

# Определение типа последовательности
if choice == "четные":
    sequence = number_sequence(start, end, even=True)
elif choice == "нечетные":
    sequence = number_sequence(start, end, even=False)
else:
    print("Ошибка: введите 'четные' или 'нечетные'.")
    exit()

# Вывод результата
print("Сгенерированная последовательность:")
for num in sequence:
    print(num, end=" ")