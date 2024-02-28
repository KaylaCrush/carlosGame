import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
BLACK = (0, 0, 0)
SPRITE_SCALE = 1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Kill', False, (0, 0, 0))



x = 50
y = SCREEN_HEIGHT - 70
width = 64
height = 64
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount

    screen.blit(bg, (0,0))


    pygame.draw.rect(screen, (255,0,0),(20,25,45,25))
    screen.blit(text_surface, (20,20))

    if walkCount + 1 >= 27:
        walkCount = 0

    if isJump:
        if left:
            screen.blit(jumpLeft,(x,y))
        elif right:
            screen.blit(jumpRight,(x,y))
        else:
            screen.blit(jump,(x,y))

    elif left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        screen.blit(stand, (x, y))
        walkCount = 0

    pygame.display.update()



run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - vel - width:
        x += vel
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()

pygame.quit()
