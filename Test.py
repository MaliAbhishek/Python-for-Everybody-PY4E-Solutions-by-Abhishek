data="hostel12-students mailing list hostel12-students@iitb.ac.in https://lists.iitb.ac.in/mailman/listinfo/hostel12-students"
atpos=data.find("@")
i=0
while i<atpos:
    j=data.find(' ', i, atpos)
    i=j+1
    if j==-1:
        break
    else:
        st=j 
ed=data.find(' ', atpos)
print(data[st+1:ed])