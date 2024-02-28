import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
BLACK = (0, 0, 0)
SPRITE_SCALE = 1

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Carlos Game")

sprite_sheet_image = pygame.image.load('images/carlos_sprites.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

walkRight = [sprite_sheet.get_image(11, i, SPRITE_SCALE, BLACK) for i in range(9)]
walkLeft = [sprite_sheet.get_image(9, i, SPRITE_SCALE, BLACK) for i in range(9)]
stand = sprite_sheet.get_image(2, 0, SPRITE_SCALE, BLACK)
jumpRight = sprite_sheet.get_image(3,5, SPRITE_SCALE,BLACK)
jumpLeft = sprite_sheet.get_image(1,5, SPRITE_SCALE,BLACK)
jump = sprite_sheet.get_image(2,5, SPRITE_SCALE,BLACK)

bg = pygame.image.load("images/school.jpg")

clock = pygame.time.Clock()


class chavez(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(stand, (self.x,self.y))



def redrawGameWindow():
    win.blit(bg, (0,0))
    carlos.draw(win)

    pygame.display.update()


#mainloop
carlos = chavez(200, 410, 64,64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and carlos.x > carlos.vel:
        carlos.x -= carlos.vel
        carlos.left = True
        carlos.right = False
    elif keys[pygame.K_RIGHT] and carlos.x < 500 - carlos.width - carlos.vel:
        carlos.x += carlos.vel
        carlos.right = True
        carlos.left = False
    else:
        carlos.right = False
        carlos.left = False
        carlos.walkCount = 0

    if not(carlos.isJump):
        if keys[pygame.K_SPACE]:
            carlos.isJump = True
            carlos.right = False
            carlos.left = False
            carlos.walkCount = 0
    else:
        if carlos.jumpCount >= -10:
            neg = 1
            if carlos.jumpCount < 0:
                neg = -1
            carlos.y -= (carlos.jumpCount ** 2) * 0.5 * neg
            carlos.jumpCount -= 1
        else:
            carlos.isJump = False
            carlos.jumpCount = 10

    redrawGameWindow()

pygame.quit()
