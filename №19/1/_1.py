arr = [1,2,6,7]
while len(arr):
    print(min(arr), end='')
    arr.remove(min(arr))
arr = [1,2,6,7]
print("")
while len(arr):
    print(max(arr), end='')
    arr.remove(max(arr))