from array import array as arr

# Selection Sort

a= arr('i',[10,9,8,7,6,5,4,3,2,1])   
print("Selection Sort")
print("array before sorting :")
print(a)


def swap(a,x,y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp


#total_swaps = 0
#total_comparisons =0


for i in range(0,len(a)):
    key = a[i]
    pointer = i
    #swap = 0
    #comparison = 0
    for j in range(i+1,len(a)):
        #comparison+=1
        if(a[j]<key):
            key = a[j]
            pointer = j
    if(pointer != i):
        swap(a,i,pointer)
        #swap+=1   
 
    #total_swaps = total_swaps + swap
    #total_comparisons = total_comparisons + comparison
    #print(f"Pass {i} : No. of Comparions={comparison}, No of swaps={swap}")

#print(f"Total No. of Comparions={total_comparisons} and Total No. of swaps={total_swaps}")
print(a)
        

    
