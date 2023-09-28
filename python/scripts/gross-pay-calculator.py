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

gross = float(hours) * float(rate)

print("Your pay is $", gross, "!")