hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter Rate: ")
xr=float(rate)
if h<=40 :
    xp=h*xr
else:
    xp=((h-40)*1.5+40)*xr
print(xp)
