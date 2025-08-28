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
steps = 1

unique_pos = {(p.x,p.y)}

while 0 <= p.y < height and 0 <= p.x < width:
        if((p.x,p.y) not in unique_pos):
            unique_pos.add((p.x,p.y))
        try:
            if(maze[p.y + directions[p.sign][1]][p.x + directions[p.sign][0]] == '#' and not (  p.x + directions[p.sign][0] == -1) and not (  p.y + directions[p.sign][1] == -1 )):
                p.sign = directions[p.sign][2]
                continue
        
            maze[p.y][p.x ], maze[p.y + directions[p.sign][1]][p.x + directions[p.sign][0]]  = maze[p.y + directions[p.sign][1]][p.x + directions[p.sign][0]], maze[p.y][p.x ]
            steps +=1
            p.x += directions[p.sign][0]
            p.y += directions[p.sign][1]
        except:
            break
print(len(unique_pos))