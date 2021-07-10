# Merge Sort
from array import array as arr
from math import floor

a= arr('i',[10,9,8,7,6,5,4,3,2,1])  
#a= arr('i',[4,3,5,45,23,76,45,98,76,12,24,33])
print("Merge Sort")
print("array before sorting :")
print(a)


def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def merge(a,i,x,y,j):
    start = i
    b= arr('i',[])

    while(i<=x and y<=j):
        if a[i]<=a[y]:
            b.append(a[i])
            i+=1
        else:
            b.append(a[y])
            y+=1
    
    while(i<=x):
        b.append(a[i])
        i+=1

    while(y<=j):
        b.append(a[y])
        y+=1

    for k in range(0,len(b)):
        a[start]=b[k]
        start+=1


def mergeSort(a,i,j):
    if i==j:
        pass
    else:
        mid=floor((i+j)/2)
        mergeSort(a,i,mid)
        mergeSort(a,mid+1,j)
        merge(a,i,mid,mid+1,j)


mergeSort(a,0,len(a)-1)
print(a)