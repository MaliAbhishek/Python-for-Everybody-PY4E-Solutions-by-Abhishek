#prompts for a file name
fname=input("Enter a file name:")
#safety valve 
try:
    fhand=open(fname) #opens that file and reads through the file
except:
    print("File is not readable. Please check the name and other parameters:", fname)
    quit()
counts={}
emails=[]    
for line in fhand:#read he file line by line
    if line.startswith("From") and not line.startswith("From:"):
        line=line.rstrip()
        L_words=line.split() #split the line into a list of words using the split() method.
        emails.append(L_words[1])#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
for i in emails:
    counts[i]=counts.get(i,0)+1#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.   
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
bigmail=None
bigcount=None
for email,count in counts.items():
    if bigcount is None or count>bigcount:
        bigmail=email
        bigcount=count
print(bigmail,bigcount) 