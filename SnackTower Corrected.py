# cook your dish here
# CodeForces Problem 767-A {SnackTower}
n = int(input())
st = str(input())
st = list(map(int, st.split(" ")))
expected = n
silo = []

for i in range(n):
    silo.append(st[i])
    silo.sort(reverse=True)
    while(silo and silo[0]==expected):
        print(silo.pop(0),end=' ')
        expected-=1
    print()