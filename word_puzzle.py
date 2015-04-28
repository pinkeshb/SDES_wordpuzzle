#!/usr/bin/env python

import puzzlegui
import charmat
import word_list,gamestatus
import options_gui
import game_settings

level,dictionary,grid_size=options_gui.start_setup()
game_set=game_settings.game_settings(level,dictionary,grid_size)
# char_mat=charmat.CharMat()
char_mat=charmat.CharMat(grid_size)
a,b,c=game_set.calc_parameters()
word_list=word_list.word_list(a,b,c)
#word_list=word_list.word_list(10,4,15)
#word_list.single_fetch_word("words_out.txt")
word_list.single_fetch_word(game_set.dictionary+".txt")
#word_list.set_position()
word_list.set_position_level(game_set.level)
print word_list.words
print word_list.position
print word_list.direction
char_mat.set_all_words(word_list)
# char_mat.term_display()
char_mat.fill_characters_randomly("z")	

gstat=gamestatus.GameStatus(word_list,char_mat)	
puzzlegui.start(gstat)