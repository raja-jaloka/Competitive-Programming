#Codeforces Problem 490-A {Team Olympiad}
n=int(input()) #No. of students in the school 
s=input().split(" ")

t1_list = []
t2_list = []
t3_list = []

for i in range(n):
  if s[i] == '1':
    t1_list.append(i + 1)
  elif s[i] == '2':
    t2_list.append(i + 1)
  else:
    t3_list.append(i + 1)

team_count = min(len(t1_list), len(t2_list), len(t3_list))
print(team_count)

for i in range(team_count):
  print(t1_list[i], t2_list[i], t3_list[i])