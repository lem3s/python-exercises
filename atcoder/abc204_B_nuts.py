n = int(input())

a = list(map(int, input().split()))

res = 0

for num in a:
    if num > 10:
        res += num - 10

print(res)
