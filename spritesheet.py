import pygame
SPRITE_WIDTH = 64
SPRITE_HEIGHT = 64

class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, x, y, scale, color = (0,0,0)):
		image = pygame.Surface((SPRITE_WIDTH, SPRITE_HEIGHT)).convert_alpha()
		rect = ((y*SPRITE_HEIGHT), (x*SPRITE_WIDTH), ((y+1)*SPRITE_WIDTH), ((x+1)*SPRITE_HEIGHT))
		image.blit(self.sheet, (0, 0), rect)
		image = pygame.transform.scale(image, (SPRITE_WIDTH * scale, SPRITE_HEIGHT * scale))
		image.set_colorkey(color)

		return image
