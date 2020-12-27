import pygame,random
pygame.init()

# game variable

width=720
height=480

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
brown = (100,60,0)
grey = (50,50,50)

font=pygame.font.SysFont(None,40)
fps=60

game = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")
pygame.display.update()


def txt_on_scr(txt,x,y):
    scr_txt=font.render(txt,True,white)
    game.blit(scr_txt,[x,y])

def welcome():
    bg=pygame.image.load("wel.png")
    bg=pygame.transform.scale(bg,(width,height)).convert_alpha()
    game.blit(bg,(0,0))
    pygame.display.update()
    while 1:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    return game_loop() 
            elif event.type==pygame.QUIT:
                quit()

def game_over(score,hiscore):
    bg3=pygame.image.load("gameover.png")
    bg3=pygame.transform.scale(bg3,(width,height)).convert_alpha()
    game.blit(bg3,(0,0))
    txt_on_scr(f"               Your SCORE : {score}         BEST : {hiscore}",10,10)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    return game_loop()
            elif event.type==pygame.QUIT:
                quit()


def game_loop():

    # Variables
    snk_x=width/2
    snk_y=height/2
    vel=1
    vel_x=0
    vel_y=0
    snk_size=10
    snk_len=1
    snk_list=[]
    food_size=6
    food_x=random.randint(10,width-10)
    food_y=random.randint(40,height-10)
    gap=10
    score=0

    clock=pygame.time.Clock()
    game.fill(brown)
    pygame.draw.rect(game,black,[snk_x,snk_y,snk_size,snk_size])
    
    with open("HiScore.txt",'r') as f:
        hiscore=int(f.read())

    while 1:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    if not vel_x==(-vel):
                        vel_x=vel
                        vel_y=0

                elif event.key==pygame.K_LEFT:
                    if not vel_x==vel:
                        vel_x=(-vel)
                        vel_y=0

                elif event.key==pygame.K_UP:
                    if not vel_y==vel:
                        vel_y=(-vel)
                        vel_x=0

                elif event.key==pygame.K_DOWN:
                    if not vel_y==(-vel):
                        vel_y=vel
                        vel_x=0
            
            elif event.type==pygame.QUIT:
                quit()

        snk_x += vel_x
        snk_y += vel_y

        head=[snk_x,snk_y]
        snk_list.append(head)

        if len(snk_list)>snk_len:
            del snk_list[0]

        game.fill(grey)        
        pygame.draw.lines(game, black, True, [(0,20),(width,20)],50)
        
        for x,y in snk_list:
            pygame.draw.rect(game,black,(x,y,snk_size,snk_size))

        pygame.draw.circle(game,red,[food_x,food_y],food_size)

        if abs(food_x-snk_x)<gap and abs(food_y-snk_y)<gap:
            score+=10
            snk_len+=4
            vel+=0.25
            food_x=random.randint(10,width-10)
            food_y=random.randint(40,height-10)
            pygame.draw.circle(game,red,[food_x,food_y],food_size)

        if snk_x<0 or snk_x>width or snk_y<40 or snk_y>height:
            return game_over(score,hiscore)

        if head in snk_list[:-1]:
            return game_over(score,hiscore)

        if score>hiscore:
            hiscore=score
            with open("HiScore.txt",'w') as f:
                f.write(str(hiscore))

        txt_on_scr(f"               Your SCORE : {score}         BEST : {hiscore}",10,10)

        clock.tick(fps)                    


welcome()