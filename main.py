import pygame
import time
#from test import moveSnake,snakeToPlatform,platform,direction
import random
  
# Initializing Pygame
pygame.init()

clock = pygame.time.Clock()

  
# Initializing surface
surface = pygame.display.set_mode((300,300))
text = pygame.display.set_caption('Sahil Game')
Font=pygame.font.SysFont('timesnewroman',  20)

  
# Initialing Color
color = (145,145,145)
black = (0,0,0)
# letter1=Font.render("Score:", True, (255,0,0))
# score_txt = surface.blit(letter1,(150,0))
# score_txt.txt = str("nikhil")
# score_txt.update()
# Drawing Rectangle



direction = 'e'
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
snake = [(2,3),(3,3),(4,3)]
food = ()
global score
score = 0


def moveSnake(direction,snake,food):
	if direction == 'e':
		if snake[-1][0]+1 >= len(platform[0]):
			snake.append((0,snake[-1][1]))
		else:
			snake.append((snake[-1][0]+1,snake[-1][1]))
		
	if direction == 'n':
		if snake[-1][1]-1 < 0:
			snake.append((snake[-1][0],len(platform[0])))
		else:
			snake.append((snake[-1][0],snake[-1][1]-1))

	if direction == 's':
		if snake[-1][1]+1 >= len(platform):
			snake.append((snake[-1][0],0))
		else:
			snake.append((snake[-1][0],snake[-1][1]+1))

	if direction == 'w':
		if snake[-1][0]-1 < 0:
			snake.append((len(platform[0])-1,snake[-1][1]))
		else:
			snake.append((snake[-1][0]-1,snake[-1][1]))
	if snake[0] != food :
		del snake[0]
		return food
	else:
		global score
		score += 100
		return generateFood(platform)
        #print(snake)

def snakeToPlatform(platform,snake,food):
	for s in snake:
		platform[s[1]][s[0]] = 1

	if food not in snake:
		platform[food[1]][food[0]] = 2

def generateFood(platform):
	return (random.randint(0,len(platform)-1),random.randint(0,len(platform[0])-1))


def drawPlatForm(platform):
	row = 10
	count =10
	x = 5
	y = 10
	color = (255,0,0)
	for r in platform:
		for c in r:
			if c == 1:
				color = (0, 36, 181)
			elif c == 2:
				color = (0,255,0)
			else:
				color = (255,0,0)
			pygame.draw.rect(surface, color, pygame.Rect(x, y, 10, 10))
			pygame.display.flip()
			x += 15
		y += 15
		x = 5

running = True
direction = 'e'
food = generateFood(platform)
while running:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				direction = 'n'
				#moveSnake(direction,snake)
			if event.key == pygame.K_DOWN:
				direction = 's'
				#moveSnake(direction,snake)
			if event.key == pygame.K_RIGHT:
				direction = 'e'
				#moveSnake(direction,snake)
			if event.key == pygame.K_LEFT:
				direction = 'w'
				#moveSnake(direction,snake)
		if event.type == pygame.QUIT:
			running = False
		if running == False:
			pygame.quit()
	snakeToPlatform(platform,snake,food)
	food = moveSnake(direction,snake,food)
	drawPlatForm(platform)
	print('Score:',score)
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

	time.sleep(0.5)
    # fpsClock.tick(FPS)
