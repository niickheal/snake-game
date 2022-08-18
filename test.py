platform = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]
    
size = 3
direction = 'e'
snake = [(2,3),(3,3),(4,3)]
def moveSnake(direction):
    if direction == 'e':
        snake.append((snake[-1][0]+1,snake[-1][1]))
        #print(snake)
    if direction == 'n':
        snake.append((snake[-1][0],snake[-1][1]-1))
        #print(snake)
    if direction == 's':
        snake.append((snake[-1][0],snake[-1][1]+1))
        #print(snake)
    if direction == 'w':
        snake.append((snake[-1][0]-1,snake[-1][1]))
        #print(snake)

def snakeToPlatform():
    for s in snake:
        platform[s[1]][s[0]] = 1

# moveSnake()    
# snakeToPlatform()
# for i in platform:
#     print(i)