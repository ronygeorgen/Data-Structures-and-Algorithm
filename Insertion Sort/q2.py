arr = [8,2,5,9,3,1,4]
n = len(arr)
for i in range(1,n):
    temp = arr[i]
    j = i-1
    while j >= 0 and arr[j] > temp:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = temp
print(arr)