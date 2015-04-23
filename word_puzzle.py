#!/usr/bin/env python

import puzzlegui
import charmat
import word_list,gamestatus
char_mat=charmat.CharMat()
word_list=word_list.word_list(4,10,15)
word_list.single_fetch_word("words_out.txt")
word_list.set_position()
print word_list.words
print word_list.position
print word_list.direction
char_mat.set_all_words(word_list)
# char_mat.term_display()
char_mat.fill_characters_randomly("z")	

gstat=gamestatus.GameStatus(word_list,char_mat)	
puzzlegui.start(gstat)