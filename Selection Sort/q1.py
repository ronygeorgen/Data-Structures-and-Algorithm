arr = [34,6,80,2,4,7,1]
n = len(arr)
for i in range(n-1):
    min = i
    for j in range(i+1,n):
        if arr[j] < arr[min]:
            min = j
    if min != i:
        arr[i], arr[min]= arr[min], arr[i]
print(arr)

#Time complexity
# best case = O(n^2)
# worst case = O(n^2)