def is_safe(list):
    length = len(list)
    if (length == 1): 
        return True
    if (int(list[0]) <= int(list[1])): ## Increasing case
        for i in range(0,length-1 ):
            if (int(list[i]) >= int(list[i+1]) or int(list[i+1]) - int(list[i]) > 3 ):
                return False
    else:
        for i in range(0,length -1): ## Decreasing case
            if (int(list[i]) <= int(list[i+1]) or int(list[i]) - int(list[i+1]) > 3 ):
                return False
    return True
def is_safe2(list):
    length = len(list)
    for i in range(0,length):
        if(is_safe(list[0:i] + list[i+1:])):
            return True
    return False        


list1 = list()


total = 0
with open("C:\Programming\python\input.txt") as f:
    for line in f:
        placeholder = line.split()
        list1.append(placeholder)


count = 0

for x in list1:
    count += 1
    total += is_safe2(x) 

print(total)



