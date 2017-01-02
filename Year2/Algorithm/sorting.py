
def swap(array, i,j):
    '''input index i and j of the array'''
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def bubblesort(array, debug=False):
    '''push the largest value to the right'''
    n = len(array)         
    if debug: print array
    for j in range(n-1, 0, -1):       # j is the position to be sorted.
        for i in range(j):
            if(array[i]>array[i+1]):
                swap(array, i, i+1)
                if debug: print array, "j=", j, "i=", i
        
def selectionsort(array, debug=False):
    '''select the minimum of unsorted and swap with the front of unsorted'''
    n = len(array)
    if debug: print array
    for front in range(n):
        minval = array[front]
        pos = front
        for i in range(front, n):
            if(array[i] < minval):          ## 1) select minimum value among unsorted
                minval = array[i]
                pos = i
        swap(array, front, pos)             ## 2) swap with the front of unsorted.
        if debug: print "minval=", minval, array

def insertionsort(array, debug=False):
    '''select element from front of unsorted and push it to the correct position in the left sorted'''
    n = len(array)
    if debug: print array
    for i in range(1, n):               ## 1) skip first element because alr sorted.
        for j in range(i, 0, -1):       ## 2) i is selected element's pos. 
            if (array[j] < array[j-1]): ## 3) push the element to correct position on the left
                swap(array, j, j-1)
                if debug: print array, "boundary index of sorted=", i
        

def merge(array, low, high, debug=False):
    '''sorting done during merging.
merge without using auxiliary array'''
    mid = (low+high)/2  # boundary between left and right incompletes
    a = low     # point to front of unsorted1
    b = mid+1   # point to front of unsorted2
    if debug: print "=merge=\n", array[low:high+1], "a=", a, "b=", b
    while(a <= mid and b<= high):
        if(array[a] < array[b]):
            a+=1
        elif(array[b] < array[a]):
            for i in range(b, a, -1):   #push b all the way to position a 
                swap(array, i, i-1)
            a+=1
            b+=1
            mid+=1                      #need to shift mid by 1 to retain the boundary
        else:
            if(a == mid and b == high): #both are already in correct place at the end of the boundaries
                break
            a+=1                        #increment 1 because 1 of them is already in position.
            for i in range(b, a, -1):   #push the other to the position of a
                swap(array, i, i-1)
            a+=1
            b+=1
        if debug: print array[low:high+1], "a=", a, "b=", b
    if debug: print "-> finish merge"

def mergesortR(array, low, high, debug=False):
    '''low and high are indices of the array.
divide the array into smaller subarray and sort during merging.'''
    if low==high:       ## 1) 1 element is sorted, terminate recursion
        return;
    mid = (low+high)/2
    if(high-low>=1):  ## 2) at least 2 elements
        mergesortR(array, low, mid, debug)
        mergesortR(array, mid+1, high, debug)
        if debug: print "trying to merge", array[low:mid+1], "and", array[mid+1:high+1]
        merge(array, low, high, debug)
        
def mergesort(array, debug=False):
    '''call mergesortR without indicating indices to sort'''
    mergesortR(array, 0, len(array)-1, debug)

def partition(array, low, high, debug=False):
    '''find the correct position for the chosen pivot(mid) element'''
    if debug: print "=partition=\n", array[low:high+1]
    pivot = (low+high)/2
    last_small = low
    swap(array, pivot, low)             # 1)temporary store the element at the front
    i = low+1
    while(i<=high):                     # 2)scan the rest
        if (array[i] < array[low]):     # smaller than pivot element.
            last_small+=1
            swap(array, last_small, i)  # if array[i] > pivot value, wait until smaller is seen again then bring smaller to the last_small pos.
        i+=1
    swap(array, last_small, low)        # 3)elements LHS < pivot <= elements RHS
    if debug: print "LHS:", array[low:last_small],"pivot:", array[last_small],"RHS:", array[last_small+1:high+1]
    return last_small                   # 4)last_small is the correct pos of the pivot.
            
def quicksortR(array, low, high, debug=False):
    '''low and high are indices.
recursively divide the array into varying length and sort while partitioning the pivot'''
    if low==high:           # only 1 element.
        return;
    if (high-low >= 1):     #at least 2 elements
        pivot = partition(array, low, high, debug)
        quicksortR(array, low, pivot-1, debug)
        quicksortR(array, pivot+1, high, debug)

def quicksort(array, debug=False):
    '''call quicksortR without indicating indices to sort'''
    quicksortR(array, 0, len(array), debug)

if __name__ == "__main__":
    array = [5,2,3,1,4,0]

    #bubblesort(array, debug=True)
    #selectionsort(array, debug=True)
    #insertionsort(array, debug=True)
    #mergesort(array, debug=True)
    quicksort(array, debug=True)

    print "result=", array
    

        
