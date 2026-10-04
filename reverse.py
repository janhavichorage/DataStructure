n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

reverse_arr = []

for i in range(n - 1, -1, -1):
    reverse_arr.append(arr[i])

print("Reversed array:", reverse_arr)