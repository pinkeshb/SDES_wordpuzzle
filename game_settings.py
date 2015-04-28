class game_settings(object):
	def __init__(self,level=0,dictionary="Animals",grid=8):
		self.level=level
		self.dictionary=dictionary
		self.matrix_size=grid
		self.letter_block_size=26
		self.word_block_size=100
		self.params=[]
	def calc_parameters(self):
		self.params=[[(6,8),(8,12),(8,12)],[(8,8),(10,12),(10,12)]]#word length, no of ords, 
		if self.matrix_size==8:
			row_index=0
		else:
			row_index=1

		return self.params[row_index][self.level][0],self.params[row_index][self.level][1],self.matrix_size