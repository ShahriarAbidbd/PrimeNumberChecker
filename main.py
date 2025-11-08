# Coded by @ShahriarAbidbd

print(" Prime & Composite Number Checker ".center(40,"*") + " \n")

prime = "Your number is prime"
composite = "Your number is composite"
num = input("Enter your number: ")

if (num.isdigit()):
	num = int(num)
	if (num == 0):
		print("0 is neither Prime nor Composite")
	elif (num == 1):
		print("1 is neither Prime nor Composite")
	elif (num % 2 == 0 and num != 2):
		print(composite)
	elif (num % 3 == 0 and num != 3):
		print(composite)
	elif (num % 5 == 0 and num != 5):
		print(composite)
	elif (num % 7 == 0 and num != 7):
		print(composite)
	else :
		print(prime)
else :
	if (num == ""):
		print("Please provide a number")
	else :
		print(" It's not a number")

# Telegram : t.me/ShahriarAbidbd
# Youtube : t.me/@ShahriarAbidbd
