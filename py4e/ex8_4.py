#prompts for a file name
fname=input("Enter a file name:")
#safety valve 
try:
    fhand=open(fname) #opens that file and reads through the file
except:
    print("File is not readable. Please check the name and other parameteres", fname)
    quit()
#build a list of words
words=list()    
for line in fhand:#read he file line by line
    line=line.rstrip()
    L_words=line.split() #split the line into a list of words using the split() method.
    for i in words:
        for j in L_words:
            if i==j:
                L_words.remove(j)
            else: continue#For each word on each line check to see if the word is already in the list and if not append it to the list.
    for i in range(len(L_words)):
        words.append(L_words[i])
words.sort()
print(words)
