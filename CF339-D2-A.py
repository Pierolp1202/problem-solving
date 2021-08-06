w=input()

arr = w.split("+")
arr = list(map(int,arr))
arr.sort()
arr = list(map(str,arr))
res = "+".join(arr)
print(res)