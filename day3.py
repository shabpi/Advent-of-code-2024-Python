import re

with open("C:\Programming\python\input.txt") as f:
    data = f.read()
parts = data.split('do')
disabled_muls = []
total_disabled = 0
for part in parts:
    if(part[0:3] == "n't"):
        disabled_muls.append(re.findall(r"mul[(](\d+),(\d+)[)]",part)) 
for list in disabled_muls:
    for x in list:
        total_disabled += -1*int(x[0])*int(x[1])


muls = re.findall(r"mul[(](\d+),(\d+)[)]",data)
total = 0

for tuple in muls:
    total += int(tuple[0])*int(tuple[1])
print(parts)
print(total)
print(total + total_disabled)
print(disabled_muls)