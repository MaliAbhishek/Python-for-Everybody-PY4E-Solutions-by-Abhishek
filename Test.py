import numpy as np 
score =input("Enter a score: ")
try:
    x=float(score)
except:
    x=-1
x=x/100
y=np.around(np.arange(0.6,1.1,0.1),2)
grade=["F", "D", "C", "B", "A"]
res=dict(zip(y,grade))
if 0.0<=x<=1.0:
   for i in y:
       if x<i:
           print(res[i]) 
           break
else:
    print("out of range")