T = int(input())

for _ in range(T):
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(a[2])