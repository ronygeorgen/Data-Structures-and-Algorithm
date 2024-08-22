# Divide and conquer Technic
# Finding out the proper place for pivot element and partitioning the array into two parts
def partition(a, lb, up):
    pivot = a[lb]
    start = lb
    end = up
    while start < end:
        while a[start] <= pivot:
            start += 1
        while a[end] > pivot:
            end -= 1
        if start < end:
            a[start], a[end] = a[end], a[start]
        else:
            break
    a[lb], a[end] = a[end], a[lb]
    return end

def quicksort(a,lb,up):
    if lb < up:
        loc = partition(a,lb,up)
        quicksort(a,lb,loc-1)
        quicksort(a,loc+1,up)

arr = [2,42,56,1,4,89,23,11,7,3]
quicksort(arr,0,len(arr)-1)
print(arr)