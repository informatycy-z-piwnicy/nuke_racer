from pygame.draw import circle as draw_circle
from random import randint

class Particle:
    def __init__(self, pos, rad, col, speed):
        self.color = col
        self.speed = speed
        self.iterator = 0
        self.x, self.y = pos[0], pos[1]
        self.vx, self.vy = randint(-2, 2), randint(-20, 0)*0.1
        self.rad = rad

    def draw(self, win):
        draw_circle(win, self.color, (self.x-self.iterator, self.y), self.rad)
        self.iterator += self.speed
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        if randint(0, 100) < 40:
            self.rad -= 1

class Dust:
    def __init__(self, pos, rad, size, col, speed):
        self.particles = []
        for i in range(size):
            self.particles.append(Particle(pos, rad, col, speed))

    def update(self):
        for i in self.particles:
            i.update()
            self.particles = [particle for particle in self.particles if particle.rad > 0]

    def draw(self, win):
        for i in self.particles:
            i.draw(win)