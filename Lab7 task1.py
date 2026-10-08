s=input("Введіть рядок: ")
a = 0
b = 1
for i in s:
    if i.isdigit():
        a += int(i)
        b *= int(i)
    elif i.isalpha():
        print("Буква", i)
    else: 
        print("Інший символ", i)
print("Сума цифр", a)
print("Добуток цифр", b)