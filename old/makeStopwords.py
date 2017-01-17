def read(file):
	setString = "{"
	for aline in file:
		setString+="'"
		setString+= aline.strip()
		setString+="'"
		setString+=",  "
	return setString

file=open ("stopwords.txt", 'r')
stopword_list=read(file)
file.close()

newfile = open("stopwords.py", 'w')
newfile.write(stopword_list)
newfile.close()
