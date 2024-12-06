#  CMPT-142 - A4Q1 - .
#  Function: .
#  ---------------------------------------------
#  Created by: Jeffrey Hamilton, nfj513, 11393559.
#  Created on: December 3rd, 2024, 11:30am.
#  Last modified: December 3rd, 2024, 12:00pm.
#  ---------------------------------------------

from cache_primes_starter import is_prime

def prime_results(file_name):
    """
    Parameter: file_name: The name of a file to pull numbers from.
    Output: Dictionary containing all numbers and whether they are prime (True) or not (False). 
    """

    # Opens text file and assigns it to "numbers"
    numbers = open(file_name , "r")

    # Empty dictionary to populate with results later.
    is_prime_dict = {}

    # Iterates through every line in the text file, adds to dictionary along with whether they are prime or not.
    for n in numbers:
        n = int(n)
        is_prime_dict[n] = is_prime(n)

    return(is_prime_dict)

# Prints the dictionary containing all numbers from the text file and whether they are prime.
print(prime_results("numbers.txt"))

    
    