# by Bekzat
try:
    s = [int(i) for i in input().split(".")]
    a = [i for i in s if i >= 0 and i <= 255]
    print(1) if len(s) == len(a) else print(0)
except:
    print(0)
