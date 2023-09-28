# Temperatures
# Pre-alpha version
# by Otto William Peyer IV

# Header
print('========================')
print('      TEMPERATURES      ')
print('by   opeyer @ opeyer.com')
print('========================')

# Function (Celsius to Fahrenheit)
print("This app will help you convert a temperature from Celsius to Fahrenheit.")
CelsiusTemp = input('What is the temperature in Celsius (°C)? ')
floatCelsiusTemp = float(CelsiusTemp)
FahrenheitTemp = (floatCelsiusTemp * (9/5)) + 32
print("Your temperature in Fahrenheit is", FahrenheitTemp, "°F!")