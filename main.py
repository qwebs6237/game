from pygame import *
from pygame.constants import K_RIGHT, K_LEFT


class GameSprite(sprite.Sprite):
    def __init__(self, image_, x, y, speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(image_), (w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
    def move_p1(self,  keys):
        if keys[K_a] and self.rect.y > 10 :
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < 500 - 10 - 130:
            self.rect.y += self.speed


class Player2(GameSprite):
    def move_p2(self,  keys):
        if keys[K_LEFT] and self.rect.y > 10 :
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < 500 - 10 - 130:
            self.rect.y += self.speed


class Ball(GameSprite):
    def __init__(self, img, x, y, speed, w, h, speed_x, speed_y):
        super().__init__(img, x, y, speed, w, h)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        global a
        global b
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.colliderect(player1.rect) or self.rect.colliderect(player2.rect):
            self.speed_x *= -1
        elif self.rect.x > 600:
            self.rect.x = 250
            self.speed_x *= -1
            a += 1
            print(a)
        elif self.rect.y < 0 :
            self.rect.y = 0
            self.speed_y *= -1
        elif self.rect.x < 0:
            self.rect.x = 250
            self.speed_x *= -1
            b += 1
            print(b)
        elif self.rect.y > 400 :
            self.rect.y = 400
            self.speed_y *= -1
       

window = display.set_mode((700, 500))
display.set_caption('ping pong')

background = transform.scale(
    image.load('fon.png'),
    (700, 500))

player1 = Player1('dask.png', 10, 10, 1, 40, 130)
player2 = Player2('dask.png', 700 - 50, 10, 1, 40, 130)
ball = Ball('player.png', 350, 250, 1, 100, 100, 1, -1)

a = 0
b = 0
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    keys = key.get_pressed()
    player1.move_p1(keys)
    player2.move_p2(keys)
    ball.move()

    window.blit(background, (0, 0))

    player1.reset()
    player2.reset()
    ball.reset()

    display.update()
