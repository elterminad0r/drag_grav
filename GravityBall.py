def apply_to(l):
    def to_all(func):
        def f():
            for i in l:
                func(i)
        return f
    return to_all

def is_small(n):
    return n.mag() < 9

class GravityBall(object):
    inst = set()
    tofade = set()
    
    def __init__(self, loc=None):
        if loc:
            self.loc = loc
        else:
            self.loc = PVector(random(width), random(height, height * 2))
        self.vel = PVector(random(-30, 30), random(-10, 10))
        self.r = random(40, 60)
        self.h = random(255)
                
        self.inst.add(self)
    
    @staticmethod
    @apply_to(inst)
    def update(self):
        self.vel.y -= 1
        self.vel *= 0.99
        self.loc += self.vel
        if self.loc.x - self.r < 0:
            self.loc.x = self.r
            self.vel.x *= -1
        if self.loc.x + self.r > width:
            self.loc.x = width - self.r
            self.vel.x *= -0.9
        if self.loc.y - self.r < 0:
            if is_small(self.vel):
                self.loc.y = self.r
                self.life = 60
                self.inst.remove(self)
                self.tofade.add(self)
            else:
                self.vel.y *= -0.9
                self.loc.y = self.vel.y + self.r
                self.vel.x *= 0.9
                
    @staticmethod
    @apply_to(inst)
    def draw(self):
        fill(self.h, 255, 255)
        noStroke()
        ellipse(self.loc.x, self.loc.y, self.r * 2, self.r * 2)

    @staticmethod
    @apply_to(tofade)
    def fade(self):
        fill(self.h, 255, 255, map(self.life, 60, 0, 255, 0))
        noStroke()
        ellipse(self.loc.x, self.loc.y, self.r * 2, self.r * 2)
        self.life -= 1
        if self.life < 0:
            self.tofade.remove(self)
            GravityBall()