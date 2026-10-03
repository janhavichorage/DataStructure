n=int(input("Enter your numbers of element:"))
arr=[]

for i in range(n):
    num=int(input("Enter your number:"))
    arr.append(num)

searching_num=int(input("enter serching number:"))
if searching_num in (arr):
        print("number is in the list")
        print("position is",arr.index(searching_num))
else:
      print("not in list")
    

