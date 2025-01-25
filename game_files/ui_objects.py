import pygame
pygame.font.init()

class Text:
    def __init__(self,cx,cy,color,text,font_size,font="arial",max_width=0,max_height=0):
        fontObj = pygame.font.SysFont(font,font_size)
        if max_width > 0 or max_height > 0:
            for i in range(font_size,4,-1):
                fontObj = pygame.font.SysFont(font,i)
                img = fontObj.render(text,True,color)
                rect = img.get_rect()
                if max_width > 0 and max_height > 0:
                    if rect.width <= max_width and rect.height <= max_height:
                        break
                elif max_width > 0:
                    if rect.width <= max_width:
                        break
                elif max_height > 0:
                    if rect.height <= max_height:
                        break
        else:
            img = fontObj.render(text,True,color)
        self.img = img
        self.cx = cx
        self.cy = cy

    def draw(self,screen):
        screen.blit(self.img,self.cx,self.cy)
        

class Clickable:
    def __init__(self,cx,cy,w,h,color,callback,text="",text_color=(0,0,0),type="box"):
        self.cx = cx
        self.cy = cy
        self.w = w
        self.h = h
        self.type = type
        self.color = color
        self.callback = callback
        if text != "":
            self.text = Text(cx,cy,text_color,text,48,max_width=w,max_height=h)
        else:
            self.text = ""

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
        pygame.draw.rect(screen,self.color,(self.cx,self.cy,self.w,self.h))
        if self.text != "":
            self.text.draw(screen)



class RoundButton(Clickable):
    def __init__(self,cx,cy,r,color,callback):
        super().__init__(self,cx,cy,r,r,color,callback,type="circle")

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.cx,self.cy),self.w)
        if self.text != "":
            self.text.draw(screen)