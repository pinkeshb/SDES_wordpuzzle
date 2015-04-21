
import pygame,sys


#___________________________
# Module puzzle_gui

	

# getting the parameters

# from gset letter_block_size=50
# calculated from letter block size #Word_block_size=100
def start(char_mat):#Gset,Gstat
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    RED = (255,   0,   0)
    GREEN = (  0, 255,   0)
    BLUE = (  0,   0, 255)
    GRAY = (200,200,200)
    LEFT=1
    letter_block_size=25
    Word_block_size=100
    # matrix size
    width_mat=(char_mat.n)*letter_block_size 
    hight_mat=(char_mat.n)*letter_block_size
    # frame size = 1
    width_frame=letter_block_size
    hight_frame=letter_block_size
    # word block size at bottom
    hight_words=Word_block_size

    width=2*width_frame+width_mat
    hight=2*hight_frame+hight_mat+hight_words
    #generating the display
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((width,hight))
    pygame.display.set_caption('Word Puzzle!')


    # creating grid
    DISPLAYSURF.fill(WHITE)
    for i in range(char_mat.n-1+2):
    	pygame.draw.line(DISPLAYSURF, GRAY, (letter_block_size*(i+1), letter_block_size), (letter_block_size*(i+1), letter_block_size*(char_mat.n+1)))
    for i in range(char_mat.n-1+2):
    	pygame.draw.line(DISPLAYSURF, GRAY, ( letter_block_size , letter_block_size *(i+1)), ( letter_block_size*(char_mat.n+1), letter_block_size*(i+1)))

    # 	set DISPLAYSURF with C and W and G
    # for every character do this
    fontObj = pygame.font.Font('freesansbold.ttf', int(letter_block_size*0.5))
    for i in range(char_mat.n):
        for j in range(char_mat.n):
                c=char_mat.get_char((i,j))
                textSurfaceObj = fontObj.render(c, True, BLUE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (letter_block_size*(3/2.0+i), letter_block_size*(3/2.0+j))
                DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    # c='a'
    # textSurfaceObj = fontObj.render(c, True, BLACK)
    # textRectObj = textSurfaceObj.get_rect()
    # textRectObj.center = (letter_block_size*(3/2.0+i), letter_block_size*(3/2.0+i))
    # DISPLAYSURF.blit(textSurfaceObj, textRectObj)


    # displaying words
    # from W


    #display copy

    start = False
    while True: # main game loop
        for event in pygame.event.get():
    # mouse drag and select
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:        
            	if valid(event.pos,width_mat,hight_mat,width_frame,hight_frame):
                    P_1=convert(event.pos,width_frame,hight_frame,letter_block_size)
                    start=True

                    pygame.draw.circle(DISPLAYSURF, RED, (P_1[0]*letter_block_size+width_frame+letter_block_size/2, P_1[1]*letter_block_size+letter_block_size/2+hight_frame), 12, 2)
                    # print P_1
            if start and event.type == pygame.MOUSEMOTION:
                
            	if valid(event.pos,width_mat,hight_mat,width_frame,hight_frame):
                    P_j=convert(event.pos,width_frame,hight_frame,letter_block_size)
                    # pygame.draw.line(DISPLAYSURF,GREEN,(P_1[0]*letter_block_size+width_frame+letter_block_size/2, P_1[1]*letter_block_size+letter_block_size/2+hight_frame),(P_j[0]*letter_block_size+width_frame+letter_block_size/2, P_j[1]*letter_block_size+letter_block_size/2+hight_frame))
            		
            if start and event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:     
            	if valid(event.pos,width_mat,hight_mat,width_frame,hight_frame):
                    P_2=convert(event.pos,width_frame,hight_frame,letter_block_size)
                    print P_2
                    print P_1
                    start = False
                    pygame.draw.circle(DISPLAYSURF, RED, (P_2[0]*letter_block_size+width_frame+letter_block_size/2, P_2[1]*letter_block_size+letter_block_size/2+hight_frame), 12, 2)
                    pygame.draw.line(DISPLAYSURF,GREEN,(P_1[0]*letter_block_size+width_frame+letter_block_size/2, P_1[1]*letter_block_size+letter_block_size/2+hight_frame),(P_2[0]*letter_block_size+width_frame+letter_block_size/2, P_2[1]*letter_block_size+letter_block_size/2+hight_frame))
                    # AAfilledRoundedRect(DISPLAYSURF,(0,0,10,10),WHITE,0.2)

            		# highlight
            		# time.sleep(0.1sec)
            	   	# G.check_word(P_2,P_1)
            	   	# if check G.success
            	   	# 	display success and time left
            	   	# if check G.timeout
            	   	# 	display score and time out
            	   	# update the display (Display_copy,G.W,)

        	# if bool ==True 
        	# 	if left click
        	# 		if valid
        	# 			call chech_fun()
        	# # 			if valid update display(green colour word + strike of the word)
         #    if event.type == MOUSEBUTTONUP:
         #        mousex, mousey = event.pos
         #        if (letter_block_size<=mousex<=letter_block_size*char_mat.n) and (letter_block_size<=mousey<=letter_block_size*char_mat.n):
         #        	Started=True
         #            pygame.quit()
         #            # sys.exit()
         #            # x_b=mousex/
         #        	# compllte it
         #            print "ggvtg"
         #            sys.exit()
         #    if left click
         #    	if valid
         #    		bool = True
         #    		S=cursor
         #    		update display with selected letter
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
def AAfilledRoundedRect(surface,rect,color,radius=0.4):

    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect         = pygame.Rect(rect)
    color        = pygame.Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = pygame.Surface(rect.size,pygame.SRCALPHA)

    circle       = pygame.Surface([min(rect.size)*3]*2,pygame.SRCALPHA)
    pygame.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = pygame.transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=pygame.BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=pygame.BLEND_RGBA_MIN)

    return surface.blit(rectangle,pos)
