import pygame

class Clickable:
    def __init__(self,cx,cy,w,h,color,callback,type="box"):
        self.cx = cx
        self.cy = cy
        self.w = w
        self.h = h
        self.type = type
        self.color = color
        self.callback = callback

    def checkClicked(self,mx,my):
        if self.type == "box":
            if mx > self.cx - (self.w / 2) and mx < self.cx + (self.w/2) and my > self.cy - (self.h/2) and my < self.cy + (self.h/2):
                self.callback()
                return True
            else:
                return False
        elif self.type == "circle":
            if ((mx-self.cx)**2 + (my-self.cy)**2)**0.5 < self.w/2:
                self.callback()
                return True
            else:
                return False
            

class RectButton(Clickable):
    def __init__(self,cx,cy,w,h,color,callback):
        super().__init__(self,cx,cy,w,h,color,callback,type="box")

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.cx,self.cy,self.cw,self.ch))


class RoundButton(Clickable):
    def __init__(self,cx,cy,r,color,callback):
        super().__init__(self,cx,cy,r,r,color,callback,type="circle")

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.cx,self.cy),self.w)