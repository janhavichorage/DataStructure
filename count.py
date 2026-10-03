n=int(input("enter numbers of elemet:"))

arr=[]
count_even=0
count_odd=0
for i in range(n):
    num=int(input("enter your number:"))
    arr.append(num)

    if(num%2==0):
        count_even=count_even+1
    if(num%2!=0):
        count_odd=count_odd+1
print("Even numbers:",count_even)
print("odd numbers count:",count_odd)