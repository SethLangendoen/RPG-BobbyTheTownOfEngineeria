import pygame
import GameObject
import Shop
import death
startGame = True
while startGame:
    pygame.init()
    # --------------------------------------------------------------------------------------------------
    # ------------------------------------ SCREEN INITIALIZATION ---------------------------------------
    # --------------------------------------------------------------------------------------------------
    # set up images and icons
    pygame.display.set_caption("Main Menu")
    pygame.display.set_icon(pygame.image.load("mainScreenImages/gameicon.png"))

    # main screen background 
    mainScreenImage = pygame.image.load('mainScreenImages/main.png'); 
    mainScreenImageRect = mainScreenImage.get_rect()
    # level 1 background
    backgroundImage_LvL1 = pygame.image.load('backgroundImages/lvl1background.png')
    backgroundImage_Lvl1_rect = backgroundImage_LvL1.get_rect()
    # level 2 background
    backgroundImage_LvL2 = pygame.image.load("backgroundImages/lvl2background.png")
    backgroundImage_LvL2_rect = backgroundImage_LvL2.get_rect()
    # level 3 background
    backgroundImage_LvL3 = pygame.image.load("backgroundImages/lvl3background.png")
    backgroundImage_LvL3_rect = backgroundImage_LvL3.get_rect()
    # set size of window screen
    screen = pygame.display.set_mode((1200, 575))
    screen_rect = screen.get_rect()

    # --------------------------------------------------------------------------------------------------
    # ------------------------------------ LEVEL ONE PLATFORMS -----------------------------------------
    # --------------------------------------------------------------------------------------------------
    # floor layout for level 1 (SPRITE GROUPS)
    platForm_group1 = pygame.sprite.Group()
    platForm_floor1 = pygame.sprite.Group()
    movingPlatform_group1 = pygame.sprite.Group()
    lavapool1 = pygame.sprite.Group()
    vertMovingPlatform_group1 = pygame.sprite.Group()

    # orange floor platform
    platForm_floor1.add(GameObject.PlatForms(987, 337, "lvl1platformImages/largeorangestone.png"))
    # brown floor platforms
    platForm_floor1.add(GameObject.PlatForms(0, 480, "lvl1platformImages/largebrownstone.png"))
    platForm_floor1.add(GameObject.PlatForms(324, 550, "lvl1platformImages/largebrownstone.png"))
    platForm_floor1.add(GameObject.PlatForms(648, 550, "lvl1platformImages/largebrownstone.png"))
    platForm_floor1.add(GameObject.PlatForms(972, 550, "lvl1platformImages/largebrownstone.png"))
    # brown pillar
    platForm_floor1.add(GameObject.PlatForms(500, 350, "lvl1platformImages/brownpillar.png"))
    # sky platform 1
    platForm_group1.add(GameObject.PlatForms(380, 420, "lvl1platformImages/orangeplatform.png"))
    # sky platform 2
    platForm_group1.add(GameObject.PlatForms(520, 250, "lvl1platformImages/brownplatform.png"))
    # sky platform 3
    platForm_group1.add(GameObject.PlatForms(680, 350, "lvl1platformImages/orangeplatform.png"))
    # sky platform 4
    platForm_group1.add(GameObject.PlatForms(850, 370, "lvl1platformImages/orangeplatform.png"))
    # moving sky platform
    movingPlatform_group1.add(GameObject.MovingPlatForms(720, 470, 3, 600, 900, "lvl1platformImages/brownplatform.png"))
    # left sky flat platform
    platForm_group1.add(GameObject.PlatForms(10, 190, "lvl1platformImages/leftskyplatform.png"))
    # right sky flat platform
    platForm_group1.add(GameObject.PlatForms(640, 180, "lvl1platformImages/rightskyplatform.png"))
    # left side border brown stone for collisions
    platForm_floor1.add(GameObject.PlatForms(-6, -5,"lvl1platformImages/brownborderplatform.png"))
    platForm_floor1.add(GameObject.PlatForms(-6, 235,"lvl1platformImages/brownborderplatform.png"))
    # right side border brown stone for collisions
    platForm_floor1.add(GameObject.PlatForms(1175, -40, "lvl1platformImages/brownborderplatform.png"))
    platForm_floor1.add(GameObject.PlatForms(1175, 190, "lvl1platformImages/brownborderplatform.png"))
    platForm_floor1.add(GameObject.PlatForms(1175, 431, "lvl1platformImages/brownborderplatform.png"))
    # top side border brown stone for collisions
    platForm_floor1.add(GameObject.PlatForms(0, 0, "lvl1platformImages/brownflatplatform.png"))
    platForm_floor1.add(GameObject.PlatForms(137, 0, "lvl1platformImages/brownflatplatform.png"))
    platForm_floor1.add(GameObject.PlatForms(274, 0, "lvl1platformImages/brownflatplatform.png"))
    platForm_floor1.add(GameObject.PlatForms(411, 0, "lvl1platformImages/brownflatplatform.png"))
    platForm_floor1.add(GameObject.PlatForms(548, 0, "lvl1platformImages/brownflatplatform.png"))
    platForm_floor1.add(GameObject.PlatForms(685, 0, "lvl1platformImages/brownflatplatform.png"))
    platForm_floor1.add(GameObject.PlatForms(822, 0, "lvl1platformImages/brownflatplatform.png"))
    platForm_floor1.add(GameObject.PlatForms(959, 0, "lvl1platformImages/brownflatplatform.png"))
    platForm_floor1.add(GameObject.PlatForms(1096, 0, "lvl1platformImages/brownflatplatform.png"))
    # lavapools
    lavapool1.add(GameObject.LavaPool(320, 530, "lvl1platformImages/lava.png"))
    lavapool1.add(GameObject.LavaPool(462, 530, "lvl1platformImages/lava.png"))
    lavapool1.add(GameObject.LavaPool(605, 530, "lvl1platformImages/lava.png"))
    lavapool1.add(GameObject.LavaPool(747, 530, "lvl1platformImages/lava.png"))
    lavapool1.add(GameObject.LavaPool(889, 530, "lvl1platformImages/lava.png"))
    # aesthetic images
    destroyedbuilding1 = pygame.image.load("lvl1platformImages/destroyedbuilding1.png")
    destroyedbuilding2 = pygame.image.load("lvl1platformImages/destroyedbuilding2.png")
    destroyedbuilding3 = pygame.image.load("lvl1platformImages/destroyedbuilding3.png")
    destroyedbuilding4 = pygame.image.load("lvl1platformImages/destroyedbuilding4.png")
    destroyedcar = pygame.image.load("lvl1platformImages/destroyedcar.png")
    tree = pygame.image.load("lvl1platformImages/deadtree.png")

    # --------------------------------------------------------------------------------------------------
    # ------------------------------------ LEVEL TWO PLATFORMS -----------------------------------------
    # --------------------------------------------------------------------------------------------------
    # floor layout for level 2 (SPRITE GROUPS)
    platForm_group2 = pygame.sprite.Group()
    platForm_floor2 = pygame.sprite.Group()
    movingPlatform_group2 = pygame.sprite.Group()
    vertMovingPlatform_group2 = pygame.sprite.Group()

    # snow floor platforms
    platForm_floor2.add(GameObject.PlatForms(0, 470, "lvl2platformImages/largeplatform.png"))
    platForm_floor2.add(GameObject.PlatForms(324, 500, "lvl2platformImages/largeplatform.png"))
    platForm_floor2.add(GameObject.PlatForms(648, 500, "lvl2platformImages/largeplatform.png"))
    platForm_floor2.add(GameObject.PlatForms(972, 350, "lvl2platformImages/largeplatform.png"))
    # moving up and down platform
    vertMovingPlatform_group2.add(GameObject.VertMovingPlatForms(820,450,2,100,450, "lvl1platformImages/brownplatform.png"))
    # platform for middle chest
    platForm_floor2.add(GameObject.PlatForms(560, 130, "lvl2platformImages/iceplatform.png"))
    # platform for chest 
    platForm_floor2.add(GameObject.PlatForms(1000, 160, "lvl2platformImages/iceplatform.png"))
    # enemy platform
    platForm_floor2.add(GameObject.PlatForms(24, 280, "lvl2platformImages/iceplatform.png"))
    platForm_floor2.add(GameObject.PlatForms(174, 280, "lvl2platformImages/iceplatform.png"))
    platForm_floor2.add(GameObject.PlatForms(324, 280, "lvl2platformImages/iceplatform.png"))
    platForm_floor2.add(GameObject.PlatForms(474, 280, "lvl2platformImages/iceplatform.png"))
    platForm_floor2.add(GameObject.PlatForms(624, 280, "lvl2platformImages/iceplatform.png"))
    # left side border platforms (from bottom to top)
    platForm_floor2.add(GameObject.PlatForms(-5, 320, "lvl2platformImages/sideborderplatforms.png"))
    platForm_floor2.add(GameObject.PlatForms(-5, 40, "lvl2platformImages/sideborderplatforms.png"))
    platForm_floor2.add(GameObject.PlatForms(-5, -225, "lvl2platformImages/sideborderplatforms.png"))
    # right side border platforms (from bottom to top)
    platForm_floor2.add(GameObject.PlatForms(1175, 350, "lvl2platformImages/sideborderplatforms.png"))
    platForm_floor2.add(GameObject.PlatForms(1175, 40, "lvl2platformImages/sideborderplatforms.png"))
    platForm_floor2.add(GameObject.PlatForms(1175, -230, "lvl2platformImages/sideborderplatforms.png"))
    # top side border brown stone for collisions
    platForm_floor2.add(GameObject.PlatForms(0, 0, "lvl2platformImages/borderplatform.png"))
    platForm_floor2.add(GameObject.PlatForms(137, 0, "lvl2platformImages/borderplatform.png"))
    platForm_floor2.add(GameObject.PlatForms(274, 0, "lvl2platformImages/borderplatform.png"))
    platForm_floor2.add(GameObject.PlatForms(411, 0, "lvl2platformImages/borderplatform.png"))
    platForm_floor2.add(GameObject.PlatForms(548, 0, "lvl2platformImages/borderplatform.png"))
    platForm_floor2.add(GameObject.PlatForms(685, 0, "lvl2platformImages/borderplatform.png"))
    platForm_floor2.add(GameObject.PlatForms(822, 0, "lvl2platformImages/borderplatform.png"))
    platForm_floor2.add(GameObject.PlatForms(959, 0, "lvl2platformImages/borderplatform.png"))
    platForm_floor2.add(GameObject.PlatForms(1096, 0, "lvl2platformImages/borderplatform.png"))

    # --------------------------------------------------------------------------------------------------
    # ------------------------------------ LEVEL THREE PLATFORMS ---------------------------------------
    # --------------------------------------------------------------------------------------------------
    platForm_floor3 = pygame.sprite.Group()
    platForm_group3 = pygame.sprite.Group()
    movingPlatform_group3 = pygame.sprite.Group()
    vertMovingPlatform_group3 = pygame.sprite.Group()

    platForm_floor3.add(GameObject.PlatForms(-10,470,"lvl3platFormImages/startingPlatForm.png"))
    platForm_floor3.add(GameObject.PlatForms(0,150,"lvl3platFormImages/level3MediumPlatForm.png"))
    platForm_floor3.add(GameObject.PlatForms(930,150,"lvl3platFormImages/BossPlatForm.png"))
    platForm_floor3.add(GameObject.PlatForms(-5,300,"lvl3platFormImages/level3MediumPlatForm.png"))
    movingPlatform_group3.add(GameObject.MovingPlatForms(215,470,3,215,850,"lvl3platFormImages/Level3Floating.png"))

    # --------------------------------------------------------------------------------------------------
    # ------------------------------------ BOBBY INITIALIZATION ----------------------------------------
    # --------------------------------------------------------------------------------------------------
    # Main Character (BOBBY) (speed, health, armour, x, y, image, screen, plat1, plat2)
    bobby = GameObject.Character(5, 10, 0, 75, 380, "Axe1/axe1R.png", screen, platForm_group1, platForm_floor1, movingPlatform_group1, vertMovingPlatform_group1)
    # bullet group 
    bullet_group = pygame.sprite.Group()
    bulletcooldown = 0
    # bobby axe throw sound effect
    bobbythrow = pygame.mixer.Sound("SoundEffects/axeThrow.mp3")

    # --------------------------------------------------------------------------------------------------
    # ------------------------------------ SOUND EFFECTS INITIALIZATION --------------------------------
    # --------------------------------------------------------------------------------------------------
    # coin collected
    collected = pygame.mixer.Sound("SoundEffects/collectedCoin.mp3")
    collected.set_volume(0.5)
    # treasure collected
    chestcollected = pygame.mixer.Sound("SoundEffects/chestOpenSound.mp3")
    chestcollected.set_volume(0.5)
    # key collected 
    keyCollected = pygame.mixer.Sound("SoundEffects/keyGrab.mp3")
    keyCollected.set_volume(0.5)
    # enemy hit sound effect
    enemyHitSound = pygame.mixer.Sound("SoundEffects/enemyHitSound.mp3")
    enemyHitSound.set_volume(0.2)
    # door open sound
    doorOpen = pygame.mixer.Sound("SoundEffects/doorOpen.mp3")
    doorOpen.set_volume(0.5)
    # death sound 
    lost = pygame.mixer.Sound("SoundEffects/deathSound.mp3")
    lost.set_volume(5)

    # --------------------------------------------------------------------------------------------------
    # ------------------------------------ ENEMIES INITIALIZATION --------------------------------------
    # --------------------------------------------------------------------------------------------------
    # enemy bullet group
    enemy_bullets1 = pygame.sprite.Group()
    # enemy coin 
    coins1 = pygame.sprite.Group()
    # initialize level 1 Enemy Groups
    enemies1 = pygame.sprite.Group()
    enemies1.add(GameObject.Enemy(385, 334, screen, enemy_bullets1, "level1", coins1))
    enemies1.add(GameObject.Enemy(855, 284, screen, enemy_bullets1, "level1", coins1))
    enemies1.add(GameObject.Enemy(900, 94, screen, enemy_bullets1, "level1", coins1))
    enemies1.add(GameObject.Enemy(90, 44, screen, enemy_bullets1, "level1", coins1))

    # initialize level 2 Enemy Groups
    enemies2 = pygame.sprite.Group()
    # --------------------------------------------------------------------------------------------------
    # ------------------------------------ SHOP INITIALIZATION -----------------------------------------
    # --------------------------------------------------------------------------------------------------
    shop = Shop.Shop(screen,bobby)

    # --------------------------------------------------------------------------------------------------
    # ------------------------------------ RENDER HELP SCREEN ------------------------------------------
    # --------------------------------------------------------------------------------------------------
    def renderHelpScreen():
        help = True
        screen.fill((255,255,255))

        titles = pygame.font.Font("Fonts/Stats.ttf",25)
        texts = pygame.font.Font("Fonts/Stats.ttf",15)

        title1 = titles.render("Storyline", True, (0, 0, 0))
        title2 = titles.render("Game Controls", True, (0, 0, 0))

        text1 = "In the town of Enginerea, where people are destined to become master builders, there lived a man named Bobby the Builder."
        text2 = "From an early age, Bobby had a passion for building and designing. He spent countless years perfecting his craft and "
        text3 = "becoming the Supreme Builder of the town. One day, a terrible earthquake struck Enginerea resulting in severe damage to "
        text4 = "many of the town buildings including the Town hall. It is the job of the Supreme Builder to rebuild the town hall to "
        text5 = "its former glory. However, in his endeavor to rebuild the town hall, he must face-off against countless other master "
        text6 = "builders who want to take the title of the Supreme Builder."

        rendered_text1 = texts.render(text1, True, (0, 0, 0))
        rendered_text2 = texts.render(text2, True, (0, 0, 0))
        rendered_text3 = texts.render(text3, True, (0, 0, 0))
        rendered_text4 = texts.render(text4, True, (0, 0, 0))
        rendered_text5 = texts.render(text5, True, (0, 0, 0))
        rendered_text6 = texts.render(text6, True, (0, 0, 0))
        gcText1 = texts.render("[LEFT ARROW KEY] player moves left",True,(0,0,0))
        gcText2 = texts.render("[RIGHT ARROW KEY] player moves right",True,(0,0,0))
        gcText3 = texts.render("[UP ARROW KEY] player jumps",True,(0,0,0))
        gcText4 = texts.render("[SPACE BAR] player shoots an axe",True,(0,0,0))
        gcText5 = texts.render("[P KEY] open shop menu",True,(0,0,0))

        screen.blit(title1, (40, 40))
        screen.blit(title2, (40, 300))


        screen.blit(rendered_text1, (40, 100))
        screen.blit(rendered_text2, (40, 120))
        screen.blit(rendered_text3, (40, 140))
        screen.blit(rendered_text4, (40, 160))
        screen.blit(rendered_text5, (40, 180))
        screen.blit(rendered_text6, (40, 200))

        screen.blit(gcText1, (40, 360))
        screen.blit(gcText2, (40, 380))
        screen.blit(gcText3, (40, 400))
        screen.blit(gcText4, (40, 420))
        screen.blit(gcText5, (40, 440))



        while help:
            pygame.display.set_caption("Help")
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(-1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    help = False

            pygame.display.flip()

    # --------------------------------------------------------------------------------------------------
    # ------------------------------------ RENDER MAIN SCREEN ------------------------------------------
    # --------------------------------------------------------------------------------------------------
    # mainScreenRender
    fontForMainScreen = pygame.font.Font("Fonts/mainScreen.ttf",50)
    Title = fontForMainScreen.render("Bobby: The Town of Enginerea",True,(255,255,255))
    playBtn = GameObject.GameObject(510,200,"mainScreenImages/playbutton.png")
    exitBtn = GameObject.GameObject(510,260,"mainScreenImages/exitbutton.png")
    helpBtn = GameObject.GameObject(510,320,"mainScreenImages/helpbutton.png")
    playBtnImage = pygame.image.load("mainScreenImages/playbutton.png")
    exitBtnImage = pygame.image.load("mainScreenImages/exitbutton.png")
    helpBtnImage = pygame.image.load("mainScreenImages/helpbutton.png")
    mainScreen = True
    sb = GameObject.SpeechBubble(bobby.rect.x, bobby.rect.y, bobby, screen)
    # mainScreen Music
    pygame.display.set_caption("Main Menu")
    pygame.mixer.init()
    pygame.mixer.music.load("GameMusic/mainScreenMusic.mp3")
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)

    # rendering the main screen
    def renderMainScreen():
        global mainScreen
        while mainScreen:
            pygame.display.set_caption("Main Menu")
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(-1)

            screen.blit(mainScreenImage,mainScreenImageRect)
            screen.blit(Title, (180,55))
            screen.blit(playBtnImage, (510,200))
            screen.blit(exitBtnImage, (510,260))
            screen.blit(helpBtnImage, (505,320))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and playBtn.rect.collidepoint(event.pos): 
                    pygame.mixer.music.stop()
                    pygame.time.delay(200)
                    pygame.mixer.music.load("GameMusic/level1music.mp3")
                    mainScreen = False
                if event.type == pygame.MOUSEBUTTONDOWN and exitBtn.rect.collidepoint(event.pos): 
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and helpBtn.rect.collidepoint(event.pos): 
                    # place the render help here. 
                    renderHelpScreen()

    # --------------------------------------------------------------------------------------------------
    # ------------------------------------ OTHER INITIALIZATION ----------------------------------------
    # --------------------------------------------------------------------------------------------------
    # death screen stuff
    die = death.Death(screen,bobby)
    startTime = pygame.time.get_ticks()

    numberOfKeys=[]

    # instructions to move 
    playDialogue1 = True
    # instructions to defeat enemies 
    playDialogue2 = True
    # says "Good Work!"
    playDialogue3 = True
    # instructions to open shop 
    playDialogue4 = True
    playDialogue5 = True
    dialogueClock = 0

    #--------------------------------------------------------------------------------------------------
    #------------------------------------ RENDER LEVEL 1 ----------------------------------------------
    #--------------------------------------------------------------------------------------------------
    # LEVEL 1 CHESTS AND KEYS 
    # door initialization
    doorOpenRect = GameObject.GameObject(1040,237,"lvl1platformImages/doorOpen.png")
    doorClosedImage = pygame.image.load("lvl1platformImages/doorClosed.png")
    doorOpenImage = pygame.image.load("lvl1platformImages/doorOpen.png")
    # chest and key initialization
    chestOpenImage =  GameObject.GameObject(1090,127,"chestImages/openedChest.png")
    chestClosedImage = GameObject.GameObject(1090,137,"chestImages/closedChest.png")
    chestKeyRect = GameObject.GameObject(120,150,"chestImages/chestKey.png")
    chestKeyImage = GameObject.GameObject(120,150,"chestImages/chestKey.png")
    # boolean functions 
    Level1keyAlive = True
    Level1ChestAlive = True
    Level1 = True
    # render level 1 
    def renderLevel1():
        if Level1:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(-1)

            pygame.display.set_caption("Bobby: The Town of Enginerea | LEVEL 1")
            numberOfKeys.append(chestKeyImage)
            screen.blit(backgroundImage_LvL1, backgroundImage_Lvl1_rect)
            screen.blit(destroyedbuilding1, (35,165)) # next to booby
            screen.blit(destroyedbuilding2, (625,-135)) # top right corner 
            screen.blit(destroyedbuilding3, (335,450)) # in the lava 
            screen.blit(destroyedbuilding4, (30,-209)) # top left corner 
            screen.blit(destroyedcar, (23,88)) # car image on left sky platform
            screen.blit(tree, (160,302))
            screen.blit(tree, (700,15))
            
            # if there are chests 
            if Level1ChestAlive:
                screen.blit(chestClosedImage.image,chestClosedImage.rect)
            # if there are no enemies, open the chest 
            elif len(enemies1)==0:
                screen.blit(chestOpenImage.image,chestOpenImage.rect)
            
            # if there are keys 
            if Level1keyAlive:
                screen.blit(chestKeyImage.image, chestKeyImage.rect)
            
            lavapool1.draw(screen)
            platForm_group1.draw(screen)
            platForm_floor1.draw(screen)
            screen.blit(doorClosedImage, (1040, 237))
            movingPlatform_group1.update()
            movingPlatform_group1.draw(screen)
            for enemy in enemies1:
                enemy.handleBehaviour(bobby)
            for coin in coins1:
                coin.animate()
            for bullet in bullet_group:
                bullet.bulletTravel()
            for bullet in enemy_bullets1:
                bullet.bulletHoming(bobby)
        else:
            print("function is false")

    # --------------------------------------------------------------------------------------------------
    # ------------------------------------ RENDER LEVEL 2 ----------------------------------------------
    # --------------------------------------------------------------------------------------------------
    # LEVEL 2 CHEST AND KEYS 
    # door initialization
    doorOpenRect2 = GameObject.GameObject(80,370,"lvl1platformImages/doorOpen.png")
    doorClosedImage2 = pygame.image.load("lvl1platformImages/doorClosed.png")
    doorOpenImage2 = pygame.image.load("lvl1platformImages/doorOpen.png")
    # chest and key 1 initialization
    chestOpenImage2 =  GameObject.GameObject(1050,107,"chestImages/openedChest.png")
    chestClosedImage2 = GameObject.GameObject(1050,117,"chestImages/closedChest.png")
    chestKeyRect2 = GameObject.GameObject(620,60,"chestImages/chestKey.png")
    chestKeyImage2 = GameObject.GameObject(620,60,"chestImages/chestKey.png")
    # chest and key 2 initialization
    chestOpenImage3 =  GameObject.GameObject(230,417,"chestImages/openedChest.png")
    chestClosedImage3 = GameObject.GameObject(230,427,"chestImages/closedChest.png")
    chestKeyRect3 = GameObject.GameObject(120,190,"chestImages/chestKey.png")
    chestKeyImage3 = GameObject.GameObject(120,190,"chestImages/chestKey.png")
    # boolean functions
    Level2keyAlive = True
    Level2keyAlive2 = True
    Level2ChestAlive = True
    Level2ChestAlive2 = True
    Level2 = True
    # render level 2
    def renderLevel2():
        if Level2:
            movingPlatform_group1.empty()
            pygame.display.set_caption("Bobby: The Town of Enginerea | LEVEL 2")
            screen.blit(backgroundImage_LvL2, backgroundImage_LvL2_rect)
            
            if Level2ChestAlive:
                screen.blit(chestClosedImage2.image,chestClosedImage2.rect)
            # if there are no enemies, open the chest 
            elif len(enemies2)==0:
                screen.blit(chestOpenImage2.image,chestOpenImage2.rect)
            
            if Level2ChestAlive2:
                screen.blit(chestClosedImage3.image,chestClosedImage3.rect)
            # if there are no enemies, open the chest 
            elif len(enemies2)==0:
                screen.blit(chestOpenImage3.image,chestOpenImage3.rect)
            
            # if there are keys
            if Level2keyAlive:
                screen.blit(chestKeyImage2.image, chestKeyImage2.rect)
            if Level2keyAlive2:
                screen.blit(chestKeyImage3.image, chestKeyImage3.rect)
            platForm_group2.draw(screen)
            platForm_floor2.draw(screen)
            vertMovingPlatform_group2.update()
            vertMovingPlatform_group2.draw(screen)
            screen.blit(doorClosedImage2, (80, 370))
        else:
            print("function is false")

    #--------------------------------------------------------------------------------------------------
    #------------------------------------ RENDER LEVEL 3 ----------------------------------------------
    #--------------------------------------------------------------------------------------------------
    Level3keyAlive = True
    Level3ChestAlive = True
    Level3 = True
    # render level 3
    def renderLevel3():
        if Level3:
            pygame.display.set_caption("Bobby: The Town of Enginerea | LEVEL 3")
            screen.blit(backgroundImage_LvL3, backgroundImage_LvL3_rect)
            movingPlatform_group3.draw(screen)
            movingPlatform_group3.update()
            platForm_floor3.draw(screen)
        else:
            print("function is false")

    # --------------------------------------------------------------------------------------------------
    # ------------------------------------ RENDER BOBBY'S STATS ----------------------------------------
    # --------------------------------------------------------------------------------------------------
    # Bobby's Stats (SPRITE) to set the images
    bobbyStats = pygame.sprite.Group()
    bobbyStats.add(GameObject.Stats(28, 17, "statsImages/heart.png"))
    bobbyStats.add(GameObject.Stats(99, 20, "statsImages/strength.png"))
    bobbyStats.add(GameObject.Stats(175, 22, "statsImages/coin.png"))
    # set the font of label and the color
    font = pygame.font.SysFont("arial.ttf", 24)
    # render stats 
    def renderStats():
        heart = font.render(str(bobby.health), True, (255, 255, 255))
        strength = font.render(str(bobby.attack), True, (255, 255, 255))
        money = font.render(str(bobby.money), True, (255, 255, 255))
        statBG = pygame.Rect(24, 15, 222, 42)

        pygame.draw.rect(screen, (0,0,0), statBG)
        bobbyStats.draw(screen)
        screen.blit(heart, (70, 27))
        screen.blit(strength, (143, 27))
        screen.blit(money, (210, 27))

    # --------------------------------------------------------------------------------------------------
    # ------------------------------------------- GAME LOOP --------------------------------------------
    # --------------------------------------------------------------------------------------------------
    current_level = 1
    running = True
    while running:
        renderMainScreen()
        pygame.time.Clock().tick(100)
        # -------------------------------------------------------------------------------------------------
        # -------------------------------- IF BOBBY IS DEAD -----------------------------------------------
        # -------------------------------------------------------------------------------------------------
        if bobby.health <= 0: 
            # resetting the game
            endTime = pygame.time.get_ticks()
            elapsedTime = (endTime - startTime)/1000 #time in seconds.
            minutesPlayed = int(elapsedTime // 60)
            secondsPlayed = int(elapsedTime%60)
            die.renderDeathScreen(minutesPlayed,secondsPlayed)
            break

        # -------------------------------------------------------------------------------------------------
        # -------------------------------- IF BOBBY IS ON LEVEL 1 -----------------------------------------
        # -------------------------------------------------------------------------------------------------
        if current_level == 1:
            renderLevel1()
            renderStats()
            keys = pygame.key.get_pressed()

            enemyCollisions = pygame.sprite.spritecollide(bobby, enemies1, False)
            for collision in enemyCollisions:
                lost.play() 
                bobby.loseHp(1)
                die.totalDamageTaken += 1
                bobby.setLocation(40, 400)

            bulletCollisions = pygame.sprite.spritecollide(bobby, enemy_bullets1, False)
            for sprite in bulletCollisions:
                lost.play()
                bobby.loseHp(1)
                die.totalDamageTaken += 1
                bobby.setLocation(40, 400)
                sprite.kill()
                del sprite

            lavaCollisions = pygame.sprite.spritecollide(bobby, lavapool1, False)
            if len(lavaCollisions) > 0:
                lost.play()
                bobby.loseHp(1)
                die.totalDamageTaken += 1
                die.lavaSpills += 1
                bobby.setLocation(40,400)

            coinCollisions = pygame.sprite.spritecollide(bobby, coins1, False)
            for coin in coinCollisions:
                collected.play()
                bobby.gainMoney(coin.value)
                die.totalMoneyEarned += 20 
                coin.kill()
                del coin

            direction = bobby.playerMovementControl(keys)
            damage =1
            if keys[pygame.K_SPACE]:
                if bulletcooldown >= 20:
                    if direction[1] == True:
                        bullet_group.add(GameObject.Bullet(8, damage, direction[1], direction[0].x - 25, direction[0].y + 20, screen))
                    else:
                        bullet_group.add(GameObject.Bullet(8, damage, direction[1], direction[0].x + 35, direction[0].y + 20, screen))
                    bulletcooldown = 0
                    die.axesChucked += 1
                
            bulletcooldown += 1
            if bulletcooldown >= 20:
                bulletcooldown = 20

            collisions1 = pygame.sprite.groupcollide(bullet_group, platForm_floor1, True, False)
            collisions2 = pygame.sprite.groupcollide(bullet_group, platForm_group1, True, False)
            collisions3 = pygame.sprite.groupcollide(enemy_bullets1, platForm_floor1, True, False)
            collisions4 = pygame.sprite.groupcollide(enemy_bullets1, platForm_group1, True, False)
            collisions5 = pygame.sprite.groupcollide(bullet_group, enemy_bullets1, True, True)

            enemiesHit = pygame.sprite.groupcollide(enemies1, bullet_group, False, True)
            # if enemy gets hit by bullet
            for enemy in enemiesHit.keys():
                enemyHitSound.play()
                enemy.loseHp(bobby.attack)
                
            if len(enemies1) == 0 and bobby.rect.colliderect(doorOpenRect):
                sb.showsmallspeechbubble(bobby)
                sb.showText(bobby, "Press [ENTER]", 32.5, 65)
            # if chest key exist on level
            if Level1keyAlive: 
                # and collides with the key rectangle and bobby has 0 key  
                if bobby.rect.colliderect(chestKeyRect):
                    # stop blitting key image and increase his key amount 
                    Level1keyAlive = False
                    keyCollected.play()
                    bobby.keys+=1
                    
            # if chest is closed and enemies are killed
            if Level1ChestAlive and len(enemies1)==0:
                # and if he collides with the closed chest with a key
                if bobby.rect.colliderect(chestClosedImage.rect) and bobby.keys>=1:
                    # blit the opened chest 
                    Level1ChestAlive = False
                    chestcollected.play()
                    bobby.money+=20
                    bobby.keys-=1
            if len(enemies1) == 0 and playDialogue3 == True:
                doorClosedImage = doorOpenImage
                sb.showsmallspeechbubble(bobby)
                sb.showText(bobby, "Good work!", 20, 65)
                dialogueClock += 1
                if dialogueClock == 50:
                    playDialogue3 = False
                    dialogueClock = 0

        # -------------------------------------------------------------------------------------------------
        # -------------------------------- IF BOBBY IS ON LEVEL 2 -----------------------------------------
        # -------------------------------------------------------------------------------------------------
        elif current_level == 2:
            renderLevel2()
            renderStats()
            keys = pygame.key.get_pressed()
            direction = bobby.playerMovementControl(keys)
            
            if keys[pygame.K_SPACE]:
                if bulletcooldown >= 20:
                    if direction[1] == True:
                        bullet_group.add(GameObject.Bullet(8, 1, direction[1], direction[0].x - 25, direction[0].y + 18, screen))
                    else:
                        bullet_group.add(GameObject.Bullet(8, 1, direction[1], direction[0].x + 35, direction[0].y + 18, screen))
                    bulletcooldown = 0
                    die.axesChucked += 1
            
            bulletcooldown += 1
            if bulletcooldown >= 20:
                bulletcooldown = 20
            for bullet in bullet_group:
                bullet.bulletTravel()

            collisions1 = pygame.sprite.groupcollide(bullet_group, platForm_floor2, True, False)
            collisions2 = pygame.sprite.groupcollide(bullet_group, platForm_group2, True, False)
            
            if len(enemies2) == 0 and bobby.rect.colliderect(doorOpenRect2):
                sb.showsmallspeechbubble(bobby)
                sb.showText(bobby, "Press [ENTER]", 32.5, 65)
            # if chest key exist on level
            if Level2keyAlive: 
                # and collides with the key rectangle
                if bobby.rect.colliderect(chestKeyRect2):
                    # stop blitting key image and increase his key amount 
                    Level2keyAlive = False
                    keyCollected.play()
                    bobby.keys+=1
            # if chest key exist on level
            if Level2keyAlive2: 
                # and collides with the key rectangle
                if bobby.rect.colliderect(chestKeyRect3):
                    # stop blitting key image and increase his key amount 
                    Level2keyAlive2 = False
                    keyCollected.play()
                    bobby.keys+=1
            
            # if chest is closed and enemies are killed
            if Level2ChestAlive and len(enemies2)==0:
                # and if he collides with the closed chest with a key
                if bobby.rect.colliderect(chestClosedImage2.rect) and bobby.keys>=1:
                    # blit the opened chest 
                    Level2ChestAlive = False
                    chestcollected.play()
                    bobby.money+=20
                    bobby.keys-=1
            # if chest is closed and enemies are killed
            if Level2ChestAlive2 and len(enemies2)==0:
                # and if he collides with the closed chest with a key
                if bobby.rect.colliderect(chestClosedImage3.rect) and bobby.keys>=1:
                    # blit the opened chest 
                    Level2ChestAlive2 = False
                    chestcollected.play()
                    bobby.money+=20
                    bobby.keys-=1
            if len(enemies2) == 0 and playDialogue5 == True:
                doorClosedImage2 = doorOpenImage2
                sb.showsmallspeechbubble(bobby)
                sb.showText(bobby, "Good work!", 20, 65)
                dialogueClock += 1
                if dialogueClock == 50:
                    playDialogue5 = False
                    dialogueClock = 0
        # -------------------------------------------------------------------------------------------------
        # -------------------------------- IF BOBBY IS ON LEVEL 3 -----------------------------------------
        # -------------------------------------------------------------------------------------------------
        elif current_level == 3:
            renderLevel3()
            renderStats()
            keys = pygame.key.get_pressed()
            direction = bobby.playerMovementControl(keys)
            
            if keys[pygame.K_SPACE]:
                if bulletcooldown >= 20:
                    if direction[1] == True:
                        bullet_group.add(GameObject.Bullet(8, 1, direction[1], direction[0].x - 25, direction[0].y + 18, screen))
                    else:
                        bullet_group.add(GameObject.Bullet(8, 1, direction[1], direction[0].x + 35, direction[0].y + 18, screen))
                    bulletcooldown = 0
                    die.axesChucked += 1
            
            bulletcooldown += 1
            if bulletcooldown >= 20:
                bulletcooldown = 20
            for bullet in bullet_group:
                bullet.bulletTravel()

            collisions1 = pygame.sprite.groupcollide(bullet_group, platForm_floor3, True, False)
            collisions2 = pygame.sprite.groupcollide(bullet_group, platForm_group3, True, False)
            
        # -------------------------------------------------------------------------------------------------
        # -------------------------------------- EVENT LOOP -----------------------------------------------
        # -------------------------------------------------------------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                # renderShop()
                shop.isOpen=True
                bobby = shop.renderShop()
                damage = bobby.attack
                if current_level == 1:
                    renderLevel1()
                    renderStats()
                if current_level == 2:
                    renderLevel2()
                    renderStats()
                if current_level == 3:
                    renderLevel3()
                    renderStats()

            elif event.type == pygame.KEYDOWN and current_level == 1:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    if bobby.rect.colliderect(doorOpenRect) and len(enemies1) == 0:
                        pygame.mixer.music.stop()
                        pygame.time.delay(100)
                        doorOpen.play()
                        current_level += 1
                        Level1 = False
                        bobby.changeLevel(platForm_group2, platForm_floor2, movingPlatform_group2, vertMovingPlatform_group2)
                
            elif event.type == pygame.KEYDOWN and current_level == 2:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    if bobby.rect.colliderect(doorOpenRect2) and len(enemies2) == 0:
                        pygame.mixer.music.stop()
                        pygame.time.delay(100)
                        doorOpen.play()
                        current_level += 1
                        Level2 = False
                        bobby.changeLevel(platForm_group3, platForm_floor3, movingPlatform_group3, vertMovingPlatform_group3)

        # -------------------------------------------------------------------------------------------------
        # -------------------------------------- DIALOUGE SECTION -----------------------------------------
        # -------------------------------------------------------------------------------------------------
        if current_level == 1 and playDialogue2 == True:
            if playDialogue1 == True:
                bobby.defaultSpeed = 0
                sb.showSpeechBubbleLevel1(bobby)
                sb.showText(bobby, "Move and jump with [ARROW]", 20, 130)
                sb.showText(bobby, "keys. Press [SPACE] key to", 20, 110)
                sb.showText(bobby, "attack and deflect enemy", 20, 90)
                sb.showText(bobby, "bullets.", 20, 70)
                dialogueClock += 1
            if dialogueClock >= 100:
                playDialogue1 = False
                playDialogue2 == True
                sb.showSpeechBubbleLevel1(bobby)
                sb.showText(bobby, "Defeat all enemies to collect", 20, 130)
                sb.showText(bobby, "chests and proceed to next", 20, 110)
                sb.showText(bobby, "level.", 20, 90)
                dialogueClock += 1
            if dialogueClock == 200:
                playDialogue2 = False
                dialogueClock = 0
                bobby.defaultSpeed = 5
        
        if current_level == 2 and playDialogue4 == True:
            if playDialogue4 == True:
                bobby.defaultSpeed = 0
                sb.showSpeechBubbleLevel2(bobby)
                sb.showText(bobby, "Press [P] to open shop menu.", 170, 130)
                sb.showText(bobby, "You can upgrade weapons and", 170, 110)
                sb.showText(bobby, "stats by [LEFT] clicking the", 170, 90)
                sb.showText(bobby, "icons.", 170, 70)
                dialogueClock += 1
            if dialogueClock == 100:
                playDialogue4 = False
                dialogueClock = 0
                bobby.defaultSpeed = 5

        pygame.display.flip()
