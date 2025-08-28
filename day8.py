import itertools

def tuple_sub(p1,p2):
    return(p1[0]-p2[0],p1[1]-p2[1])

def tuple_add(p1,p2):
    return(p1[0]+p2[0],p1[1]+p2[1])




map = []

with open("input.txt") as f:
    input = f.read()
    map = {(x, y): val for y, line in enumerate(input.split('\n'))
        for x, val in enumerate(line)}

antennas = dict()
for k in map:
    if(map[k] == '.'):
        continue
    if map[k] in antennas:
        antennas[map[k]].add(k)
    else:
        antennas[map[k]] = {k}

anitnodes_1 =set()
anitnodes_2 = set()


for frequency in antennas:
    for combination in itertools.combinations(antennas[frequency],2):

        ##combination[0] is the first antenna, call it 'u' and combination[1] is the second antenna, call it 'v':
        # treating them as vectors every combination has 2 antinodes 2u - v, and 2v - u.
        # we iterate on the whole dictionary of kinds of antennas with the positions of the antennas.
        # and check if their respective antinodes are in the map.  
        diff_vector = tuple_sub(combination[0],combination[1]) ## u - v 
        canditate = tuple_add(combination[0],diff_vector)
        if(canditate in map):
            anitnodes_1.add(canditate)
        canditate = tuple_sub(combination[1], diff_vector)
        if(canditate in map):
            anitnodes_1.add(canditate)

for frequency in antennas:
    for combination in itertools.combinations(antennas[frequency],2):

        ## as in part 1 we do the same thing, but we also check for all collinear pairs, so u take the difference vector 
        ## and iterate till you reach out of bounds, adding all points along the way.
        diff_vector = tuple_sub(combination[0],combination[1]) ## u - v 
        pivot = combination[0]
        while(pivot in map):
            anitnodes_2.add(pivot)
            map[pivot] = '#'
            pivot = tuple_add(pivot,diff_vector)

        pivot = combination[1]
        while(pivot in map):
            anitnodes_2.add(pivot)
            map[pivot] = '#'

            pivot = tuple_sub(pivot,diff_vector)

        

print(len(anitnodes_2),len(anitnodes_1))

def grid_to_string(grid):
    max_x = max(x for x, _ in grid.keys())
    max_y = max(y for _, y in grid.keys())
    lines = []
    for y in range(max_y + 1):
        line = ''.join(grid[(x, y)] for x in range(max_x + 1))
        lines.append(line)
    return '\n'.join(lines)

print(grid_to_string(map))
