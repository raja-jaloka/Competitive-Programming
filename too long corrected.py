#Way too long words (Problem 71A.Codeforces)
n=int(input())
for _ in range(n):
    x=str(input())
    if(len(x)>10):
        print(f'{x[0]}{len(x)-2}{x[-1]}')
    else:
        print(x)