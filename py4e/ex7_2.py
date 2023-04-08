#prompts for a file name
file=input("Enter a file name:")
#safety valve 
try:
    fhand=open(file) #opens that file and reads through the file
except:
    print("File is not readable. Please check the name and other parameteres", file)
    quit()
count=0
total=0
for i in fhand:
    if i.startswith("X-DSPAM-Confidence:"): #ooking for lines of the form: X-DSPAM-Confidence:    0.8475
        count+=1 #Count these lines and 
        x=i.split(":")#extract the floating point values from each of the lines 
        x=float(x[1])
        total+=x
print("Average spam confidence:", total/count) #and compute the average of those values and produce an output
