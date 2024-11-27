# Summations of the Number of the Beast
# by Amrita Bithi 2023 www.amritabithi.com 
# https://github.com/amritabithi/Base_Numbers_Of_The_Beast/

from colorama import Fore
# Summation of the series of natural numbers 1 to 36
# ie. 1 + 2 + 3 + 4 + 5 ... + 32 + 33 + 34 + 35 + 36
def summationIntegersTo36(printVerbose = False):
	if printVerbose == True:
		print(Fore.LIGHTYELLOW_EX,"\n	Summation of the series of natural numbers 1 to 36")
		print(Fore.LIGHTYELLOW_EX,"	ie. 1 + 2 + 3 + 4 + 5 ... + 32 + 33 + 34 + 35 + 36\n",Fore.RESET)
	csum = 0
	for i in range(1,37):
		csum += i
		if printVerbose == True:
			print("	",str(csum-i).rjust(3,' ')+" + "+str(i).rjust(2,' ')+" = ",Fore.LIGHTYELLOW_EX,str(csum).rjust(3,' '),Fore.RESET)
	if printVerbose == True:
		print(Fore.LIGHTYELLOW_EX,"\n	Sum of integers from 1 to 36 is: "+str(csum),Fore.RESET)
	return csum


# Summation of the notational value of "10" which is
# the simplest value that will generate a non-repeating
# sequence for the function, in all number systems from
# base 1 to base 36.  The number system of base 1 here 
# is defined as only the number one.
def summationBasesTo36(printVerbose = False):
	print(Fore.LIGHTYELLOW_EX,"\n	Summation of values for the numerals \"10\" in number systems 1 to 36.\n	Sums are shown in decimal.\n",Fore.RESET)
	csum = 1 # Begin with base 1, which is always 1
	numberString = "10"
	for i in range(2,37):
		csum += int(numberString,i)
		if printVerbose == True:
			print("	'10' in base ",str(i).ljust(2,' ')," = ",str(int(numberString,i)).ljust(2,' '),Fore.LIGHTYELLOW_EX,"  (sum: ",str(csum).rjust(3,' '),")",Fore.RESET)
	if printVerbose == True:
		print(Fore.LIGHTYELLOW_EX,"\n	The sum of notational '10' for number systems with bases 1-36 is: "+str(csum),Fore.RESET)
	return csum

while(True):
	print("\n\n		",Fore.LIGHTRED_EX,"⛧⛧⛧",Fore.LIGHTYELLOW_EX," Base Numbers of the Beast ",Fore.LIGHTRED_EX,"⛧⛧⛧",Fore.RESET)
	print("\n	Select an option to view summation:\n")
	print(Fore.LIGHTCYAN_EX,"		(1) Summation of the series of natural numbers 1 to 36.")
	print("		(2) Summation of notational value \"10\" in number systems 1 to 36.")
	print("		(3) Exit",Fore.RESET)
	choice = input("\n	Enter a menu option: ")
	if choice == "1":
		summationIntegersTo36(True)
	elif choice == "2":
		summationBasesTo36(True)
	elif choice == "3":
		break
	else:
		print("Invalid option selected, exiting...")
		break
