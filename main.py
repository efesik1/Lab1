sum = 0
while True:
    try:
        num = int(input("Введите число: "))
        while num > 0:
            digit = num % 10
            if digit % 2 == 0:
                sum += digit
            num //= 10
        print("Сумма четных цифр: ", sum)
        break  
    except ValueError:
        print("Ошибка: Введено нечисловое значение. Пожалуйста, введите число.")
