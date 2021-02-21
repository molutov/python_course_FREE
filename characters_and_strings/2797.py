# by Bekzat
s = input()
counter = 0
for x in s:
    if x == "0" or x == "6" or x == "9": counter += 1
    if x == "8": counter += 2
print(counter)
