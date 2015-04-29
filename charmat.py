from random import randint


DEFAULT_SIZE = 15


class CharMat(object):

    def __init__(self, n=DEFAULT_SIZE):
        """adds size of puzzle n and character array to object,
        fills matrix with spaces
        """
        self.char_array = [' '] * n * n
        self.n = n

    def get_word(self, (x_start, y_start), (x_end, y_end)):
        """returns word from matrix form start to end coordinates 
        after checking validity of coordinates
        """
        word = []

        # validity checking
        if not((0 <= x_start <= self.n and 0 <= x_end <= self.n) and
               (0 <= y_start <= self.n and 0 <= y_end <= self.n)):
            raise ValueError

          # horz and vert direction words
        if x_start == x_end:
            if y_start < y_end:
                for i in range(y_start, y_end + 1):
                    word.append(self.get_char((x_start, i)))
                print "".join(word), "charm"
                return "".join(word)

            else:
                for i in range(y_end, y_start + 1):
                    word.append(self.get_char((x_start, i)))
                word.reverse()
                print "".join(word), "charm"
                return "".join(word)
        if y_start == y_end:
            if x_start < x_end:
                for i in range(x_start, x_end + 1):
                    word.append(self.get_char((i, y_start)))
                print "".join(word), "charm"
                return "".join(word)
            else:
                for i in range(x_end, x_start + 1):
                    word.append(self.get_char((i, y_start)))
                word.reverse()
                print "".join(word), "charm"
                return "".join(word)

         # diagonal words
        if not(abs(x_start - x_end) == abs(y_start - y_end)):
            raise ValueError
        for i in range(abs(x_start - x_end) + 1):
            word.append(self.get_char((x_start + i * (x_end - x_start) / abs(
                x_end - x_start), y_start + i * (y_end - y_start) / abs(
                y_end - y_start))))
        print "".join(word), "charm"
        return "".join(word)

    def set_word(self, word, (x_start, y_start), (x_end, y_end)):
        """set word in matrix from start to end coordinates 
        after checking validity of coordinates
        """
        # validity check
        if not((0 <= x_start < self.n and 0 <= x_end < self.n) and
               (0 <= y_start < self.n and 0 <= y_end < self.n)):
            raise ValueError

          # horz and vert direction words
        if x_start == x_end:
            if abs(y_start - y_end) == (len(word) - 1):
                for i in range(len(word)):
                    self.char_array[x_start + (y_start + i * (y_end - y_start)
                                    / abs(y_end - y_start)) * self.n] = word[i]
                return
            else:
                raise ValueError
        if y_start == y_end:
            if abs(x_start - x_end) == (len(word) - 1):
                for i in range(len(word)):
                    self.char_array[y_start * self.n +
                                    (x_start + i * (x_end - x_start) /
                                     abs(x_end - x_start))] = word[i]
                return
            else:
                raise ValueError

          # diagonal words
        if not(abs(x_start - x_end) == abs(y_start - y_end) ==
               (len(word) - 1)):
            raise ValueError
        for i in range(len(word)):
            self.char_array[
                (x_start + i * (x_end - x_start) / abs(x_end - x_start)) +
                (y_start + i * (y_end - y_start) / abs(y_end - y_start))
                * self.n] = word[i]

    def fill_characters_randomly(self, string):
        """fills all the spaces in matrix with randomly selected 
        characters form string
        """
        for i in range(self.n * self.n):
            if self.char_array[i] == ' ':
                self.char_array[i] = string[randint(0, len(string) - 1)]

    def term_display(self):
        """display matrix on terminal"""
        print self.n, "*", self.n, "puzzle"
        for i in range(self.n):
            for j in range(self.n):
                print self.char_array[j + i * self.n],
            print " "

    def get_char(self, (x, y)):
        """return character corresponding to x and y"""
        return self.char_array[x + y * self.n]

    def set_all_words(self, word_list):
        """set word in matrix from start to end coordinates 
        after checking validity of coordinates
        """
        for i in range(len(word_list.words)):
            word = word_list.words[i].upper()
            start, end = word_list.get_start_end_xy(i)
            self.set_word(word, start, end)
# HOW TO USE IT


# C=CharMat(5)
# C.set_word("teap",(0,0),(3,3))
# C.fill_characters_randomly("gz")
# C.term_display()
# print C.get_char((0,0))
