import random
def fib(a):
    i=0
    x=[]
    for i in range(a):
        if i<=1:
            x.append(1)
        else:
          x.append(x[i-1]+x[i-2])
        i+=1
    return(x)
a=input("Enter number of elemnts required in a Fibonacci series: ")
a=int(a)
y=fib(a)   
random.shuffle(y)
print(y)
j=0
for i in range(len(y)):
    for j in range(i+1, len(y)):    
        if(y[i] < y[j]):    
            temp = y[i]    
            y[i] = y[j]    
            y[j] = temp
print(y)


