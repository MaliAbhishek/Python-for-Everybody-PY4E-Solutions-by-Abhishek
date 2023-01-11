def computepay(h, r):
    if h<=40:
         p=h*r
    elif h>40:
        p=(h-40)*1.5*r+40*r
    return p
hrs = input("Enter Hours:")
rate=input("Enter Rate: ")
xh=float(hrs)
xr=float(rate)
p = computepay(xh, xr)
print("Pay", p)
