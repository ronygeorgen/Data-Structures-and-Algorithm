arr = [11, 33, 2, 4, 5]
n = len(arr)
for i in range(n-1):
    flag = 0
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            flag = 1
    if flag ==0:
        break
print(arr)