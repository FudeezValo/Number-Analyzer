#Lets Play with Numbers!!
#So Numbers gives: character (odd, even)

def check_odd_even(number):
    if number%2 == 0:
      print(f'{number} is an even number')
    else:
      print(f'{number} is an odd number')


#To get the factors of a number, we'll iterate through all the numbers from 1 till the number itself. We'll then try to divide the numbers by the iteration index.
# If the division has no remainder, the iteration index is a factor of the number.
def get_factors(number):
	factors = []
	iteration_index = 1
	while iteration_index <= number:
		if number%iteration_index == 0:
			factors.append(iteration_index)
		iteration_index += 1
	print(f'The factors of {number} are: {factors}')
	return factors

def check_prime(number,factors):
	if len(factors) == 2:
		print(f'{number} is a prime number')
	else:
		print(f'{number} is not a prime number')

def analyze_number(number):
	check_odd_even(number)
	factors = get_factors(number)
	check_prime(number,factors)

analyze_number(888)



















