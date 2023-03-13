import pygame
import GameObject

pygame.init()

pygame.display.set_caption("Bobby: The Town of Enginerea")
pygame.display.set_icon(pygame.image.load("gameicon.png"))
backgroundImage_LvL1 = pygame.image.load('backgroundImages/lvl1background.png')
backgroundImage_LvL2 = pygame.image.load("backgroundImages/lvl2background.png")
backgroundImage_LvL3 = pygame.image.load("backgroundImages/lvl3background.png")
backgroundImage_Lvl1_rect = backgroundImage_LvL1.get_rect()
backgroundImage_LvL2_rect = backgroundImage_LvL2.get_rect()
backgroundImage_LvL3_rect = backgroundImage_LvL3.get_rect()

platForm_group = pygame.sprite.Group()
# floor platform
platForm_group.add(GameObject.PlatForms(
    0, 500, "lvl1platformImages/largebrownstone.png"))
platForm_group.add(GameObject.PlatForms(
    324, 550, "lvl1platformImages/largebrownstone.png"))
platForm_group.add(GameObject.PlatForms(
    648, 550, "lvl1platformImages/largebrownstone.png"))
platForm_group.add(GameObject.PlatForms(
    972, 550, "lvl1platformImages/largebrownstone.png"))
# orange platforms
platForm_group.add(GameObject.PlatForms(
    987, 337, "lvl1platformImages/mediumorangestone.png"))
# sky platform 1
platForm_group.add(GameObject.PlatForms(
    135, 430, "lvl1platformImages/leftcornerbrownstone.png"))
platForm_group.add(GameObject.PlatForms(
    175, 430, "lvl1platformImages/rightcornerbrownstone.png"))
# sky platform 2
platForm_group.add(GameObject.PlatForms(
    290, 360, "lvl1platformImages/leftcornerbrownstone.png"))
platForm_group.add(GameObject.PlatForms(
    330, 360, "lvl1platformImages/rightcornerbrownstone.png"))
# brown platform
platForm_group.add(GameObject.PlatForms(
    450, 446, "lvl1platformImages/smallbrownstone.png"))
platForm_group.add(GameObject.PlatForms(
    450, 350, "lvl1platformImages/smallbrownstone.png"))

screen = pygame.display.set_mode(
    (backgroundImage_Lvl1_rect.width, backgroundImage_Lvl1_rect.height))
screen_rect = screen.get_rect()

# main character
bobby = GameObject.Character(
    17, 5, 0, 425, "characterImages/bobby.png", screen)


# rendering levels
def renderLevel1():
    screen.blit(backgroundImage_LvL1, backgroundImage_Lvl1_rect)
    platForm_group.draw(screen)


def renderLvl2():
    screen.blit(backgroundImage_LvL2, backgroundImage_LvL2_rect)
    pygame.display.flip()


def renderBossLvl():
    screen.blit(backgroundImage_LvL3, backgroundImage_LvL3_rect)
    pygame.display.flip()


running = True
# gameloop1
while running:
    renderLevel1()

    pygame.time.Clock().tick(14)

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    bobby.playerMovementControl(keys)
    pygame.display.flip()


pygame.quit()
