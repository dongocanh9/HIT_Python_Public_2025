#bai1
from collections import Counter
a= tuple(map(int, input().split()))
b= Counter(a)
c= (x for x in b if b[x] % 5 == 0 and b[x] % 10 != 0)
print(list(c))
#bai2
a = input().split()
b = []
for x in a :
    for c in x :
        if c not in b:
            b.append(c)
print(b)
#bai3


