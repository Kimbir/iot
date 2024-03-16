lst = [2, 6, 43, 1, 66]
s = 0
for item in lst:
    if item % 2 == 0:
        s += 1
    else:
        continue
print(s)