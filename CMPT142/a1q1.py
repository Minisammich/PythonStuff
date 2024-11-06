#  CMPT-142 - A1Q1 - Mad lib.
#  Function: Create a user generated story based
#  on a common template.
#  ---------------------------------------------
#  Created by: Jeffrey Hamilton, nfj513, 11393559.
#  Created on: November 4th, 2024, 3:00pm.
#  Last modified: November 4th, 2024, 3:20pm.
#  ---------------------------------------------

noun1 = input("Enter a noun: ") # Preferably a biotic thing such as an animal or person, but can be an inanimate object too. 
verb1 = input("Enter a verb ending in \"ing\": ") # e.g. Running, sprinting, strutting, but could by any verb ending with "ing".
adj1 = input("Enter an adjective: ") # Describes the following noun the user will be asked to enter.
noun2 = input("Enter another noun: ") # Also preferably a person or animal, but again abiotic things will work too.
noun3 = input("Enter another noun (Place): ") # Must be a place (e.g. "corner store" or "mall")
verb2 = input("Enter a verb (Simple Present Tense): ") # Simple present tense verb such as "fight", "run", or "talk"

# Sets string to "an" if following noun begins with an "a", else sets the string to "a".
adj1_formatting = "a"
if adj1[0].lower() == "a":
    adj1_formatting = "an"


# Prints all of the user input words into the template sentence.
print(f"The {noun1} was {verb1} around the town. He ran into {adj1_formatting} {adj1} {noun2} while at the {noun3}, and they began to {verb2}.")