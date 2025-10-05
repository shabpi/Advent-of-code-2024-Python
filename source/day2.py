def is_safe(sequence):
    """
    Returns a bool, declaring the safety of the sequence.

   :param sequence: a sequence of numbers
   :type kind: list[int]
   :return: if it's safe or not.
   :rtype: bool

    """

    length = len(sequence)
    if (length == 1): 
        return True
    if (int(sequence[0]) <= int(sequence[1])): ## Increasing case
        for i in range(0,length-1 ):
            if (int(sequence[i]) >= int(sequence[i+1]) or int(sequence[i+1]) - int(sequence[i]) > 3 ):
                return False
    else:
        for i in range(0,length -1): ## Decreasing case
            if (int(sequence[i]) <= int(sequence[i+1]) or int(sequence[i]) - int(sequence[i+1]) > 3 ):
                return False
    return True
def is_safe2(sequence):
    length = len(sequence)
    for i in range(0,length):
        if(is_safe(sequence[0:i] + sequence[i+1:])):
            return True
    return False        


sequence1 = list()


total = 0
with open("C:\Programming\python\input.txt") as f:
    for line in f:
        placeholder = line.split()
        sequence1.append(placeholder)


count = 0

for x in sequence1:
    count += 1
    total += is_safe2(x) 

print(total)



