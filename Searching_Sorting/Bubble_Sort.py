from array import array as arr

# Bubble Sort
#a= arr('i',[4,3,5,45,23,76,45,98,76,12,24,33])
#a= arr('i',[1,2,3,4,5,6,7,8,9,10])  #Best case - zero swaps
a= arr('i',[10,9,8,7,6,5,4,3,2,1])   #worst case  - n(n-1)/2 swaps
print("Bubble Sort")
print("array before sorting :")
print(a)

def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


#total_swaps = 0
#total_comparisons =0
for i in range(0,len(a)):
    #swap = 0
    #comparison = 0
    for j in range(0,len(a)-i-1):
        #comparison+=1
        if(a[j]>a[j+1]):
            swap(a,j,j+1)
            #swap+=1
    #total_swaps = total_swaps + swap
    #total_comparisons = total_comparisons + comparison
    #print(f"Pass {i} : No. of Comparions={comparison}, No of swaps={swap}")

print(a)


    
