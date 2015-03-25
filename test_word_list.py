import word_list as wl
import unittest
import sys
import math

class TestwordList(unittest.TestCase):
	def setUp(self):
		self.sport=wl.word_list(2,3,6)
		self.sport.single_fetch_word("words_out.txt")
		
		
	def tearDown(self):
		pass

	
	def test_words_count(self):	
		
		self.assertEqual(len(self.sport.words),2)
		
	# def test_space_matrix(self):
	def test_words_max_length(self):
		maxl=0
		for i in self.sport.words:
			maxl=max(maxl,len(i))
			# print i
		
		self.assertTrue(maxl<=3)


class TestwordHitOrMiss(unittest.TestCase):
	def setUp(self):
		self.matrix=[[0,1,1],[0,0,0],[1,1,0]]
		pass
		
		
	def tearDown(self):
		pass

	
	def test_wordhit_overflow(self):
		self.assertEqual(wl.word_hit_or_miss(1,1,10,[0,1],self.matrix),0)
	def test_wordhit_hit(self):
		self.assertEqual(wl.word_hit_or_miss(1,1,2,[1,0],self.matrix),0)
	def test_wordhit_miss(self):
		self.assertEqual(wl.word_hit_or_miss(1,1,2,[0,1],self.matrix),1)

class TestMatrix_superimpose(unittest.TestCase):
	def setUp(self):
		self.matrix=[[0,1,1],[0,0,0],[1,1,0]]
		pass
		
	def tearDown(self):
		pass
	
	def test_mat_superimpose(self):
		
		self.assertEqual(wl.matrix_superimpose(self.matrix,[1,1],[0,-1],2),[[0,1,1],[1,1,0],[1,1,0]])
	def test_mat_superimpose(self):
		
		self.assertEqual(wl.matrix_superimpose(self.matrix,[1,1],[1,0],2),[[0,1,1],[0,1,0],[1,1,0]])
class TestwordList_setPosition(unittest.TestCase):
	def setUp(self):
		self.sport=wl.word_list(2,3,6)
		self.sport.single_fetch_word("words_out.txt")
		self.sport.set_position()
		self.inc=[[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
	def tearDown(self):
		pass

	def test_set_positions_no_intersection(self):
		pos=[]
		[i,j]=self.sport.position[0]
		dir0 = self.sport.direction[0]
		for i in range(self.sport.length[0]):
			pos.append([i,j])
			i,j=i+self.inc[dir0][0],j+self.inc[dir0][1]
		[i,j]=self.sport.position[1]
		dir1 = self.sport.direction[1]
		for i1 in range(self.sport.length[1]):
			self.assertFalse([i,j] in pos)
			i,j=i+self.inc[dir1][0],j+self.inc[dir1][1]


	

if __name__ =='__main__':
	unittest.main()