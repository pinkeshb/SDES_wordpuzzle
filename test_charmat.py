import charmat
import unittest


class TestCharMatClass(unittest.TestCase):


    def setUp(self):
        pass

    def test_init(self):
        self.char_array = [' ']*15*15
        self.n = 15
        char_mat = charmat.CharMat()
        self.assertEqual((self.char_array, 15),
                         (char_mat.char_array, char_mat.n))
        self.char_array = [' ']*25*25
        self.n = 25
        char_mat = charmat.CharMat(25)
        self.assertEqual((self.char_array, 25),
                         (char_mat.char_array, char_mat.n))

    def test_set_word(self):
        self.char_array = [' ']*15*15
        self.n = 15
        self.char_array[0:3] = ['T', 'E', 'A']
        char_mat =  charmat.CharMat()
        char_mat.set_word("TEA", (0, 0), (2, 0))
        self.assertEqual(self.char_array, char_mat.char_array)

        self.char_array = [' ']*15*15
        self.n = 15
        self.char_array[0] = 'T'
        self.char_array[16] = 'E'
        self.char_array[32] = 'A'
        char_mat =  charmat.CharMat()
        char_mat.set_word("TEA", (0, 0), (2, 2))
        self.assertEqual(self.char_array, char_mat.char_array)

        self.char_array = [' ']*15*15
        self.n = 15
        self.char_array[95] = 'T'
        self.char_array[111] = 'E'
        self.char_array[127] = 'A'
        char_mat =  charmat.CharMat()
        char_mat.set_word("TEA", (5, 6), (7, 8))
        self.assertEqual(self.char_array, char_mat.char_array)

        # invalid position
        self.assertRaises(ValueError, char_mat.set_word, 
                          "TEA", (5, 6), (8, 8))

        # invalid position
        self.assertRaises(ValueError, char_mat.set_word, 
                          "TEA", (15, 8), (15, 10))

        # length doesn't match
        self.assertRaises(ValueError, char_mat.set_word, 
                          "TEAA", (5, 6), (7, 8))

        # length doesn't match
        self.assertRaises(ValueError, char_mat.set_word, 
                          "TEA", (0, 0), (0, 13))

    def test_get_word(self):
        char_mat =  charmat.CharMat()
        char_mat.set_word("TEA", (5, 6), (7, 8))
        self.assertEqual("TEA", char_mat.get_word((5, 6), (7, 8)))
        char_mat.set_word("TEA", (5, 6), (7, 6))
        self.assertEqual("TEA", char_mat.get_word((5, 6), (7, 6)))
        char_mat.set_word("TEA", (5, 6), (5, 8))
        self.assertEqual("TEA", char_mat.get_word((5, 6), (5, 8)))
        # invalid position
        self.assertRaises(ValueError, char_mat.get_word, (5, 6), (8, 8))
        # invalid position
        self.assertRaises(ValueError, char_mat.get_word, (15, 6), (8, 8))

    def test_fill_characters_randomly(self):
        char_mat =  charmat.CharMat()
        char_mat.fill_characters_randomly("asjf")
        self.assertTrue(not(" " in char_mat.char_array))

    def test_get_char(self):
        char_mat =  charmat.CharMat()
        char_mat.set_word("QWERTYUIOPASDFG", (0, 0), (14, 14))
        self.assertEqual(char_mat.get_char((0, 0)), 'Q')
        self.assertEqual(char_mat.get_char((14, 14)), 'G')
        self.assertEqual(char_mat.get_char((4, 4)), 'T')
        self.assertEqual(char_mat.get_char((10, 10)), 'A')
if __name__  == '__main__':
    unittest.main()
