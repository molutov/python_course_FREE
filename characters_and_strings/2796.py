# by Bekzat
first, sign = [int(i) for i in input().split()]
string = str(first)
for j in range(sign - 1):
    final = ""
    counter = 1
    char = string[0]
    for i in range(1, len(string)):
        if string[i] != char:
            final += str(counter)
            final += char
            char = string[i]
            counter = 1
        else:
            counter += 1
    final += str(counter)
    final += char
    string = final
print(string)
