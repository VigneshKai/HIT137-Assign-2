import pygame

pygame.init()

win = pygame.display.set_mode((800,600))
pygame.display.set_caption("first game")

x = 50
y = 50
width = 40
height = 60
vol = 5

run = True
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			run = False
	pygame.draw.rect(win,(255,0,0), (x, y, width, height))
	pygame.display.update()
pygame.quit()

