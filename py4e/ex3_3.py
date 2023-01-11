score = input("Enter Score: ")
try:
    xc=float(score)
except:
    xc=-1
if xc>=0.0 and xc<=1.0:
    if xc< 0.6:
        print('F')
    elif xc>= 0.9:
        print('A')
    elif xc>= 0.8:
        print('B')
    elif xc>= 0.7:
        print('C')
    elif xc>=0.6:
        print('D')
else:
    print('Out of Range')
