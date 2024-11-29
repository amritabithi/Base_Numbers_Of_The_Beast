# Summations of the Number of the Beast
# by Amrita Bithi 2023 www.amritabithi.com 
# https://github.com/amritabithi/Base_Numbers_Of_The_Beast/

from colorama import Fore
# Summation of the series of natural numbers 1 to 36
# ie. 1 + 2 + 3 + 4 + 5 ... + 32 + 33 + 34 + 35 + 36
def hr(): print("\n\n	--------------------------------------------------------");

def summationIntegersTo36(printVerbose = False):
	if printVerbose == True:
		hr();
		print(Fore.LIGHTYELLOW_EX,"\n	Summation of the series of natural numbers 1 to 36");
		print(Fore.LIGHTYELLOW_EX,"	ie. 1 + 2 + 3 + 4 + 5 ... + 32 + 33 + 34 + 35 + 36\n",Fore.RESET);
	csum = 0;
	for i in range(1,37):
		csum += i;
		if printVerbose == True:
			print("	",str(csum-i).rjust(3,' ')+" + "+str(i).rjust(2,' ')+" = ",Fore.LIGHTYELLOW_EX,str(csum).rjust(3,' '),Fore.RESET);
	if printVerbose == True:
		print(Fore.LIGHTYELLOW_EX,"\n	Sum of integers from 1 to 36 is: ",Fore.LIGHTRED_EX,str(csum),Fore.RESET);
		hr();
	return csum;


# Summation of the notational value of "10" which is
# the simplest value that will generate a non-repeating
# sequence for the function, in all number systems from
# base 1 to base 36.  The number system of base 1 here 
# is defined as only the number one.
def summationBasesTo36(printVerbose = False):
	csum = 1; # Begin with base 1, which is always 1
	numberString = "10";
	if printVerbose == True:
		hr();
		print(Fore.LIGHTYELLOW_EX,"\n\n	Summation of values for the numerals \"10\" in number systems 1 to 36.\n	Sums are shown in decimal.\n",Fore.RESET);
		print("	'10' in base ",str(1).ljust(2,' ')," =  1",Fore.LIGHTYELLOW_EX,"   sum: ",str(csum).rjust(3,' '),Fore.RESET);
	for i in range(2,37):
		csum += int(numberString,i);
		if printVerbose == True:
			print("	'10' in base ",str(i).ljust(2,' ')," = ",str(int(numberString,i)).ljust(2,' '),Fore.LIGHTYELLOW_EX,"  sum: ",str(csum).rjust(3,' '),Fore.RESET);
	if printVerbose == True:
		print(Fore.LIGHTYELLOW_EX,"\n	The sum of notational '10' for number systems with bases 1-36 is: ",Fore.LIGHTRED_EX,str(csum),Fore.RESET);
		hr();
	return csum;

# Summation of the decimal values of each distinct
# Roman numeral which cannot be represented in
# bar notation.
def summationRomanNumerals(printVerbose = False):
	csum = 0;
	I = 1;
	V = 5;
	X = 10;
	L = 50;
	C = 100;
	D = 500;
	csum = I + V + X + L + C + D;
	if printVerbose == True:
		hr();
		print(Fore.LIGHTYELLOW_EX,"\n\n	Summation of the first 6 Roman numerals, which are the numerals");
		print("  	which cannot be substituted with thousands bar notation.",Fore.RESET);
		print("\n\n	I = ",Fore.LIGHTYELLOW_EX,"1",Fore.RESET);
		print("	V = ",Fore.LIGHTYELLOW_EX,"5",Fore.RESET);
		print("	X = ",Fore.LIGHTYELLOW_EX,"10",Fore.RESET);
		print("	L = ",Fore.LIGHTYELLOW_EX,"50",Fore.RESET);
		print("	C = ",Fore.LIGHTYELLOW_EX,"100",Fore.RESET);
		print("	D = ",Fore.LIGHTYELLOW_EX,"500",Fore.RESET);
		print("\n");
		print("	I + V + X + L + C + D = ",Fore.LIGHTRED_EX,"666",Fore.RESET);
		hr();
	return csum;

while(True):
	print("\n\n		",Fore.LIGHTRED_EX,"⛧⛧⛧",Fore.LIGHTYELLOW_EX," Base Numbers of the Beast ",Fore.LIGHTRED_EX,"⛧⛧⛧",Fore.RESET)
	print("\n	Select an option to view summation:\n")
	print(Fore.LIGHTCYAN_EX,"		(1) Summation of the series of natural numbers 1 to 36.");
	print("		(2) Summation of notational value \"10\" in number systems 1 to 36.");
	print("		(3) Summation of the first 6 Roman numerals, which are the Roman numerals");
	print("			which cannot be substituted for thousands bar notation.");
	print("		(4) Exit",Fore.RESET);
	choice = input("\n	Enter a menu option: \n	");
	if choice == "1":
		summationIntegersTo36(True);
	elif choice == "2":
		summationBasesTo36(True);
	elif choice == "3":
		summationRomanNumerals(True);
	elif choice == "4":
		break;
	else:
		print("Invalid option selected, exiting...");
		break;

