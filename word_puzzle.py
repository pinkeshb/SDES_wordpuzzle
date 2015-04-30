#!/usr/bin/env python

import puzzlegui
import charmat
import word_list
import gamestatus
import options_gui
import game_settings

level, dictionary, grid_size = options_gui.start_setup()
game_set = game_settings.game_settings(level, dictionary, grid_size)
char_mat = charmat.CharMat(grid_size)
a, b, c = game_set.calc_parameters()
while(True):
    word_list1 = word_list.word_list(a, b, c)
    word_list1.single_fetch_word(game_set.dictionary)
    word_list1.set_position_level(game_set.level)
    print word_list1.words
    print word_list1.position
    print word_list1.direction
    if word_list1.success == True:
        break
char_mat.set_all_words(word_list1)
char_mat.fill_characters_randomly(word_list1.words, game_set.level)
gstat = gamestatus.GameStatus(word_list1, char_mat)
puzzlegui.start(game_set, gstat, level)
