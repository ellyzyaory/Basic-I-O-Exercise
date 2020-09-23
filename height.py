print("Enter your height.")

feet = eval(input("Feet: "))
while feet < 0:
    feet = eval(input("Feet: "))

inches = eval(input("Inches: "))
while inches < 0:
    inches = eval(input("Inches: "))



conversion = (feet * 30.48) + (inches * 2.54)
board_length = conversion * (88/100)


print("Suggested board length: ", board_length, "cm")
