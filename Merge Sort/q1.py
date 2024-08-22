def mergesort(array):
    if len(array) > 1:
        mid = len(array)//2
        left_array = array[:mid]
        right_array = array[mid:]
        mergesort(left_array)
        mergesort(right_array)
        i,j,k = 0,0,0
        while i < len(left_array) and j < len(right_array):
            if left_array[i]<right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

array = [45,2,56,6,11,5,98,33,57,4]
mergesort(array)
print(array)