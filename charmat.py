DEFAULT_n=15
class CharMat(object):
	def __init__(self,n=DEFAULT_n):
		"""adds size of puzzle n and character array to object,
		fills matrix with spaces"""
		self.chararray=[' ']*n*n
		self.n=n
	def get_word(self,(x_start,y_start),(x_end,y_end)):
		"""returns word from matrix form start to end coordinates 
		after checking validity of coordinates"""
		pass 
	def set_word(self,word,(x_start,y_start),(x_end,y_end)):
		"""set word in matrix form start to end coordinates 
		after checking validity of coordinates"""
		pass
	def fill_characters_randomly(self,string):
		"""fills all the spaces in matrix with randomly selected 
		characters form string"""
		pass
	def term_display(self):
		"""display matrix on terminal"""
		pass