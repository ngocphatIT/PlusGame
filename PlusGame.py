import pygame as pg
import random
pg.init()
class Button:
    def __init__(self,text,font='Times',size=40,bg1=(128,128,128),bg2=(255,230,12),fg=(0,0,0)):
        self.text=text
        self.img=pg.font.SysFont(f'{font}',size).render(f'{self.text}',True,fg)
        self.bg1=bg1
        self.bg2=bg2
    def update(self,surface,x,y):
        global time_delay
        pos=pg.mouse.get_pos()
        if pos[0]>=x and pos[0]<=x+self.img.get_width()+10 and pos[1]>=y and pos[1]<=y+self.img.get_height()+10:
            pg.draw.rect(surface,self.bg2,(x,y,self.img.get_width()+20,self.img.get_height()+20))
            if pg.mouse.get_pressed()[0] and pg.time.get_ticks()-time_delay>500:
                time_delay=pg.time.get_ticks()
                return True
        else:
            pg.draw.rect(surface,self.bg1,(x,y,self.img.get_width()+20,self.img.get_height()+20))
        surface.blit(self.img,(x+10,y+10))
        return False
class Game():
    def __init__(self):
        self.surface=pg.display.set_mode((screen_w,screen_h))
        pg.display.set_caption("Plus plus")
        self.font=pg.font.SysFont("Arial",80)
        self.score=0
        self.Toturial=0
        self.endtime=7000
        self.btStart=Button(text='Bắt đầu')
        self.btLevel=Button(text='Cấp độ')
        self.bt1=Button(text='Dễ')
        self.bt2=Button(text='Bình thường')
        self.bt3=Button(text='Vip')
        self.bt4=Button(text="Siêu cấp")
        self.bt5=Button(text="Siêu cấp vip pro")
        self.btRestart=Button(text='Chơi lại')
        self.btBack=Button(text="Quay lại")
    def run(self):
        clock=pg.time.Clock()
        FPS=60
        while True:
            clock.tick(FPS)
            self.display()
            for ev in pg.event.get():
                if ev.type==pg.QUIT:
                    return
                if ev.type==pg.KEYDOWN:
                    if ev.key==pg.K_BACKSPACE:
                        self.text=self.text[:-1]
                    elif ev.key==pg.K_LSHIFT:
                        self.text=''
                    elif ev.key==pg.K_RETURN:
                        if self.text==self.answer:
                            self.new()
                            self.score+=1
                    else:
                        self.text=self.text+ev.unicode
            pg.display.update()
    def add_question(self):
        self.number1=random.randint(1,self.score*4+5)
        self.number2=random.randint(1,self.score*4+5)
        self.question=self.font.render(f'{self.number1} + {self.number2}',True,(0,0,0))
        self.answer=str(self.number1+self.number2)
        self.rect=self.question.get_rect()
        self.rect.center=(screen_w//2,screen_h//2-100)
    def display(self):
        self.surface.fill((100,255,200))
        if self.Toturial==0:
            self.surface.blit(pg.font.SysFont("Times",50).render('Để tui coi',True,(255,0,0)),(screen_w//2-100,30))
            self.surface.blit(pg.font.SysFont("Times",50).render('tính nhẩm được bao nhiêu',True,(255,0,0)),(screen_w//2-250,100))
            if self.btStart.update(self.surface,screen_w//2-70,200):
                self.Toturial=3
                self.new()
            if self.btLevel.update(self.surface,screen_w//2-63,350):
                self.Toturial=1
        elif self.Toturial==1:
            self.level()
        elif self.Toturial==2:
            self.gameover()
        elif self.Toturial==3:
            if pg.time.get_ticks()-self.update_time>self.endtime:
                self.Toturial=2
            pg.draw.rect(self.surface,(255,255,255),(screen_w//2-self.question.get_width()//2-10,screen_h//2-self.question.get_height()//2-110,self.question.get_width()+20,self.question.get_height()+20))
            self.surface.blit(self.question,self.rect) 
            img=pg.font.SysFont("Arial",40).render(f'{self.text}',True,(255,255,255))
            rect=img.get_rect()
            rect.center=(screen_w//2,screen_h//2+50)
            pg.draw.rect(self.surface,(15,168,213),(screen_w//2-img.get_width()//2-10,screen_h//2-img.get_height()//2+45,img.get_width()+20,img.get_height()+20))
            self.surface.blit(img,rect)
            self.surface.blit(pg.font.SysFont("Arial",30).render(f'SCORE: {self.score}',True,(0,0,0)),(10,10))
            pg.draw.rect(self.surface,(255,255,0),(00,screen_h-100,screen_w,50))
            pg.draw.rect(self.surface,(245,0,0),(0,screen_h-100,screen_w-screen_w*(pg.time.get_ticks()-self.update_time)/self.endtime,50))
    def new(self):
        self.update_time=pg.time.get_ticks()
        self.text=''
        self.add_question()
    def level(self):
        self.surface.blit(pg.font.SysFont("Times",50).render('Cấp độ',True,(255,0,0)),(screen_w//2-70,10))
        y=100
        if self.bt1.update(self.surface,screen_w//2-20-10,y):
            self.endtime=6500
            self.Toturial=3
            self.new()
        if self.bt2.update(self.surface,screen_w//2-90-10,y+80):
            self.endtime=6000
            self.new()
            self.Toturial=3
        if self.bt3.update(self.surface,screen_w//2-25-10,y+160):
            self.endtime=5000
            self.new()
            self.Toturial=3
        if self.bt4.update(self.surface,screen_w//2-70-10,y+240):
            self.endtime=3500
            self.new()
            self.Toturial=3
        if self.bt5.update(self.surface,screen_w//2-135-10,y+320):
            self.endtime=1500
            self.new()
            self.Toturial=3
    def gameover(self):
        self.surface.blit(pg.font.SysFont("Times",50).render(f'Điểm của bạn: {self.score}',True,(0,0,0)),(screen_w//2-170,30))
        self.surface.blit(pg.font.SysFont("Times",50).render('Thua rồi! Chơi lại đi!',True,(255,0,0)),(screen_w//2-220,100))
        self.surface.blit(pg.font.SysFont("Times",50).render('Còn thở là còn gỡ!',True,(255,0,0)),(screen_w//2-180,170))
        if self.btRestart.update(self.surface,screen_w//2-70,250):
            self.Toturial=3
            self.new()
            self.score=0
        if self.btBack.update(self.surface,screen_w//2-73,350):
            self.Toturial=0
            self.score=0
if __name__ == "__main__":
    screen_w=700
    screen_h=500
    time_delay=pg.time.get_ticks()
    screen=Game()
    screen.run()