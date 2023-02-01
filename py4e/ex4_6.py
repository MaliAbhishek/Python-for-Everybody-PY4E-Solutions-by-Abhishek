def computepay(hh, rr):
    if hh<40:
        gross_pay=hh*rr
    else:
        gross_pay=(40+(hh-40)*1.5)*rr
    return gross_pay
hours=input("Enter hours of work: ")
rate=input("Enter rate: ")
xh=float(hours)
xr=float(rate)
print("Pay", computepay(xh,xr)) #invokes function computepay()
