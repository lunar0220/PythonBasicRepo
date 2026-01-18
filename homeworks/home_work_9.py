def number_sequence(start, end, even=True):
    for number in range(start, end + 1):
        if even and number % 2 == 0:
            yield number
        elif not even and number % 2 != 0:
            yield number


try:
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))

    choice = input("Введите тип последовательности (чётные / нечётные): ").strip().lower()

    if choice in ("чётные", "четные"):
        even = True
    elif choice in ("нечётные", "нечетные"):
        even = False
    else:
        print("Ошибка: введите 'чётные' или 'нечётные'.")
        exit()

    print("Сгенерированная последовательность:")
    for num in number_sequence(start, end, even):
        print(num, end=" ")
    
    
except ValueError:
    print("Ошибка: необходимо вводить целые числа.")