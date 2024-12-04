import re

mul = []
with open('input_day3.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        mul.append(re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", line))


# print(mul)
is_enbaled = False
sum = 0
l=0
for j in mul:
    for t in j:
        if t == "do()":
            is_enbaled = False
            continue
        elif t == "don't()":
            is_enbaled = True
            continue
        elif is_enbaled:
            continue
        else:
            l+=1
            x,y = map(int, re.findall(r"\d+", t))
            sum += x * y
print(sum)  
print(l)