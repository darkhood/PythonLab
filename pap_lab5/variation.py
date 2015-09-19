if __name__=="__main__":
	file_name = "/home/student/pap_lab5/file_for_reading.txt"
	f = open(file_name, 'r')
	line = f.readline()
	while line!='':
		line1 = line.strip().split(" ")
		## print(line1) ## returns a list
		line = f.readline()
		
	f.close()
	
	dic1 = {} ## maintains a mapping of alphabet and count
	dic2 = {} ## maintains a mapping of alphabet and list of words in alphabetical order
	
	file_name1 = "/home/student/pap_lab5/file_for_writing.txt"
	f1 = open(file_name1, 'w')
	## There are two cases, we have seen the alphabet and not seen the alphabet, if the word with the alphabet is in the list, do not add it, else add the new word to the list
	'''for word in line1:
		if word[0] not in dic1:
			dic1[word[0]] = 1
			dic2[word[0]] = dic2[word[0]].append(word)
		else: 
			dic1[word[0]] = dic1[word[0]] + 1
			if word not in dic2[word[0]]:
				dic2[word[0]].append(word)
			else:
				pass
	for i in dic1:
		print(i, dic1[i])
	for j in dic2:
		print(j, dic2[j])
			
		'''
		
	dic1 = {}
	dic2 = {}
	for word in line1:
		if word[0] not in dic1:
			dic1[word[0]] = 1
			dic2[word[0]] = [word]
		else:
			dic1[word[0]] += 1
			if word not in dic2[word[0]]:
				dic2[word[0]].append(word)
			else:
				pass
		##print(word)
		'''
	for word in dic1:
		print(word, dic1[word])
	for word in dic2:
		print(word, dic2[word])
		'''
		
	
	for word in sorted(dic1.keys()):
		print(word, dic1[word], dic2[word])
		
	f1.close()
