a = int(input())
b = [int(i) for i in input().split()]
c = list(set(b))
c.sort(reverse=True)
print(c[1])