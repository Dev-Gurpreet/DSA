# Binary Search 

from array import array as arr
from math import floor

a = arr('i',[1,2,3,4,5,6,7,8,9,10]) 
print(a)
x = int(input("Enter the number to know its location: "))

def binarySearch(a,i,j,x):
    print(i,j)
    mid = floor((i+j)/2)
    if x == a[mid]:
        print(f"{x} is present in array at {mid} location")
    elif x < a[mid]:
        binarySearch(a,i,mid-1,x)
    else:
        binarySearch(a,mid+1,j,x)


binarySearch(a,0,len(a),x)