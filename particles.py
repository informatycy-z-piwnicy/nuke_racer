from pygame.draw import circle as draw_circle
from random import randint

class Particle:
    def __init__(self, pos, rad, col, speed, direction, rad_decrement):
        self.color = col
        self.speed = speed
        self.iterator = 0
        self.tx, self.ty = pos[0], pos[1]
        self.x, self.y = pos[0], pos[1]
        self.rad_decrement = rad_decrement
        self.rad = rad
        self.trad = rad
        if direction == "left":
            self.vx, self.vy = randint(-5, -1), randint(-50, 50)*0.1
        elif direction == "right":
            self.vx, self.vy = randint(1, 5), randint(-15, 15)*0.1
        elif direction == "down":
            self.vx, self.vy = randint(-2, 2), randint(1, 15)*0.1
        elif direction == "up":
            self.vx, self.vy = randint(-2, 2), randint(-15, -1)*0.1
        else:
            self.vx, self.vy = randint(-7, -1), randint(-5, -1)*0.1

    def draw(self, win):
        draw_circle(win, self.color, (self.x-self.iterator, self.y), self.rad)
        self.iterator += self.speed
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        if randint(0, 100) < 40:
            self.rad -= self.rad_decrement

    def update_for_loop(self):
        self.x += self.vx
        self.y += self.vy
        if randint(0, 100) < 40:
            self.rad -= self.rad_decrement
        if self.rad < 1:
            self.x = self.tx
            self.y = self.ty
            self.rad = self.trad
            self.iterator = 0

class Dust:
    def __init__(self, pos, rad, size, col, speed, direction, rad_decrement):
        self.particles = []
        for i in range(size):
            self.particles.append(Particle(pos, rad, col, speed, direction, rad_decrement))

    def update(self):
        for i in self.particles:
            i.update()
            self.particles = [particle for particle in self.particles if particle.rad > 0]

    def draw(self, win):
        for i in self.particles:
            i.draw(win)

    def update_for_loop(self):
        for i in self.particles:
            i.update_for_loop()
            self.particles = [particle for particle in self.particles if particle.rad > 0]