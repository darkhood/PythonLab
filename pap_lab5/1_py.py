import tkinter.filedialog

if __name__=="__main__":
	file_name = "/home/student/pap_lab5/sample_etc_passwd.txt"
	## f = tkinter.filedialog.askopenfilename()
	f = open(file_name, 'r')
	count = 0
	line = ""
	while f.readline() != '':
		count += 1
		##line = f.readline()
		##print(line)
	print("Total number of entries are : ",count)
		
	print("Reached the end of the file while printing")
	f.close()
	
	## Also find out the no of users with the /bin/bash as the login shell
	
	f = open(file_name, 'r')
	count_login = 0
	line = f.readline()
	pattern = "/bin/bash"
	while line!='':
		## Perform some function
		line1 = line.split(":")[-1].strip()
		if line1 == pattern:
			count_login += 1
			print(line1)
		line = f.readline()
	print("The number of users with",pattern,"are:",count_login)
