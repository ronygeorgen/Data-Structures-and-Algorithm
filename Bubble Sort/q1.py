arr = [2,5,1,6,3,66,23]
n = len(arr)
for i in range(n-1):
    flag = 0
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            flag = 1
    if flag == 0:
        break
print(arr)