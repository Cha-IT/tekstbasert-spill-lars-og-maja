World = [
    ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"],
    ["x"," "," "," "," "," "," "," "," "," "," "," "," ","x","x"," "," "," "," "," "," "," "," "," "," "," "," ","x"],
    ["x"," ","x","x","x","x"," ","x","x","x","x","x"," ","x","x"," ","x","x","x","x","x"," ","x","x","x","x"," ","x"],
    ["x"," ","x","x","x","x"," ","x","x","x","x","x"," ","x","x"," ","x","x","x","x","x"," ","x","x","x","x"," ","x"],
    ["x"," ","x","x","x","x"," ","x","x","x","x","x"," ","x","x"," ","x","x","x","x","x"," ","x","x","x","x"," ","x"],
    ["x"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","x"],
    ["x"," ","x","x","x","x"," ","x","x"," ","x","x","x","x","x","x","x","x"," ","x","x"," ","x","x","x","x"," ","x"],
    ["x"," ","x","x","x","x"," ","x","x"," ","x","x","x","x","x","x","x","x"," ","x","x"," ","x","x","x","x"," ","x"],
    ["x"," "," "," "," "," "," ","x","x"," "," "," "," ","x","x"," "," "," "," ","x","x"," "," "," "," "," "," ","x"],
    ["x","x","x","x","x","x"," ","x","x","x","x","x"," ","x","x"," ","x","x","x","x","x"," ","x","x","x","x","x","x"],
    [" "," "," "," "," ","x"," ","x","x","x","x","x"," ","x","x"," ","x","x","x","x","x"," ","x"," "," "," "," "," "],
    [" "," "," "," "," ","x"," ","x","x"," "," "," "," "," "," "," "," "," "," ","x","x"," ","x"," "," "," "," "," "],
    [" "," "," "," "," ","x"," ","x","x"," ","x","x","x","x","x","x","x","x"," ","x","x"," ","x"," "," "," "," "," "],
    ["x","x","x","x","x","x"," ","x","x"," ","x"," "," "," "," "," "," ","x"," ","x","x"," ","x","x","x","x","x","x"],
    [" "," "," "," "," "," "," "," "," "," ","x"," "," "," "," "," "," ","x"," "," "," "," "," "," "," "," "," "," "],
    ["x","x","x","x","x","x"," ","x","x"," ","x"," "," "," "," "," "," ","x"," ","x","x"," ","x","x","x","x","x","x"],
    [" "," "," "," "," ","x"," ","x","x"," ","x","x","x","x","x","x","x","x"," ","x","x"," ","x"," "," "," "," "," "],
    [" "," "," "," "," ","x"," ","x","x"," "," "," "," "," "," "," "," "," "," ","x","x"," ","x"," "," "," "," "," "],
    [" "," "," "," "," ","x"," ","x","x"," ","x","x","x","x","x","x","x","x"," ","x","x"," ","x"," "," "," "," "," "],
    ["x","x","x","x","x","x"," ","x","x"," ","x","x","x","x","x","x","x","x"," ","x","x"," ","x","x","x","x","x","x"],
    ["x"," "," "," "," "," "," "," "," "," "," "," "," ","x","x"," "," "," "," "," "," "," "," "," "," "," "," ","x"],
    ["x"," ","x","x","x","x"," ","x","x","x","x","x"," ","x","x"," ","x","x","x","x","x"," ","x","x","x","x"," ","x"],
    ["x"," ","x","x","x","x"," ","x","x","x","x","x"," ","x","x"," ","x","x","x","x","x"," ","x","x","x","x"," ","x"],
    ["x"," "," "," ","x","x"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","x","x"," "," "," ","x"],
    ["x","x","x"," ","x","x"," ","x","x"," ","x","x","x","x","x","x","x","x"," ","x","x"," ","x","x"," ","x","x","x"],
    ["x","x","x"," ","x","x"," ","x","x"," ","x","x","x","x","x","x","x","x"," ","x","x"," ","x","x"," ","x","x","x"],
    ["x"," "," "," "," "," "," ","x","x"," "," "," "," ","x","x"," "," "," "," ","x","x"," "," "," "," "," "," ","x"],
    ["x"," ","x","x","x","x","x","x","x","x","x","x"," ","x","x"," ","x","x","x","x","x","x","x","x","x","x"," ","x"],
    ["x"," ","x","x","x","x","x","x","x","x","x","x"," ","x","x"," ","x","x","x","x","x","x","x","x","x","x"," ","x"],
    ["x"," "," "," "," "," "," "," "," "," "," "," "," ","x","x"," "," "," "," "," "," "," "," "," "," "," "," ","x"],
    ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"]
]

import pygame as pg
pg.init()
from sys import exit
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)


Width = 280
Height = 310
Screen=pg.display.set_mode([Width, Height])
Screen.fill((255, 255, 255))
clock = pg.time.Clock()

spill_areal = pg.Surface((Width, Height))
spill_areal.fill((133, 155, 177))

class Figur():
    def __init__(self, x, y, fartx, farty, farge):
        self.x = x
        self.y = y
        self.fartx = fartx
        self.farty = farty
        self.farge = farge
    def draw0(self):
        World[self.y][self.x] = " "
    def draw1(self):
        World[self.y][self.x] = "o"
    def move(self):
        if (self.fartx == 1):
            if (World[self.y][self.x+1]) == "x":
                self.fartx = 0
            else:
                self.x+=self.fartx
        elif (self.fartx == -1):
            if (World[self.y][self.x-1]) == "x":
                self.fartx = 0
            else:
                self.x+=self.fartx
        elif (self.farty == 1):
            if (World[self.y+1][self.x]) == "x":
                self.farty = 0
            else:
                self.y+=self.farty
        elif (self.farty == -1):
            if (World[self.y-1][self.x]) == "x":
                self.farty = 0
            else:
                self.y+=self.farty
    def opp(self):
            self.fartx=0
            self.farty=-1
    def ned(self):
            self.fartx=0
            self.farty=1
    def venstre(self):
            self.fartx=-1
            self.farty=0
    def høyre(self):
            self.fartx=1
            self.farty=0
class pacman(Figur):
    def __init__(self, x, y, fartx, farty, farge):
        super().__init__(x, y, fartx, farty, farge)
    


spiller = pacman(14, 23, 1, 0, (255,0,0))
spiller.draw1()
t = 0
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    trykkede_taster = pg.key.get_pressed()
    if trykkede_taster[K_LEFT]:
        spiller.venstre()
    elif trykkede_taster[K_RIGHT]:
        spiller.høyre()
    elif trykkede_taster[K_UP]:
        spiller.opp()
    elif trykkede_taster[K_DOWN]:
        spiller.ned()
    spiller.draw0()
    if t >=100:
        spiller.move()
        t=0
    t+=10
    spiller.draw1()
    for i in range(len(World)):
        for m in range(len(World[i])):
            if World[i][m] == "x":
                pg.draw.rect(spill_areal, (0, 0, 255), (10*m,10*i, 10, 10))
            elif World[i][m] == " ":
                pg.draw.rect(spill_areal, (255, 255, 255), (10*m,10*i, 10, 10))
            elif World[i][m] == "o":
                pg.draw.rect(spill_areal, spiller.farge, (10*m,10*i, 10, 10))

    Screen.blit(spill_areal, (0, 0))
    pg.display.update()
    clock.tick(60)