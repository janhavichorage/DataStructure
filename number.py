n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter the number: "))
    arr.append(num)

largest = arr[0]
smallest = arr[0]

for i in range(n):
    if arr[i] > largest:
        largest = arr[i]

    if arr[i] < smallest:
        smallest = arr[i]

second_largest = arr[0]
second_smallest = arr[0]

for i in range(n):
    if arr[i] != largest and arr[i] > second_largest:
        second_largest = arr[i]

    if arr[i] != smallest and arr[i] < second_smallest:
        second_smallest = arr[i]

print("Smallest element:", smallest)
print("Largest element:", largest)
print("Second largest:", second_largest)
print("Second smallest:", second_smallest)

