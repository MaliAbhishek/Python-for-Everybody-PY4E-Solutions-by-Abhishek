#prompts for a file name
fname=input("Enter a file name:")
#safety valve 
try:
    fhand=open(fname) #opens that file and reads through the file
except:
    print("File is not readable. Please check the name and other parameters:", fname)
    quit()
count=0    
for line in fhand:#read he file line by line
    if line.startswith("From") and not line.startswith("From:"):
        line=line.rstrip()
        L_words=line.split() #split the line into a list of words using the split() method.
        print(L_words[1])
        count+=1        
print("There were", count, "lines in the file with From as the first word")
