import random
from operator import itemgetter

class word_list(object):
	def __init__(self,count,maxl,n):
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
		fin=open(fileinput)
		
		countstring=fin.next()
		count=map(int,countstring.split())
		countnum=sum(count[:self.max_length])
		wordspace=[]
		for i in range(countnum):
			wordspace.append(fin.next().strip('\n'))
			#print wordspace[i]
			
		for j in range(self.count):
			self.words.append(wordspace.pop(random.randrange(0,countnum)))
		self.length=map(len,self.words)
	def set_position(self):
		temp_list=[]
		i1=0
		for i in self.words:
			temp_list.append([])
			temp_list[i1]=[i,len(i)]
			i1+=1
		temp_list.sort(key=itemgetter(1), reverse=True)
		direction_inc=[[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
		first_word_dir=[[2,4],[4,6],[6,0],[0,2]]
		second_word_dir=[[2,3,4],[4,5,6],[6,7,0],[0,1,2]]
		quad_start=[[0,0],[0,self.matrix_size-1],[self.matrix_size-1,self.matrix_size-1],[self.matrix_size-1,0]]
		matrix=[]
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
			while(current_success==0 and itera<=10):
				x,y=generate_start_pos(self.matrix_size)
				current_quad=find_quadrant(x,y,self.matrix_size)
				r2_dir=random.randrange(0,3)
				current_dir=second_word_dir[current_quad][r2_dir]
				current_success=word_hit_or_miss(x,y,temp_list[i3][1],direction_inc[current_dir],matrix)
				itera+=1



			self.position.append([x,y])
			self.direction.append(current_dir)
			self.words.append(temp_list[i3][0])
			self.length.append(temp_list[i3][1])
			matrix=matrix_superimpose(matrix,self.position[i3],direction_inc[self.direction[i3]],self.length[i3])
		if len(self.words)==self.count:
			self.success=True

def find_quadrant(x,y,n):
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
	i,j=pos[0],pos[1]
	for i1 in range(l):
		matrix[i][j]=1
		i,j=i+inc[0],j+inc[1]
	return matrix

def generate_start_pos(n):
	return random.randrange(n),random.randrange(n)

# if __name__=="__main__"