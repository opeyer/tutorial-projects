# Gross Pay Calculator
# Pre-alpha version
# by Otto William Peyer IV

# Header
print('========================')
print('  GROSS PAY CALCULATOR  ')
print('by   opeyer @ opeyer.com')
print('========================')

# Function
hours = input("Enter hours: ")
rate = input("Enter rate (in $USD per hour): ")


try:
    hoursInt = int(hours)
    if hoursInt <= 40:
        gross = float(hours) * float(rate)
    elif hoursInt > 40:
        grossPreOvertime = 40 * float(rate)
        overtime = (float(hours) - 40)
        overtimePay = (float(overtime) * (float(rate) * 1.5))    
        gross = grossPreOvertime + overtimePay
    print("Your pay is $", gross, "!")
except:
    print("Error! Please enter numeric input.")