import random
from operator import itemgetter

class word_list(object):
	def __init__(self,count,maxl,n):
		'''words, length, position, direction in self are in respective order. that is first len, dir, position corresponds to  first word,  eg. cat, 3 , 0,0 , 2'''
		self.words=[]
		self.length=[]
		self.position=[]
		self.direction=[]
		self.max_length=maxl
		self.count=count
		self.level=0
		self.matrix_size=n
		self.success=False
	def single_fetch_word(self,fileinput):
		''' From the input file, first builds a list of words which satisy the given parameters , say max 6 length words
		and from them randomly picks eg.10 no. of words. 
		Input: a file name 
		return: set of words in a list <= given max length  '''
		fin=open(fileinput)
		
		countstring=fin.next().strip('\n')
		count=map(int,countstring.split())
		countnum=sum(count[:self.max_length])
		#print countnum
		wordspace=[]
		for i in range(countnum):
			wordspace.append(fin.next().strip('\n'))
			#print wordspace[i]
			
		for j in range(self.count):
			self.words.append(wordspace.pop(random.randrange(0,countnum-j)))# while popping, for next time randrange limit should be decreased
		self.length=map(len,self.words)
	def set_position(self):
		'''generates the postions for the words
		''' 
		temp_list=[]#stores [word, word_len] eg. [cat,3]
		i1=0
		for i in self.words:
			temp_list.append([])
			temp_list[i1]=[i,len(i)]
			i1+=1
		temp_list.sort(key=itemgetter(1), reverse=True)#sort the words in decreasing order of length
		direction_inc=[[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
		first_word_dir=[[2,4],[4,6],[6,0],[0,2]]# possible directions for the respective quadrant 
		#Ignoring diagnol directions
		second_word_dir=[[2,3,4],[4,5,6],[6,7,0],[0,1,2]]# possible directions for all words except the first one for the respective quadrant
		quad_start=[[0,0],[0,self.matrix_size-1],[self.matrix_size-1,self.matrix_size-1],[self.matrix_size-1,0]]
		matrix=[]# matrix will be filled with 1's , wherever words are fitted
		for i2 in range(self.matrix_size):
			matrix.append(self.matrix_size*[0])
		# for First longest word, different processing
		r1_quad=random.randrange(0,4)
		r1_dir=random.randrange(0,2)
		self.words=[]
		self.length=[]
		self.position.append(quad_start[r1_quad])
		self.direction.append(first_word_dir[r1_quad][r1_dir])
		self.words.append(temp_list[0][0])
		self.length.append(temp_list[0][1])
		matrix=matrix_superimpose(matrix,self.position[0],direction_inc[self.direction[0]],self.length[0])
		for i3 in range(1,self.count):
			current_success=0
			itera=0
			while(current_success==0 and itera<=20):
				x,y=generate_start_pos(self.matrix_size)
				current_quad=find_quadrant(x,y,self.matrix_size)
				r2_dir=random.randrange(0,3)
				current_dir=second_word_dir[current_quad][r2_dir]
				current_success=word_hit_or_miss(x,y,temp_list[i3][1],direction_inc[current_dir],matrix)
				itera+=1


			if current_success==0: #if all 20 start positions fail, then words list can't be fit into this matrix
				break	
			self.position.append([x,y])
			self.direction.append(current_dir)
			self.words.append(temp_list[i3][0])
			self.length.append(temp_list[i3][1])
			matrix=matrix_superimpose(matrix,self.position[i3],direction_inc[self.direction[i3]],self.length[i3])
		if len(self.words)==self.count:
			self.success=True
		return matrix
			#it will stay false, if 20 itearaions had failed for a word

def find_quadrant(x,y,n):
	'''Finds the quadrant , in which the given point x,y lies
	returns: 0,1,2,3 (quadrant no.)'''
	if x<n/2 :
		if y<n/2:
			return 0
		else:
			return 1
	else:
		if y<n/2:
			return 3
		else:
			return 2


def word_hit_or_miss(x,y,l,inc,matrix):
	'''Checks whether a word of length l can be fitted in the given direction inc.
	Input: start position, length, direction_increment
	Returns: 1, if we can fit'''
	i,j=x,y
	flag=0
	n=len(matrix)
	for i1 in xrange(l):
		if i>=n or j>=n or matrix[i][j]==1:
			flag=1
			break
		else:
			i,j=i+inc[0],j+inc[1]
	if flag==1:
		return 0
	else:
		return 1

def matrix_superimpose(matrix,pos,inc,l):
	'''fills 1's in the given word positions
	returns: the matrix with superimposed 1s'''
	i,j=pos[0],pos[1]
	for i1 in range(l):
		matrix[i][j]=1
		i,j=i+inc[0],j+inc[1]
	return matrix

def generate_start_pos(n):
	'''Genertaes starting positions between [1,n]'''
	return random.randrange(n),random.randrange(n)

# if __name__=="__main__"