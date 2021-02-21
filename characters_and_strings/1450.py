#by Bekzat
def is_pal(s):
    if s[0::1] == s[-1::-1]: return True
    else: return False
s = input()
max_len = 0
for i in range(0, len(s)):
    length = len(s)
    for j in range(1, length + 1):
        trial = s[i:i+j]
        if is_pal(trial) and len(trial) > max_len:
            max_pal = trial
            max_len = len(trial)
print(max_pal)
