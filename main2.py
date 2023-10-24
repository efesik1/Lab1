string = input("Введи строку ")
string = string.lower()
glas = "aouie"
glas_count = 0
sogl_count = 0
word_count = 0
glas_letters = []
for char in string:
    if char.isalpha():
        if char in glas:
            glas_count += 1
            glas_letters.append(char)
        else:
            sogl_count += 1
    elif char.isspace():
        word_count +=1
word_count += 1
print(f"Гласных: ", glas_count)
print(f"Согласных: ", sogl_count)
if sogl_count == glas_count:
    print("Гласные буквы в тексте:")
    print(" ".join(glas_letters))
print(f"Количество слов в тексте:", word_count)
