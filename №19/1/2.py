arr = [
      [1,3,5],
      [4,6,2],
      [7,8,9]
      ]
a = max(arr[0])
f = max(arr[1])
b = max(arr[2])

if a > f and a > b:
    print(a)
elif f > a and f > b:
    print(f)
else:
    print(b)

