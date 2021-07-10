# linear Search

a = list(input("Enter the list of numbers separated by comma: ").split(","))
x = input("enter the number you want to search: ")


i, flag = 0,0
while(i<len(a)):
    if a[i] == x:
        flag=1
        print (f"Number {x} found at index {i}")
        break
    i+=1
if flag==0:
    print (f"Number {x} is not present in list")

