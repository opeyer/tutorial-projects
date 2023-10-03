# Talking Clock
# Pre-alpha version
# by Otto William Peyer IV

# Header
print('========================')
print('     TALKING  CLOCK     ')
print('by   opeyer @ opeyer.com')
print('========================')

# Function (Get input from user)
inputTime = input('What time?')

# Set AM or PM
inputTimeInteger = int(inputTime)
if inputTimeInteger >= 12:
    meridiemStatus = "PM"
else:
    meridiemStatus = "AM"

# Print result
print('It is ', meridiemStatus, '!')
