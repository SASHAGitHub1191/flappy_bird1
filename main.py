
from pygame import *
from time import sleep
from time import time as globl_time
from random import randint
init()
window = display.set_mode((1024, 720))
background = transform.scale(image.load('background.png'), (1024, 720))
clock = time.Clock()
class Sprite(sprite.Sprite):
    def __init__(self, picture, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(picture), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Bird(Sprite):
    def __init__(self, picture, x, y, width, height):
        super().__init__(picture, x, y, width, height)
        self.speed = 0
        self.angle = 0
        self.width = width
        self.height = height
        self.picture = picture



    def update(self):
        print(self.angle)
        self.rect.y = self.rect.y + self.speed
        if self.speed <= 4:
            self.speed = self.speed + 0.1
        keys = key.get_pressed()
        if keys[K_SPACE]:
            self.image = transform.scale(image.load('bird-50.png'), (self.width, self.height))
            self.speed =  - 4

            self.angle  = 50
        if self.angle >= -50:
            self.angle = self.angle - 1

            if self.angle == -50:
                self.image = transform.scale(image.load('bird50.png'), (self.width, self.height))
            if self.angle == 0:
                self.image = transform.scale(image.load(self.picture), (self.width, self.height))
        
                self.rect = self.image.get_rect(center=self.rect.center)
    def rotate(self, angle):
        self.image = transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)


    

class Tube(Sprite):
    def __init__(self, picture, x, y, width, height, speed):
        super().__init__(picture, x, y, width, height)
        self.speed = speed
    def update(self):
        self.rect.x = self.rect.x - self.speed
        if self.rect.x < -100:
            tubes.remove(self)
invulnerability_coin = Tube('pngwing.com.png', 500, 50, 100, 100, 2)



game_over = transform.scale(image.load('game_over.png'), (720, 360))
tube5 = Tube('труба2.jpg', 1000, 550, 100, 800, 2)
tube6 = Tube('труба.jpg', 1000, -550, 100, 800, 2)
tube7 = Tube('труба2.jpg', 2000, 550, 100, 800, 2)
tube8 = Tube('труба.jpg', 2000, -550, 100, 800, 2)
tubes = sprite.Group()
tubes.add( tube5, tube6, tube7, tube8)
bird = Bird('bird2.1.png',20,300,70,60)
play_button = Sprite('Play_Button.webp',370, 400, 250, 150)
n = False
run  = True
points = -1
def restart():
    global lose, n, points
    lose = False
    bird.rect.x = 20
    bird.rect.y = 300
    bird.speed = 0
    play_button.rect.y = -300
    tubes.empty()
    points = -1

    tube5 = Tube('труба2.jpg', 1000, 550, 100, 800, 2)
    tube6 = Tube('труба.jpg', 1000, -550, 100, 800, 2)
    tube7 = Tube('труба2.jpg', 2000, 550, 100, 800, 2)
    tube8 = Tube('труба.jpg', 2000, -550, 100, 800, 2)
    tubes.add( tube5, tube6, tube7, tube8)
    n = True
lose = False
point = points+5
fon_token = transform.scale(image.load('timerfont.png'),(300, 350))
while run:


    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == MOUSEBUTTONDOWN:
            x,y = mouse.get_pos()
            if play_button.rect.collidepoint(x,y):
                restart()

    if len(tubes) < 6:
        a = randint(-200,200)
        points += 1
        print(points)

        tubes.add(Tube('труба.jpg',1500, -550 + a, 100 , 800, 2)),
        tubes.add(Tube('труба2.jpg',1500, 550 + a, 100 ,800, 2))#TODO

    images = font.SysFont('impact', 100 ).render( str(points), True, (0, 30, 60))
    window.blit(background, (0, 0))
    window.blit(fon_token,(-50,-110))
    tubes.draw(window)
    tubes.update()

    if bird.rect.colliderect(invulnerability_coin.rect):
        print('frejiouerfinujervnuiervu')
        point = points + 5
        invulnerability_coin.rect.y -= 1000
        n = False
    if point < points and n == False:
        invulnerability_coin.rect.y = randint(20,620)
        invulnerability_coin.rect.x = randint(1000,10000)
        n = True
        

    bird.draw()
    bird.update()
    window.blit(images, (100, 0))
    play_button.draw()
    if lose:
        window.blit(game_over, (140, 130))
    if n == True:

        play_button.draw()




        invulnerability_coin.update()

        invulnerability_coin.draw()

        if sprite.spritecollide(bird, tubes,False):

            lose = True

            n = False
            play_button.rect.y = 400
            play_button.draw()


    display.update()



    clock.tick(120)



