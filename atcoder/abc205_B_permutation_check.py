n = int(input())

a = list(map(int, input().split()))

a.sort()

isPermutation = "Yes"

for i in range(1, n + 1):
    if i != a[i - 1]:
        isPermutation = "No"

print(isPermutation)
