from array import array as arr

# Insertion Sort

a= arr('i',[4,3,5,45,23,76,45,98,76,12,24,33])
print("array before sorting :")
print(a)

for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while(j>=0 and a[j]>key):
        a[j+1]=a[j]
        j=j-1
    a[j+1]=key
    print(f"Array after pass {i-1}: {a}")
