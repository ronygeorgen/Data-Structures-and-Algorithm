def partition(array,lb,up):
    pivot = array[lb]
    start = lb
    end = up

    while start < end:
        while start <= up and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if start < end:
            array[start], array[end] = array[end], array[start]
        else:
            break
    array[lb], array[end] = array[end], array[lb]
    return end

def quick_sort(array,lb,up):
    if lb < up:

        index = partition(array,lb,up)

        quick_sort(array,lb,index-1)
        quick_sort(array,index+1,up)

array = [2,42,56,1,4,89,23,11,7,3]

quick_sort(array,0,len(array)-1)
print(array)