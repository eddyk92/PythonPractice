# random number game

import random
def ask_user_and_check_number():
	user_number = int(input("Enter a number between 0 and 9: "))
	if user_number in magic_numbers:
		return("You got it right")
	if user_number not in magic_numbers:
		return("You didn't get it, you f*kin' loser! ")
		
magic_numbers = [random.randint(0,9), random.randint(0, 9)]

def run_program_x_times(chances):
	for attempt in range(chances): 
		print('this is attempt {}'.format(attempt))
		messsage = ask_user_and_check_number()
		print(messsage)
		
run_program_x_times(int(input("How many chances do you want? Insert a number: ")))