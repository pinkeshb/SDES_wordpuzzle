def generating_file(rfile,wfile):
	fout=open(wfile,"w+")
	count=15*[0]
	buckets=[]
	for i1 in range(15):
		buckets.append([])

	for i in open(rfile):
		
		i=i.rstrip('\n')
		t=len(i)
		buckets[t-1].append(i)
		# fout.write(i+' '+str(len(i)-1)+'\n')
		count[len(i)-1]=count[len(i)-1]+1
	#fout.seek(0,0)

	#i'm appending at the end of file.
	fout.write(' '.join(map(str,count))+'\n')
	for j in range(15):
		for k in range(0,len(buckets[j])):
			# fout.write(buckets[j][k]+' '+str(j+1)+'\n')#storre sthe length of word at the end of the line
			fout.write(buckets[j][k]+'\n')
	fout.close()

if __name__=='__main__':
	generating_file("words_inp.txt","words_out.txt")
