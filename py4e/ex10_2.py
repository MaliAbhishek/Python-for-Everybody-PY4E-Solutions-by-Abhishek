#prompts for a file name
fname=input("Enter a file name:")
#safety valve 
try:
    fhand=open(fname) #opens that file and reads through the file
except:
    print("File is not readable. Please check the name and other parameters:", fname)
    quit()
counts={}
hours=[]    
for line in fhand:#read he file line by line
    if line.startswith("From") and not line.startswith("From:"):
        hour = line.rstrip().split()[len(line.split())-2][:2]#pull the hour out from the 'From ' line by finding the time and then splitting the string.
        hours.append(hour)
for i in hours:
    counts[i]=counts.get(i,0)+1
[print(k, v) for k, v in sorted(counts.items(), key=lambda item: item[0], reverse=False)]#print out the counts, sorted by hour