arr = [32,5,2,6,1,4,10]
n = len(arr)
for i in range(1,n):
    temp = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > temp:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = temp
print(arr)

#Time complexity 
# Best case: O(n)
# Worst case: O(n^2)
