N = int(input())
directions = input().split(' ')
cx, cy = 0, 0

def isValid(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

def move(direction):
    global cx, cy
    nx, ny = cx, cy
    if direction == 'U':
        ny -= 1
    elif direction == 'D':
        ny += 1
    elif direction == 'L':
        nx -= 1
    elif direction == 'R':
        nx += 1
        
    if isValid(nx, ny):
        cx, cy = nx, ny

for direction in directions:
    move(direction)
    
print(cy + 1, cx + 1)