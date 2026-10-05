n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

index = 0


for i in range(n):
    if arr[i] != 0:
        arr[index] = arr[i]
        index += 1


while index < n:
    arr[index] = 0
    index += 1

print("Array after moving zeros to end:")
print(arr)