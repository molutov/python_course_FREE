# by Bekzat
s = input()
a = int(input())
for x in s:
    if ord(x) - a < 65: print(chr(ord(x) - a + 26), end = "")
    else: print(chr(ord(x) - a), end = "")
