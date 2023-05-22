import random
class BoringParticle:
    def __init__(self,x,y,speed_x,speed_y):
        self.x=x
        self.y=y
        self.speed_x=speed_x
        self.speed_y=speed_y

    def bewegen(self,interval):
        self.x += (self.speed_x*interval)
        self.y += (self.speed_y*interval)

    def reset(self,breedte,hoogte):
        if (self.y < 0) or (self.y > hoogte) or (self.x < 0) or (self.x > breedte) or ((random.random()) > 0.9999):
            self.color_boring = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            self.x = breedte//2
            self.y = hoogte//2
            self.random_x = (random.random()*2)-1
            self.random_y = (random.random()*2)-1

class BouncingParticle:
    def __init__(self,x,y,speed_x,speed_y):
        self.x=x
        self.y=y
        self.speed_x=speed_x
        self.speed_y=speed_y

    def bewegen(self,interval):
        self.x += (self.speed_x*interval)
        self.y += (self.speed_y*interval)

    def bounce(self,breedte,hoogte):
        if (self.y < 0) or (self.y > hoogte) or ((random.random()) > 0.9999):
            self.color_bounce = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            self.speed_y = -self.speed_y
        if(self.x < 0) or (self.x > breedte) or ((random.random()) > 0.9999):
            self.color_bounce = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            self.speed_x = -self.speed_x