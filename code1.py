a = [12, 45, 23, 67, 34]
smallest = a[0]

for i in a:
    if i < smallest:
        smallest = i

print(smallest)