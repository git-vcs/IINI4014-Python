import sys
print("Hello sir or madam, please enter your full name")
name = sys.stdin.readline()
print("Your name is:", name)
initials=''.join([firt_letter[0] for firt_letter in name.split()])
print("Dear mr or mrs",initials.upper(),"this is a simple python program")
print("You are running python version",sys.version)
print("I wish you a nice day.\nBest regards your computer.")