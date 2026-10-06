n = 7

for i in range(n):
    for j in range(n):
        distance = (i - n // 2) ** 2 + (j - n // 2) ** 2

        if 5 <= distance <= 10:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()