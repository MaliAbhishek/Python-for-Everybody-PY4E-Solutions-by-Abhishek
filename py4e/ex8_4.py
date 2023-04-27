#prompts for a file name
fname=input("Enter a file name:")
#safety valve 
try:
    fhand=open(fname) #opens that file and reads through the file
except:
    print("File is not readable. Please check the name and other parameters:", fname)
    quit()
#build a list of words
words=list()    
for line in fhand:#read he file line by line
    line=line.rstrip()
    L_words=line.split() #split the line into a list of words using the split() method.
    for i in L_words:
        if i not in words:
            words.append(i)#For each word on each line check to see if the word is already in the list and if not append it to the list.
fhand.close()
words.sort()
print(words)
