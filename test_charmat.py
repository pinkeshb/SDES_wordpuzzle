import charmat
import unittest
class TestCharMatClass(unittest.TestCase):
	def setUp(self):
		pass
	def test_init(self):
		self.chararray=[' ']*15*15
		self.n=15
		C=charmat.CharMat()
		self.assertEqual((self.chararray,15),(C.chararray,C.n))
		self.chararray=[' ']*25*25
		self.n=25
		C =charmat.CharMat(25)
		self.assertEqual((self.chararray,25),(C.chararray,C.n))
	def test_set_word(self):
		self.chararray=[' ']*15*15
		self.n=15
		self.chararray[0:3]=['T','E','A']
		C =charmat.CharMat()
		C.set_word("TEA",(0,0),(2,0))
		self.assertEqual(self.chararray,C.chararray)

		self.chararray=[' ']*15*15
		self.n=15
		self.chararray[0]='T'
		self.chararray[16]='E'
		self.chararray[32]='A'
		C =charmat.CharMat()
		C.set_word("TEA",(0,0),(2,2))
		self.assertEqual(self.chararray,C.chararray)

		self.chararray=[' ']*15*15
		self.n=15
		self.chararray[95]='T'
		self.chararray[111]='E'
		self.chararray[127]='A'
		C =charmat.CharMat()
		C.set_word("TEA",(5,6),(7,8))
		self.assertEqual(self.chararray,C.chararray)

		self.assertRaises(ValueError,C.set_word,"TEA",(5,6),(8,8)) #invalid position

		self.assertRaises(ValueError,C.set_word,"TEA",(15,8),(15,10)) #invalid position

		self.assertRaises(ValueError,C.set_word,"TEAA",(5,6),(7,8)) #length doesn't match

		self.assertRaises(ValueError,C.set_word,"TEA",(0,0),(0,13)) #length doesn't match

	def test_get_word(self):
		C =charmat.CharMat()
		C.set_word("TEA",(5,6),(7,8))
		self.assertEqual( "TEA",C.get_word((5,6),(7,8)) )
		C.set_word("TEA",(5,6),(7,6))
		self.assertEqual( "TEA",C.get_word((5,6),(7,6)) )
		C.set_word("TEA",(5,6),(5,8))
		self.assertEqual( "TEA",C.get_word((5,6),(5,8)) )
		self.assertRaises(ValueError,C.get_word,(5,6),(8,8)) #invalid position
		self.assertRaises(ValueError,C.get_word,(15,6),(8,8) ) #invalid position

	def test_fill_characters_randomly(self):
		C=charmat.CharMat()
		C.fill_characters_randomly("asjf")
		self.assertTrue(not(" " in C.chararray))


if __name__ == '__main__':
    unittest.main()