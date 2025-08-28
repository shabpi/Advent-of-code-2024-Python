from enum import Enum

maze = []
with open("input.txt") as f:
    for line in f: 
        maze.append(list(line.strip())) 

height = len(maze)
width = len(maze[0])


class direction(Enum):
    UPWARDS = 1
    RIGHT = 2
    DOWNWARDS = 3
    LEFT = 4

class player:
   def __init__(self, x, y, sign):
        self.x = x
        self.y = y
        self.sign = sign

directions = {'^':(0,-1,'>'),'>':(1,0,'v'),'v':(0,1,'<'), '<':(-1,0,'^')}


def find_player(data):
    for i in range(0,height):
        for j in range(0, width):
           if data[i][j] in '^>v<':
                return player(j, i, data[i][j]) 
            

p = find_player(maze)
p_og = player(p.x, p.y, p.sign)
count_stuck_loops = 0
maze_og = [row[:] for row in maze]



for row_index, row in enumerate(maze_og):
    for col_index, q in enumerate(row):
        if q in '>^<v#':
            continue
        unique_pos = set()
        maze = [row[:] for row in maze_og]
        maze[row_index][col_index] = '#'
        p = player(p_og.x, p_og.y, p_og.sign)
        while 0 <= p.y < height and 0 <= p.x < width:
            if((p.x,p.y,p.sign) not in unique_pos):
                unique_pos.add((p.x,p.y, p.sign))
            else:
                count_stuck_loops += 1
                break
            try:
                if(maze[p.y + directions[p.sign][1]][p.x + directions[p.sign][0]] == '#' and not (  p.x + directions[p.sign][0] == -1) and not (  p.y + directions[p.sign][1] == -1 )):
                    p.sign = directions[p.sign][2]
                    continue
            
                maze[p.y][p.x ], maze[p.y + directions[p.sign][1]][p.x + directions[p.sign][0]]  = maze[p.y + directions[p.sign][1]][p.x + directions[p.sign][0]], maze[p.y][p.x ]
                
                p.x += directions[p.sign][0]
                p.y += directions[p.sign][1]
            except IndexError:
                break
print(count_stuck_loops)