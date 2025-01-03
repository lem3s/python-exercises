a, b, c =  map(int, input().split())
found = False

for i in range(a, b+1):
    if i % c == 0:
        print(i)
        found = True
        break

if not found:
    print(-1)
