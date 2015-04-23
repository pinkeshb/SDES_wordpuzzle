class GameStatus(object):


    def __init__(self,word_list,char_mat):
        """Initialize the score = 0, word_list, char_mat, time = 60,
        success=False, times_up=False"""
        self.word_list=word_list
        self.word_list.found=[False]*len(word_list.words)
        self.char_mat=char_mat
        self.score=0
        self.time=60
        self.success=False
        self.times_up=False

    def check_word(self,p_1,p_2):
        """Checks if word corresponding to p_1, p_2 is correct. 
        And accordingly updates the word_list, score, success
        if p_1==p_2==-1(indicating time's up) then updates the times_up
        """ 
        # times_up case
        if p_1==(-1,-1) and p_2==(-1,-1):
        	self.times_up=True
        else:

        # correctness
            try:
                user_selected_word=self.char_mat.get_word(p_1,p_2).lower()
            except ValueError:
                return
            print user_selected_word
            if user_selected_word in self.word_list.words and not self.word_list.found[self.word_list.words.index(user_selected_word)]:
                self.score=self.score+10
                self.word_list.found[self.word_list.words.index(user_selected_word)]=True
                if not(False in self.word_list.found):
                    self.success=True
        # self.char_mat.term_display()


