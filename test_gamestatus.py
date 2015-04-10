import unittest
from gamestatus import GameStatus
from charmat import CharMat
from word_list import word_list as WordList

class TestCharMatClass(unittest.TestCase):


    def setUp(self):
        pass

    def test_init(self):
        char_mat=CharMat()
        word_list=WordList()
        game_status=GameStatus(char_mat,word_list)
        self.assertEqual(game_status.word_list,word_list)
        self.assertEqual(game_status.char_mat,char_mat)
        self.assertEqual(game_status.score,0)
        self.assertEqual(game_status.time,60)
        self.assertEqual(game_status.times_up,False)
        self.assertEqual(game_status.success,False)

    def test_check_word():
        # create all game like variable
        char_mat=CharMat()
        char_mat.set_word("hello",(4,4),(0,0))
        word_list=WordList()
        game_status=GameStatus(char_mat,word_list)
        # 1. -1 =times up
        # 2. repeated word
        # 3. correct word
        # 4. wrong word
if __name__  == '__main__':
    unittest.main()
