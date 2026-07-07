# Codeforces Problem 770-A {New Password}
inp=str(input())
inp=inp.split(" ")
n=int(inp[0])
k=int(inp[1])
s='abcdefghijklmnopqrstuvwxyz'
res = ""
for i in range(n):
  res += s[i % k]
print(res)