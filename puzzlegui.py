
import pygame,sys


#___________________________
# Module puzzle_gui
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)
GRAY = (200,200,200)
LEFT=1
letter_block_size=26
Word_block_size=100
current_start=0
current_end=0

# getting the parameters

# from gset letter_block_size=50
# calculated from letter block size #Word_block_size=100
w_start,w_end=(0,0),(0,0)
def start(gstat):#Gset,gstat
    char_mat=gstat.char_mat

    # matrix size
    width_mat=(char_mat.n)*letter_block_size 
    hight_mat=(char_mat.n)*letter_block_size
    # frame size = 1
    width_frame=letter_block_size
    hight_frame=letter_block_size
    # word block size at bottom
    hight_words=Word_block_size

    width=2*width_frame+width_mat+hight_words
    hight=2*hight_frame+hight_mat
    #generating the display
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((width,hight))
    pygame.display.set_caption('Word Puzzle!')


    # creating grid

    # 	set DISPLAYSURF with C and W and G
    # for every character do this
    fontObjMessage = pygame.font.Font('freesansbold.ttf',letter_block_size*2)

    # c='a'
    # textSurfaceObj = fontObj.render(c, True, BLACK)
    # textRectObj = textSurfaceObj.get_rect()
    # textRectObj.center = (letter_block_size*(3/2.0+i), letter_block_size*(3/2.0+i))
    # DISPLAYSURF.blit(textSurfaceObj, textRectObj)


    # displaying words
    # from W


    #display copy
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 25)
    frame_count = 0
    frame_rate = 60
    start_time = gstat.time
    total_seconds = start_time - (frame_count // frame_rate)
    start = False
    while True: # main game loop
        for event in pygame.event.get():
    # mouse drag and select
            if not gstat.times_up and not gstat.success:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:        
                    if valid(event.pos,width_mat,hight_mat,width_frame,hight_frame):
                        P_1=convert(event.pos,width_frame,hight_frame,letter_block_size)
                        start=True
                        current_start=P_1
                        current_end=P_1
                        
                        # print P_1
                if start and event.type == pygame.MOUSEMOTION:
                    
                    if valid(event.pos,width_mat,hight_mat,width_frame,hight_frame):
                        P_j=convert(event.pos,width_frame,hight_frame,letter_block_size)
                        # pygame.draw.line(DISPLAYSURF,GREEN,(P_1[0]*letter_block_size+width_frame+letter_block_size/2, P_1[1]*letter_block_size+letter_block_size/2+hight_frame),(P_j[0]*letter_block_size+width_frame+letter_block_size/2, P_j[1]*letter_block_size+letter_block_size/2+hight_frame))
                        current_start=P_1
                        current_end=P_j
                if start and event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:     
                    if valid(event.pos,width_mat,hight_mat,width_frame,hight_frame):
                        P_2=convert(event.pos,width_frame,hight_frame,letter_block_size)
                        print P_2
                        print P_1
                        start = False

                        # AAfilledRoundedRect(DISPLAYSURF,(0,0,10,10),WHITE,0.2)

                        # highlight_char
                        # time.sleep(0.1sec)
                        gstat.check_word(w_start,w_end)
                        print gstat.word_list.found
            if event.type == pygame.QUIT:
                pygame.quit()
                    

                    # update the display (Display_copy,G.W,)

            # if bool ==True 
            #   if left click
            #       if valid
            #           call chech_fun()
            # #             if valid update display(green colour word + strike of the word)
         #    if event.type == MOUSEBUTTONUP:
         #        mousex, mousey = event.pos
         #        if (letter_block_size<=mousex<=letter_block_size*char_mat.n) and (letter_block_size<=mousey<=letter_block_size*char_mat.n):
         #          Started=True
         #            pygame.quit()
         #            # sys.exit()
         #            # x_b=mousex/
         #          # compllte it
         #            print "ggvtg"
         #            sys.exit()
         #    if left click
         #      if valid
         #          bool = True
         #          S=cursor
         #          update display with selected letter

                # sys.exit()
        DISPLAYSURF.fill(WHITE)
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT  
    # --- Timer going up ---
    # Calculate total seconds
        draw_lines(char_mat,DISPLAYSURF)
        draw_chars(char_mat,DISPLAYSURF)
        draw_words(gstat.char_mat,gstat.word_list,DISPLAYSURF)
        y=0
        for w in gstat.word_list.words:
            if gstat.word_list.found[y]:
                # print w
                # print P_1
                # print P_2
                w_start,w_end =gstat.word_list.get_start_end_xy(y)

                highlight_char(DISPLAYSURF,(w_start[0]*letter_block_size+width_frame, w_start[1]*letter_block_size+hight_frame),GREEN)
                highlight_char(DISPLAYSURF,(w_end[0]*letter_block_size+width_frame, w_end[1]*letter_block_size+hight_frame),GREEN)
                pygame.draw.line(DISPLAYSURF,GREEN,(w_start[0]*letter_block_size+width_frame+letter_block_size/2, w_start[1]*letter_block_size+letter_block_size/2+hight_frame),(w_end[0]*letter_block_size+width_frame+letter_block_size/2, w_end[1]*letter_block_size+letter_block_size/2+hight_frame))
                # highlight_charpygame.draw.circle(DISPLAYSURF, RED, (P_1[0]*letter_block_size+width_frame+letter_block_size/2, P_1[1]*letter_block_size+letter_block_size/2+hight_frame), 12, 2)
                # pygame.draw.circle(DISPLAYSURF, GREEN, (w_start[0]*letter_block_size+width_frame+letter_block_size/2, w_start[1]*letter_block_size+letter_block_size/2+hight_frame), 12, 0)
                # pygame.draw.circle(DISPLAYSURF, GREEN, (w_end[0]*letter_block_size+width_frame+letter_block_size/2, w_end[1]*letter_block_size+letter_block_size/2+hight_frame), 12, 2)
                # pygame.draw.line(DISPLAYSURF,GREEN,(w_start[0]*letter_block_size+width_frame+letter_block_size/2, w_start[1]*letter_block_size+letter_block_size/2+hight_frame),(w_end[0]*letter_block_size+width_frame+letter_block_size/2, w_end[1]*letter_block_size+letter_block_size/2+hight_frame))
            y=y+1

        if start:
            w_start,w_end=get_sticky(current_start,current_end)
            highlight_char(DISPLAYSURF,(w_start[0]*letter_block_size+width_frame, w_start[1]*letter_block_size+hight_frame),RED)
            
            highlight_char(DISPLAYSURF,(w_end[0]*letter_block_size+width_frame, w_end[1]*letter_block_size+hight_frame),RED)
            pygame.draw.line(DISPLAYSURF,RED,(w_start[0]*letter_block_size+width_frame+letter_block_size/2, w_start[1]*letter_block_size+letter_block_size/2+hight_frame),(w_end[0]*letter_block_size+width_frame+letter_block_size/2, w_end[1]*letter_block_size+letter_block_size/2+hight_frame))
           
        if gstat.success:
            # display success and time left
            textSurfaceObj = fontObjMessage.render("You Won!", True, BLUE)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (letter_block_size*(3/2.0+char_mat.n/2), letter_block_size*(3/2.0+char_mat.n/2))
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        if total_seconds==0:
            gstat.check_word((-1,-1),(-1,-1))
            print "timesup"
            print gstat.times_up
        if gstat.times_up:
            textSurfaceObj = fontObjMessage.render("Time's Up!", True, BLUE)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (letter_block_size*(3/2.0+char_mat.n/2), letter_block_size*(3/2.0+char_mat.n/2))
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)


        # total_seconds = frame_count // frame_rate
         
        # # Divide by 60 to get total minutes
        # minutes = total_seconds // 60
         
        # # Use modulus (remainder) to get seconds
        # seconds = total_seconds % 60
         
        # Use python string formatting to format in leading zeros
        # output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
         
        # # Blit to the screen
        # text = font.render(output_string, True, BLACK)
        # DISPLAYSURF.blit(text, [250, 250])
         
     
        # --- Timer going down ---
        # --- Timer going up ---
        # Calculate total seconds
        if not gstat.success:
            total_seconds = start_time - (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
         
        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
         
        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60
         
        # Use python string formatting to format in leading zeros
        output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
         
        # Blit to the screen
        text = font.render(output_string, True, BLACK)
         
        DISPLAYSURF.blit(text, [letter_block_size, 0])
        output_string = "Score: " + str(gstat.score)
         
        # Blit to the screen
        text = font.render(output_string, True, BLACK)
         
        DISPLAYSURF.blit(text, [letter_block_size*7, 0])
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        frame_count += 1
        # Limit to 20 frames per second
        clock.tick(frame_rate)
      
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        

        pygame.display.update()
def valid((mousex, mousey),width_mat,hight_mat,width_frame,hight_frame):
    if width_frame<mousex<width_mat+width_frame and hight_frame<mousey<hight_mat+hight_frame:
        return True
    else:
        return False
def convert((mousex, mousey),width_frame,hight_frame,letter_block_size):
    i=int((mousex-width_frame)/letter_block_size)
    j=int((mousey-hight_frame)/letter_block_size)
    return (i,j)
def get_sticky(current_start,current_end):
    w_start=current_start
    norm_end_x=current_end[0]-current_start[0]
    norm_end_y=current_start[1]-current_end[1]
    if norm_end_x == 0:
        w_end=current_end
    else:
        w_end=[0,0]
        slope = norm_end_y/float(norm_end_x)
        print slope
        if abs(slope) in [0,1]:
            w_end=current_end
        else:
            if 0<slope<0.414:
                w_end[0]=current_end[0]
                w_end[1]=current_start[1]
            elif 0.414<=slope<1:
                w_end[0]=current_end[0]
                w_end[1]=current_start[1]-norm_end_x
            elif 1<slope<2.414:
                w_end[1]=current_end[1]
                w_end[0]=current_start[0]+norm_end_y
            elif 2.414<=slope:
                w_end[1]=current_end[1]
                w_end[0]=current_start[0]
            elif slope<=-2.414:
                w_end[1]=current_end[1]
                w_end[0]=current_start[0]
            elif -2.414<=slope<-1:
                w_end[1]=current_end[1]
                w_end[0]=current_start[0]-norm_end_y
            elif -1<slope<=-0.414:
                w_end[0]=current_end[0]
                w_end[1]=current_start[1]+norm_end_x
            elif -0.414<=slope<=0:
                w_end[0]=current_end[0]
                w_end[1]=current_start[1]

    return w_start,w_end 
# def AAfilledRoundedRect(surface,rect,color,radius=0.4):

#     """
#     AAfilledRoundedRect(surface,rect,color,radius=0.4)

#     surface : destination
#     rect    : rectangle
#     color   : rgb or rgba
#     radius  : 0 <= radius <= 1
#     """

#     rect         = pygame.Rect(rect)
#     color        = pygame.Color(*color)
#     alpha        = color.a
#     color.a      = 0
#     pos          = rect.topleft
#     rect.topleft = 0,0
#     rectangle    = pygame.Surface(rect.size,pygame.SRCALPHA)

#     circle       = pygame.Surface([min(rect.size)*3]*2,pygame.SRCALPHA)
#     pygame.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
#     circle       = pygame.transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

#     radius              = rectangle.blit(circle,(0,0))
#     radius.bottomright  = rect.bottomright
#     rectangle.blit(circle,radius)
#     radius.topright     = rect.topright
#     rectangle.blit(circle,radius)
#     radius.bottomleft   = rect.bottomleft
#     rectangle.blit(circle,radius)

#     rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
#     rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

#     rectangle.fill(color,special_flags=pygame.BLEND_RGBA_MAX)
#     rectangle.fill((255,255,255,alpha),special_flags=pygame.BLEND_RGBA_MIN)

#     return surface.blit(rectangle,pos)
def draw_lines(char_mat,DISPLAYSURF):

    
    for i in range(char_mat.n-1+2):
        pygame.draw.line(DISPLAYSURF, GRAY, (letter_block_size*(i+1), letter_block_size), (letter_block_size*(i+1), letter_block_size*(char_mat.n+1)))
    for i in range(char_mat.n-1+2):
        pygame.draw.line(DISPLAYSURF, GRAY, ( letter_block_size , letter_block_size *(i+1)), ( letter_block_size*(char_mat.n+1), letter_block_size*(i+1)))
def draw_chars(char_mat,DISPLAYSURF):
    fontObj = pygame.font.Font('freesansbold.ttf', int(letter_block_size*0.5))
    for i in range(char_mat.n):
        for j in range(char_mat.n):
            c=char_mat.get_char((i,j))
            textSurfaceObj = fontObj.render(c, True, BLUE)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (letter_block_size*(3/2.0+i), letter_block_size*(3/2.0+j))
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
def draw_words(char_mat,word_list,DISPLAYSURF):
    fontObjwords = pygame.font.Font('freesansbold.ttf',int(letter_block_size*0.75))
    y=0
    for w in word_list.words:
        if word_list.found[y]:
            colour_word=WHITE
        else:
            colour_word=BLACK
        textSurfaceObj = fontObjwords.render(w, True, colour_word)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (letter_block_size*(char_mat.n+3), letter_block_size*(3/2.0+y))
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        y=y+1
def highlight_char(DISPLAYSURF,(x,y),high_colour):
     # pygame.draw.circle(DISPLAYSURF, RED, (w_start[0]*letter_block_size+width_frame+letter_block_size/2, w_start[1]*letter_block_size+letter_block_size/2+hight_frame), 12, 2)
     #        pygame.draw.circle(DISPLAYSURF, RED, (w_end[0]*letter_block_size+width_frame+letter_block_size/2, w_end[1]*letter_block_size+letter_block_size/2+hight_frame), 12, 2)
     #        pygame.draw.line(DISPLAYSURF,RED,(w_start[0]*letter_block_size+width_frame+letter_block_size/2, w_start[1]*letter_block_size+letter_block_size/2+hight_frame),(w_end[0]*letter_block_size+width_frame+letter_block_size/2, w_end[1]*letter_block_size+letter_block_size/2+hight_frame))
    s = pygame.Surface((letter_block_size, letter_block_size))
    s.fill(WHITE)
    pygame.draw.circle(s, high_colour, (letter_block_size/2, letter_block_size/2), letter_block_size/2, 0)
    s.set_alpha(100)
    DISPLAYSURF.blit(s, (x,y))