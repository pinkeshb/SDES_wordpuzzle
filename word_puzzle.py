#!/usr/bin/env python

import puzzlegui
import charmat
import word_list
import gamestatus
import options_gui
import game_settings

level, dictionary, grid_size = options_gui.start_setup()
# frame.close()
game_set = game_settings.game_settings(level, dictionary, grid_size)
# char_mat=charmat.CharMat()
char_mat = charmat.CharMat(grid_size)
a, b, c = game_set.calc_parameters()

while(True):
    word_list1 = word_list.word_list(a, b, c)
    # word_list=word_list.word_list(10,4,15)
    # word_list.single_fetch_word("words_out.txt")
    word_list1.single_fetch_word(game_set.dictionary + ".txt")
    # word_list.set_position()
    word_list1.set_position_level(game_set.level)
    print word_list1.words
    print word_list1.position
    print word_list1.direction
    if word_list1.success == True:
        break
    else:
        pass
        # sys.exit()
        # continue
char_mat.set_all_words(word_list1)
# char_mat.term_display()
if level != 2:
    char_mat.fill_characters_randomly("z")
else:
    charlist = "".join(word_list1.words)
    charset = set(charlist)
    charlist = list(charset)
    stringchar = "".join(charlist).upper()
    char_mat.fill_characters_randomly(stringchar.lower())


gstat = gamestatus.GameStatus(word_list1, char_mat)
puzzlegui.start(game_set,gstat, level)
