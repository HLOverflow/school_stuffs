# python 2

def mergesort(array):
    low = 0
    high = len(array) - 1
    mid = (low + high)/2
		
    if (len(array)==1): return array
    else:
        array1 = mergesort(array[: mid+1])
        array2 = mergesort(array[mid+1:])
        return merge(array1, array2)

def merge(array1,array2):
    #print array1, array2
    i=j=k=0
    sortedarray = []
    while( i < len(array1) and j < len(array2) ):
        if array1[i] <= array2[j]:
            sortedarray.append(array1[i])
            i += 1
            k += 1
        else:
            sortedarray.append(array2[j])
            j += 1
            k += 1
    if (i >= len(array1)):
        sortedarray.extend(array2[j:])
    elif (j >= len(array2)):
        sortedarray.extend(array1[i:])

    #print sortedarray
    #print '='*10
    return sortedarray;

unsorted = [2,3,1,4,7,6]
print "unsorted: ", unsorted
print "sorted: ", mergesort(unsorted)
