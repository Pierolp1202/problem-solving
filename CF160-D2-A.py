w = int(input())
values = list(map(int,input().split()))
# values = []

# for i in range(w):
#     values.append(int(input()))

values = sorted(values, reverse=True)
sum_values = sum(values)
count = 0
sum_bro = 0

for x in values:
    sum_bro += x
    count+=1
    if sum_bro > (sum_values/2):
        break
   
print(count)