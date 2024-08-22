#bubble sort
list1 = [23,45,1,7]
n = len(list1)
for i in range(n):
    for j in range(n-i-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]

#second smallest
print(list1[-2])
print(list1)