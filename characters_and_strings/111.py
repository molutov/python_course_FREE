# by Bekzat
import sys
x = 0; y = 0
text = (str(sys.stdin.read()).split())
for i in range(0, len(text), 2):
    if text[i] == "North": y += int(text[i+1])
    if text[i] == "South": y -= int(text[i+1])
    if text[i] == "East": x += int(text[i+1])
    if text[i] == "West": x -= int(text[i+1])
print(x, y)
# final = open("output.txt", "a")
# final.write(x, y)
# final.close()
#
# final = open("output.txt", "r")
# print(final.read())
