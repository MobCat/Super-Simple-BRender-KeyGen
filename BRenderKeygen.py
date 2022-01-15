#!/env/Python3.8.10
# Headder
print("Simple BRender SDK Keygen\nBy MobCat and Foon.\n")
# Take Input key
X = input("Your Identification code is: ")

# Check input key.. is a key.
if len(X) < 8:
	print("ERROR: Identification code must be longer then 8 digits")
	input("Press enter to exit...")
	exit()
try:	
	X = int(X)
except ValueError:
	print("ERROR: Identification code can only be numbers.")
	input("Press enter to exit...")
	exit()

# Do foon math with key.
Y = (((~X)>>4)&0xfffffff)^0x11f37a7
# Gib key to user.
print(f"Your Validation code is:     {Y}")

# Quit when done.
input("Press enter to exit...")
exit()