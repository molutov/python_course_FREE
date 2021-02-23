# by Bekzat
string = input()
a, b = map(int, input().split()); a -= 1; b -= 1
print(string[0:a] + string[a:b+1][-1::-1] + string[b+1:])
