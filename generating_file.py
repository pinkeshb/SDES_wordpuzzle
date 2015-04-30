def generating_file(rfile, wfile):
    '''Generates a file with words in increasing order of length
    their count's w.r.t  length are printed in 1st line'''
    fout = open(wfile, "w+")
    count = 15 * [0]
    buckets = []
    for i1 in range(15):
        buckets.append([])
    for i in open(rfile):
        i = i.rstrip('\n')
        t = len(i)
        buckets[t - 1].append(i)
        count[len(i) - 1] = count[len(i) - 1] + 1
    fout.write(' '.join(map(str, count)) + '\n')
    for j in range(15):
        for k in range(0, len(buckets[j])):
            fout.write(buckets[j][k] + '\n')
    fout.close()

if __name__ == '__main__':
    generating_file("words_inp.txt", "words_out.txt")
