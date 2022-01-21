# Nourish Virginia
# by Gwen Virtue
#
# This simple python script helps determine which of the 
# food banks in Virginia to support this month.


import random as rand

listBanks = {1: "Feedmore Richmond", 2: "Chesterfield Foodbank", 3: "Feeding Southwest Virginia"}
bank = []


def whichBank():

	print("Current banks in network:")

	for key, value in listBanks.items():
		print("{}: {}".format(key, value))

	is_int = False

	while is_int == False:  # These two while loops help weight the ranking based on recent donations.

		print("\nEnter the number for the bank that received the most recent donation. 0 for none.")

		lastDonation = input()

		try:
			int(lastDonation)
			is_int = True
		except ValueError:
			is_int = False
			print("Please enter a number (1-10) corresponding with the bank. 0 for none.")

	is_int = False

	while is_int == False:
		print("\nEnter the number for the bank that received the second most recent donation. 0 for none.")

		secondDonation = input()

		try:
			int(secondDonation)
			is_int = True
		except ValueError:
			is_int = False
			print("Please enter a number (1-10) corresponding with the bank, or 0 for none.")

		for i in range(len(listBanks)):  # Create a random number between 1 and 10 and assign it to a list
			bank.append(rand.randrange(1, 10))

		rankedList = {}

		for i in range(len(bank)):
			rankedList[bank[i]] = listBanks[i + 1]

		for key in rankedList:  # This loop lowers the random rank of banks that have been more recently donated to.
			tempKey = int(key)  # My hope is that this will ensure that the donations are more equitably distributed.
			if tempKey == lastDonation:
				print(key)
				rankedList[key] = tempKey - 2
			elif tempKey == secondDonation:
				rankedList[key] = tempKey - 1

		# print(rankedList)

		tempTop = 0  # Temporary holding number to find high number
		for key in rankedList:
			if key > tempTop:
				tempTop = key  # Assign current highest number to tempTop.

		print(" Next bank for donation is: {} ".format(rankedList[tempTop]))
		print("Press ENTER to return to main menu.")

		enterToContinue = input()
		bank.clear()

		welcome()


def welcome():
	print("\n\n\nWelcome to Nourish Virginia")
	print("This program will help you determine which area foodbank to support next.")
	print("------------------------------------------------------------------------")
	print("1: Display food banks")
	print("2: Determine donation")
	print("3: Quit")

	menu = input()

	if (menu == '1'):
		for key, value in listBanks.items():
			print("{}: {}".format(key, value))  # Display list of banks contained in listBanks dictionary. TODO: load listBanks from textfile.
		welcome()
	elif (menu == '2'):
		whichBank()  # Main program loop
	elif (menu == '3'):
		exit()
	else:
		print("Please try again.")
		welcome()


def main():
	rand.seed()  # Initialize the random number generator
	welcome()  # Main program menu


if __name__ == "__main__":
	main()
