list = [12, 511, 'Python', 311, 122, 'love']
for i in range(len(list)):
    if isinstance(list[i], int) and list[i] % 2 == 0:
        digit_sum = 0
        for digit in str(list[i]):
            if digit.isdigit():
                digit_sum += int(digit)
        list[i] = digit_sum
    elif isinstance(list[i], int) and list[i] % 2 != 0:
        list[i] = 1
print(list)