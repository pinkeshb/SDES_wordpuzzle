from random import randint
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
		 # validity checking
		if not( 0 <= x_start <=self.n and 0 <= x_end <=self.n and 0 <= y_start <=self.n and 0 <= y_end <=self.n):
			raise	ValueError

		 # horz and vert direction words 
		word=[]
		if x_start==x_end:
			if y_start<y_end:
				for i in range(y_start,y_end+1):
					word.append(self.chararray[x_start+i*self.n])
				return "".join(word)

			else:
				for i in range(y_start,y_end+1):
					word.append(self.chararray[x_start+i*self.n])
					word.reverse()
				return "".join(word)
		if y_start==y_end:
			if x_start<x_end:
				for i in range(x_start,x_end+1):
					word.append(self.chararray[y_start*self.n+i])
				return "".join(word)
			else:
				for i in range(x_start,x_end+1):
					word.append(self.chararray[y_start*self.n+i])
					word.reverse()
				return "".join(word)

		 # validity chararray for diagonal words 
		if not(abs(x_start-x_end) == abs(y_start-y_end)):
			raise ValueError

		 # diagonal words
		for i in range(abs(x_start-x_end)+1):
			word.append(self.chararray[ 
				( x_start+i*(x_end- x_start)/abs(x_end- x_start) ) 
				+ (y_start+i*(y_end- y_start)/abs(y_end- y_start)) *self.n  
			])

		return "".join(word)

	def set_word(self,word,(x_start,y_start),(x_end,y_end)):
		"""set word in matrix form start to end coordinates 
		after checking validity of coordinates"""
		if not( 0 <= x_start <self.n and 0 <= x_end <self.n and 0 <= y_start <self.n and 0 <= y_end <self.n):
			raise	ValueError
		if x_start == x_end:
			if abs(y_start-y_end) == (len(word)-1):
				for i in range(len(word)):
					self.chararray[x_start + (y_start+i*(y_end- y_start)/abs(y_end- y_start)) *self.n  ] = word[i]
				return
			else:
				raise ValueError
		if y_start == y_end:
			if abs(x_start-x_end) == (len(word)-1):
				for i in range(len(word)):
					self.chararray[y_start*self.n + (x_start+i*(x_end- x_start)/abs(x_end- x_start)) ] = word[i]
				return 
			else:
				raise ValueError
		if not( abs(x_start-x_end) == abs(y_start-y_end)== (len(word)-1)):
			raise ValueError

		for i in range(len(word)):
			self.chararray[ 
				( x_start+i*(x_end- x_start)/abs(x_end- x_start) ) 
				+ (y_start+i*(y_end- y_start)/abs(y_end- y_start)) *self.n  
			] = word[i]


	def fill_characters_randomly(self,string):
		"""fills all the spaces in matrix with randomly selected 
		characters form string"""
		for i in range(self.n*self.n):
			if self.chararray[i]==' ':
				self.chararray[i]= string[randint(0,len(string)-1)]
	def term_display(self):
		"""display matrix on terminal"""
		print self.n,"*",self.n, "puzzle"
		for i in range(self.n):
			for j in range(self.n):
				print self.chararray[j+i*self.n],
			print " "


# HOW TO USE IT



# C=CharMat(5)
# C.set_word("teap",(0,0),(3,3))
# C.fill_characters_randomly("gz")
# C.term_display()