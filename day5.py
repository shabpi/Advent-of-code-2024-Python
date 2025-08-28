

rules = []
data = []
Flag = True
with open("input.txt") as f:
    for line in f:
        if(line == "\n"):
            Flag = False
            continue
        if(Flag):
            rules.append(line.strip("\n").split('|'))
            continue
        data.append(line.strip("\n").split(','))
    
dic = dict()

for pair in rules:
    if pair[0] not in dic:
        dic[pair[0]] = {pair[1]}
    else:
        dic[pair[0]].add(pair[1])


middle_values_1 = []
inds_wrong = []

number_sequences = len(data)
for k in range(0,number_sequences):
    is_okay = True  
    length = len(data[k])
    for i in range(0,length):
        for j in range(0, i):
            if(data[k][j] in dic[data[k][i]]):
                is_okay = False
                inds_wrong.append(k)
                break 
        if(not is_okay):
            break   
    if(is_okay):
        middle_values_1.append(data[k][int(length/2)])

total_1 = 0

for k in middle_values_1:
    total_1 += int(k)

## Now part 2 of day 5, ordering the sequences first and then finding the middle value.
middle_values_2 = []
for k in inds_wrong:
    length = len(data[k])
    i = 0


    while (i < length):
        for j in range(0, i):
            if(data[k][j] in dic[data[k][i]]):
                data[k][j], data[k][i] = data[k][i], data[k][j]
                i = j - 1 
                
                break
            
        i += 1
    middle_values_2.append(data[k][int(length/2)])


total2 = 0 
for k in middle_values_2:
    total2 += int(k)
print(total_1, total2)

print(middle_values_2)
print(data)
print(inds_wrong)