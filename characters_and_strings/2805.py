import re
def to_binary(string):
    number = int(string)
    result = ""
    while number > 0:
        result += str(number % 2)
        number //= 2
    result = result[-1::-1]
    return result
# beginning
string = input()
list = re.findall(r"\d+", string)
list = [int(i) for i in list]
list = sorted(list, reverse = True)
list = [str(i) for i in list]
# print(list)
# exit()
for item in list:
    changed = to_binary(item)
    string = string.replace(item, changed)
print(string)
