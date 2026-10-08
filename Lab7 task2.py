import random
N = int(input("Введіть кількість рядків: "))
for i in range(N):
    N1 = input("Введіть рядок: ")
    value = []

    if len(N1) % 3 == 0:
        k = len(N1) // 3

        for v in range(3):
            part = N1[v*k:(v+1)*k]
            value.append(part)

        random.shuffle(value)
        for v in value:
            print(v)
        print("Випадковий список:", value)
    else:
        print("Рядок не кратний 3")
