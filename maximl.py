from itertools import combinations

a=list(input())

c=0

for i in range(1,len(a)):

    perm=list(combinations(a,i))

    for j in perm:

        x=set(j)

        if c<len(x):

            c=len(x)

print(c)
