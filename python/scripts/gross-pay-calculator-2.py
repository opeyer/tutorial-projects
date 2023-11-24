# Take input from user
# def takeInput():
hours = input("Enter hours: ")
rate = input("Enter rate (in $USD per hour): ")
# return "hours", "rate"

def computepay(hours, rate):
	hoursInt = int(hours)
	if hoursInt <= 40:
		gross = float(hours) * float(rate)
	elif hoursInt > 40:
		grossPreOvertime = 40 * float(rate)
		overtime = (float(hours) - 40)
		overtimePay = (float(overtime) * (float(rate) * 1.5))    
		gross = grossPreOvertime + overtimePay
	return gross

#takeInput()
pay = computepay(hours, rate)

print("Pay", pay)              