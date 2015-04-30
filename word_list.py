import random
from operator import itemgetter


class word_list(object):

    def __init__(self, maxl, count, n):
        '''words, length, position, direction in self are in respective order. that is first len, dir, position corresponds to  first word,  eg. cat, 3 , 0,0 , 2'''
        self.words = []
        self.length = []
        self.position = []
        self.direction = []
        self.max_length = maxl
        self.count = count
        self.level = 0
        self.matrix_size = n
        self.success = False

    def single_fetch_word(self, fileinput):
        ''' From the input file, first builds a list of words which satisy the given parameters , say max 6 length words
        and from them randomly picks eg.10 no. of words. 
        Input: a file name 
        return: set of words in a list <= given max length  '''
        fin = open(fileinput+".txt")
        countstring = fin.next().strip('\n')
        count = map(int, countstring.split())
        countnum = sum(count[:self.max_length])
        wordspace = []
        for i in range(countnum):
            wordspace.append(fin.next().strip('\n'))
        for j in range(self.count):
            # while popping, for next time randrange limit should be decreased
            self.words.append(wordspace.pop(random.randrange(0, countnum - j)))
        self.length = map(len, self.words)

    def set_position_level(self, level):
        '''generates the postions for the words, for differnet levels
        '''
        self.level = level
        if level == 0:
            self.set_position()
        if level == 1:
            self.set_position1()
        if level == 2:
            self.set_position1()

    def set_position(self):
        '''generates the postions for the words
        '''
        temp_list = []
        i1 = 0
        for i in self.words:
            temp_list.append([])
            temp_list[i1] = [i, len(i)]
            i1 += 1
        # sort the words in decreasing order of length
        temp_list.sort(key=itemgetter(1), reverse=True)
        direction_inc = [
            [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        # possible directions for the respective quadrant
        first_word_dir = [[2, 4], [4, 6], [6, 0], [0, 2]]
        # Ignoring diagnol directions
        # possible directions for all words except the first one for the
        # respective quadrant
        second_word_dir = [[2, 3, 4], [4, 5, 6], [6, 7, 0], [0, 1, 2]]
        quad_start = [[0, 0], [0, self.matrix_size - 1],
                      [self.matrix_size - 1, self.matrix_size - 1], [self.matrix_size - 1, 0]]
        # matrix will be filled with 1's , wherever words are fitted
        matrix = []
        for i2 in range(self.matrix_size):
            matrix.append(self.matrix_size * [0])
        # for First longest word, different processing
        r1_quad = random.randrange(0, 4)
        r1_dir = random.randrange(0, 2)
        self.words = []
        self.length = []
        self.position.append(quad_start[r1_quad])
        self.direction.append(first_word_dir[r1_quad][r1_dir])
        self.words.append(temp_list[0][0])
        self.length.append(temp_list[0][1])
        matrix = matrix_superimpose(
            matrix, self.position[0], direction_inc[self.direction[0]], self.length[0])
        for i3 in range(1, self.count):
            current_success = 0
            itera = 0
            while(current_success == 0 and itera <= 20):
                x, y = generate_start_pos(self.matrix_size)
                current_quad = find_quadrant(x, y, self.matrix_size)
                r2_dir = random.randrange(0, 3)
                current_dir = second_word_dir[current_quad][r2_dir]
                current_success = word_hit_or_miss(
                    x, y, temp_list[i3][1], direction_inc[current_dir], matrix)
                itera += 1

            # if all 20 start positions fail, then words list can't be fit into
            # this matrix
            if current_success == 0:
                break
            self.position.append([x, y])
            self.direction.append(current_dir)
            self.words.append(temp_list[i3][0])
            self.length.append(temp_list[i3][1])
            matrix = matrix_superimpose(
                matrix, self.position[i3], direction_inc[self.direction[i3]], self.length[i3])
        if len(self.words) == self.count:
            self.success = True
        return matrix
        # it will stay false, if 20 itearaions had failed for a word

    def set_position1(self):
        '''generates the postions for the words with overlap
        '''
        temp_list = []  # stores [word, word_len] eg. [cat,3]
        i1 = 0
        for i in self.words:
            temp_list.append([])
            temp_list[i1] = [i, len(i)]
            i1 += 1
        # sort the words in decreasing order of length
        temp_list.sort(key=itemgetter(1), reverse=True)
        direction_inc = [
            [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        # possible directions for the respective quadrant
        first_word_dir = [[2, 4], [4, 6], [6, 0], [0, 2]]
        # Ignoring diagnol directions
        # possible directions for all words except the first one for the
        # respective quadrant
        second_word_dir = [[2, 3, 4], [4, 5, 6], [6, 7, 0], [0, 1, 2]]
        quad_start = [[0, 0], [0, self.matrix_size - 1],
                      [self.matrix_size - 1, self.matrix_size - 1], [self.matrix_size - 1, 0]]
        # matrix will be filled with 1's , wherever words are fitted
        matrix = []
        for i2 in range(self.matrix_size):
            matrix.append(self.matrix_size * [0])
        # for First longest word, different processing
        r1_quad = random.randrange(0, 4)
        r1_dir = random.randrange(0, 2)
        self.words = []
        self.length = []
        self.position.append(quad_start[r1_quad])
        self.direction.append(first_word_dir[r1_quad][r1_dir])
        self.words.append(temp_list[0][0])
        self.length.append(temp_list[0][1])
        matrix = matrix_superimpose(
            matrix, self.position[0], direction_inc[self.direction[0]], self.length[0])
        # from second word onwards
        i3 = 1
        while i3 < self.count:
            current_success = 0
            itera = 0
            if i3 + 1 < self.count:
                word1 = temp_list[i3][0]
                word2 = temp_list[i3 + 1][0]
                common_letters = list(set(word1) & set(word2))
                if len(common_letters) > 0:
                    char = common_letters[0]
                    offset1 = word1.index(char)
                    offset2 = word2.index(char)
                    while(current_success == 0 and itera <= 40):
                        x, y = generate_start_pos(self.matrix_size)
                        current_quad = find_quadrant(x, y, self.matrix_size)
                        r2_dir = random.randrange(0, 3)
                        current_dir = second_word_dir[current_quad][r2_dir]
                        current_success1 = word_hit_or_miss(
                            x, y, temp_list[i3][1], direction_inc[current_dir], matrix)
                        if current_success1 != True:
                            itera += 1
                            continue
                        # go to the overlap position in word1 by offset qty
                        x_off, y_off = convert_pos_inc(
                            x, y, offset1, current_dir, self.matrix_size)
                        if x_off == -1:  # here it wont happen
                            itera += 1
                            continue

                        temp = range(3)
                        # just creating a temp list with 0,1,2,3 and removing
                        # the already chosen direction for first word
                        temp.remove(r2_dir)
                        # bcos of continue , inside loop, it may not even be
                        # intialized
                        current_success2 = False
                        for r2_dir2 in temp:
                            current_dir2 = second_word_dir[
                                current_quad][r2_dir2]
                            # revert back to the position, where word2 would
                            # begin, in the guven direction
                            x2, y2 = convert_pos_dec(
                                x_off, y_off, offset2, current_dir2, self.matrix_size)
                            if x2 == -1:
                                # this direction wont work. goes ot of bound
                                continue
                            current_success2 = word_hit_or_miss(
                                x2, y2, len(word2), direction_inc[current_dir2], matrix)
                            # this word_hitor misss may make the indices out of
                            # bound
                            if current_success2 == True:
                                break
                        if current_success2 == True:
                            current_success = True
                        else:
                            itera += 1
                            continue
                    # if all 20 start positions fail, then words list can't be
                    # fit into this matrix
                    if current_success == 0:
                        print "Not  possible"
                        break
                    self.position.append([x, y])
                    self.direction.append(current_dir)
                    self.words.append(temp_list[i3][0])
                    self.length.append(temp_list[i3][1])
                    matrix = matrix_superimpose(
                        matrix, self.position[i3], direction_inc[self.direction[i3]], self.length[i3])
                    self.position.append([x2, y2])
                    self.direction.append(current_dir2)
                    self.words.append(temp_list[i3 + 1][0])
                    self.length.append(temp_list[i3 + 1][1])
                    matrix = matrix_superimpose(matrix, self.position[
                                                i3 + 1], direction_inc[self.direction[i3 + 1]], self.length[i3 + 1])
                    i3 += 2

            if current_success == 0:
                while(current_success == 0 and itera <= 20):
                    x, y = generate_start_pos(self.matrix_size)
                    current_quad = find_quadrant(x, y, self.matrix_size)
                    r2_dir = random.randrange(0, 3)
                    current_dir = second_word_dir[current_quad][r2_dir]
                    current_success = word_hit_or_miss(
                        x, y, temp_list[i3][1], direction_inc[current_dir], matrix)
                    itera += 1
                # if all 20 start positions fail, then words list can't be fit
                # into this matrix
                if current_success == 0:
                    break
                self.position.append([x, y])
                self.direction.append(current_dir)
                self.words.append(temp_list[i3][0])
                self.length.append(temp_list[i3][1])
                matrix = matrix_superimpose(
                    matrix, self.position[i3], direction_inc[self.direction[i3]], self.length[i3])
                i3 += 1
        if len(self.words) == self.count:
            self.success = True
        return matrix

    def get_start_end_xy(self, i):
        """returns start and end coordinates of i_th word in words(list)"""
        direction_inc = [
            [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        x_start = self.position[i][1]
        y_start = self.position[i][0]
        x_end = x_start + \
            (len(self.words[i]) - 1) * direction_inc[self.direction[i]][1]
        y_end = y_start + \
            (len(self.words[i]) - 1) * direction_inc[self.direction[i]][0]
        return (x_start, y_start), (x_end, y_end)


def find_quadrant(x, y, n):
    '''Finds the quadrant , in which the given point x,y lies
    returns: 0,1,2,3 (quadrant no.)'''
    if x < n / 2:
        if y < n / 2:
            return 0
        else:
            return 1
    else:
        if y < n / 2:
            return 3
        else:
            return 2


def convert_pos_dec(x, y, offset, curr_dir, size):
    direction_inc = [
        [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    for i in range(offset):
        x = x - direction_inc[curr_dir][0]
        y = y - direction_inc[curr_dir][1]
    if (x < 0 or x >= size) or (y < 0 or y >= size):
        x, y = -1, -1
    return x, y


def convert_pos_inc(x, y, offset, curr_dir, size):
    direction_inc = [
        [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    for i in range(offset):
        x = x + direction_inc[curr_dir][0]
        y = y + direction_inc[curr_dir][1]
    if (x < 0 or x >= size) or (y < 0 or y >= size):
        x, y = -1, -1
    return x, y


def word_hit_or_miss(x, y, l, inc, matrix):
    '''Checks whether a word of length l can be fitted in the given direction inc.
    Input: start position, length, direction_increment
    Returns: 1, if we can fit'''
    i, j = x, y
    flag = 0
    n = len(matrix)
    for i1 in xrange(l):
        # this worked eralier , without issue of going out bound in <0. Bcos
        # dircetions, acc to quad, are such a way that, it wont go below bound
        if i >= n or j >= n or i < 0 or j < 0 or matrix[i][j] == 1:
            flag = 1
            break
        else:
            i, j = i + inc[0], j + inc[1]
    if flag == 1:
        return 0
    else:
        return 1


def matrix_superimpose(matrix, pos, inc, l):
    '''fills 1's in the given word positions
    returns: the matrix with superimposed 1s'''
    i, j = pos[0], pos[1]
    for i1 in range(l):
        matrix[i][j] = 1
        i, j = i + inc[0], j + inc[1]
    return matrix


def generate_start_pos(n):
    '''Genertaes starting positions between [1,n]'''
    return random.randrange(n), random.randrange(n)
