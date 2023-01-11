largest = None
smallest = None

while True:
    inp = input("Enter a number: ")
    if inp == "done" :
         break
    try:
        num = float(inp)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = num
    elif num < smallest :
        smallest = num
    if largest is None:
        largest = num
    elif num > largest :
        largest = num

def done(largest,smallest):
    print("Maximum is", int(largest))
    print("Minimum is", int(smallest))

done(largest,smallest)
