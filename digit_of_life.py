date = input("Enter date in the format YYYMMDD: ")

def bd_digit(string):
    total = 0
    for digit in string:
        total+=int(digit)
    
    if total >=10:
        return bd_digit(str(total))
    else:
        return total   
print(bd_digit(date))