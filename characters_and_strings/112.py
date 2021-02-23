# by Bekzat
s = input().replace(" ", "")
print("yes") if s[0::1] == s[-1::-1] else print("no")
