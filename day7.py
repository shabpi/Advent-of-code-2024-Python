


def candidates(nums, result, length):
    if (length == 1 ):
        return nums
    list_new = candidates(nums[:-1],result,length - 1)
    return [q for x in list_new for q in (nums[-1]*x, nums[-1] + x, int(str(x) + str(nums[-1])))  if q <= result]

def is_possible(line):
    if line[0] in candidates(line[1],line[0],len(line[1])):
        return True
    else:
        return False

nums = []
with open("input.txt") as f:
    for line in f: 
        left, right = line.strip().split(':')
        nums.append(( int(left),[int(x) for x in right.strip().split(' ')]))
        

total = 0 
for line in nums:
    if(is_possible(line)):
        total += line[0]
print(total)


listo = [5,10,15,20]

print(int(str(10)+str(10)))