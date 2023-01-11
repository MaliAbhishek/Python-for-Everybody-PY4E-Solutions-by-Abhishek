# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
xc=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #counting nuber of lines
    count=count+1
    #adding confidence level
    Xconf=float(line[20:])
    xc=xc+Xconf
xav=xc/count
print("Average spam confidence:", xav)
