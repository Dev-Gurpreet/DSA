# Quick Sort
from array import array as arr

a= arr('i',[10,9,8,7,6,5,4,3,2,1]) 
#a= arr('i',[1,2,3,4,5,6,7,8,9,10]) #worst case = O(n**2)
#a= arr('i',[4,3,5,45,23,76,45,98,76,12,24,33])
print("Quick Sort")
print("array before sorting :")
print(a)


def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def partition(a,i,j):
    pivot = a[i]
    L = i
    for R in range(i+1,j):
        if (a[R]<=pivot):
            L=L+1
            swap(a,L,R)
    swap(a,i,L)
    return L


def quickSort(a,i,j):
    if i==j:
        pass
    else:
        m = partition(a,i,j)
        quickSort(a,i,m)
        quickSort(a,m+1,j)


quickSort(a,0,len(a))
print(a)