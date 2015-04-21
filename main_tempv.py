import
#import statements
while(1)
#Starting the option GUI
Gset=option_gui.start()
Gset.generateParameters()
# Createing the Game Initial Stage
W=word_list(Gset)
# inside constrcutor.. W.single_fetch_word("gset.dict"), W.set_position()
C=charmat(Gset,W)
# inside constructur.. C.set_words(W) C.random
G=gameStatus(C,W)

#Display of Game starts
puzzle_gui.start(Gset,G) 
}


#___________________________
# Module puzzle_gui

	

# getting the parameters

# from gset letter_block_size=50
# calculated from letter block size #Word_block_size=100
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)
GRAY = (200,200,200)
fontObj = pygame.font.Font('freesansbold.ttf', 100)

#generating the display

pygame.init()
DISPLAYSURF = pygame.display.set_mode(((C.n+2)*letter_block_size,(C.n+2)*letter_block_size+Word_block_size))
pygame.display.set_caption('Word Puzzle!')


# creating grid
DISPLAYSURF.fill(WHITE)
for i in range(C.n-1+2):
	pygame.draw.line(DISPLAYSURF, GRAY, (letter_block_size*(i+1), letter_block_size), (letter_block_size*(i+1), letter_block_size*(C.n+1)))
for i in range(C.n-1+2):
	pygame.draw.line(DISPLAYSURF, GRAY, ( letter_block_size , letter_block_size *(i+1)), ( letter_block_size*(C.n+1), letter_block_size*(i+1)))

# 	set DISPLAYSURF with C and W and G
# for every character do this
		c='a'
		textSurfaceObj = fontObj.render(c, True, BLACK)
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (letter_block_size*3/2.0, letter_block_size*3/2.0)
		DISPLAYSURF.blit(textSurfaceObj, textRectObj)

# displaying words
# from W


#display copy


while True: # main game loop
	
    for event in pygame.event.get():
# mouse drag and select
        if mouse down event
        	if valid M_1
        		P_1=convert(M_1)
        		start=true
        if start and mouse move
        	if valid M_j
        		P_j=convert(M_j) 
        		highlight(P_j,P_1)(sticky direction)
        if start and mouse up 
        	if valid M_2
        		M_2=convert(P_2)
        		highlight
        		time.sleep(0.1sec)
        	   	G.check_word(P_2,P_1)
        	   	if check G.success
        	   		display success and time left
        	   	if check G.timeout
        	   		display score and time out
        	   	update the display (Display_copy,G.W,)

        		

    	# if bool ==True 
    	# 	if left click
    	# 		if valid
    	# 			call chech_fun()
    	# # 			if valid update display(green colour word + strike of the word)
     #    if event.type == MOUSEBUTTONUP:
     #        mousex, mousey = event.pos
     #        if (letter_block_size<=mousex<=letter_block_size*C.n) and (letter_block_size<=mousey<=letter_block_size*C.n):
     #        	Started=True
     #            pygame.quit()
     #            # sys.exit()
     #            # x_b=mousex/
     #        	# compllte it
     #            print "ggvtg"
     #            sys.exit()
        # if left click
        # 	if valid
        # 		bool = True
        # 		S=cursor
        # 		update display with selected letter

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

