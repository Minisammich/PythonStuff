#  CMPT-142 - A1Q4 - Online Account
#  ---------------------------------------------
#  Created by: Jeffrey Hamilton, nfj513, 11393559.
#  Created on: November 5th, 2024, 1:00pm
#  Last modified: November 5th, 2024, 2:10pm.
#  ---------------------------------------------

# Gets users birthdate and desired name, passes them into a tuple.
# Warns user that name will be truncated to 10 characters if the name given is greater than 10 characters.
def Get_Name_and_Birthdate():
    '''
    :param(s): none
    :output: tuple containing user inputs for name and birthdate
    '''
    good_input = False
    while not good_input:
        name = input("Enter a name for your account: ")
        if len(name) > 10:
            if input("This username will be truncated to 10 characters. Continue? (Y/n): ").lower() != "n":
                good_input = True
            
    date_of_birth = input("Enter your date of birth (MM/DD/YYYY): ")
    return name, date_of_birth

# Receives a tuple with both account name and birthdate from the get name and birthdate function,
# Passes birthdate directly, but cuts name to 10 characters and replaces spaces with underscores before passing it on.
def Format_Name(name_and_birthdate):
    '''
    :param(s): (tuple) => (string, string) => (name, birthdate)
    :output: tuple containing modified name string and original birthdate string.
    '''
    name, birthdate = name_and_birthdate
    formatted_name = name[0:10].lower().replace(" ","_")
    return formatted_name, birthdate

# Receives a tuple with the formatted account name along with the birthdate, adds the last two digits of the
# birth year to the end of the name to finalize the username. Passes only one string.
def Finalize_Name(name_and_birthdate):
    '''
    :param(s): (tuple) => (string, string) => (name, birthdate)
    :output: string containing final user handle
    '''
    name, birthdate = name_and_birthdate
    finalized_name = name + str(birthdate[8:10])
    return finalized_name

# Prints the output of the function sequence for receiving and modifying a user handle for the user.
print(Finalize_Name(Format_Name(Get_Name_and_Birthdate())))