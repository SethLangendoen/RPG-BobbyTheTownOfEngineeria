import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y


class Bullet(GameObject):
    def __init__(self, speed, damage, direction, x, y):
        super.__init__(x, y, "Bullet.png")
        self.speed = speed
        self.damage = damage
        self.direction = direction


class SpeechBubble(GameObject):
    def __init__(self, text, x, y):
        self.text = text
        super.__init__(x, y, "SpeechBubble.png")

    def replaceText(self, text):
        self.text = text

    def closeBubble(self):
        self.text = ""


class Character(GameObject):
    def __init__(self, speed, health, currentLocation, x, y):
        super.__init__(x, y, "Character.png")
        self.speed = speed
        self.health = health
        self.currentLocation = currentLocation

    def loseHp(self, damage):
        self.health = self.health - damage


class Enemy(GameObject):
    def __init__(self, type, direction, health, x, y):
        self.type = type
        self.direction = direction
        self.health = health
        super.__init__(x, y, "Enemy.png")

    def loseHp(self, damage):
        self.health = self.health - damage

    def shoot(self):
        speed = ""
        damage = ""
        if type == 1:
            speed = 5
            damage = 1
        elif type == 2:
            speed = 10
            damage = 2
        elif type == 3:
            speed = 15
            damage = 3
        # return a bullet object with correct direction and starting position with given speed


class PlatForms(GameObject):
    def __init__(self, x, y, img_path):
        super().__init__(x, y, img_path)
