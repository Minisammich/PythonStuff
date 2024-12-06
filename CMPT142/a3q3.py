#  CMPT-142 - A3Q3 - Pokedex.
#  Function: Create a record of pokemon and their attributes.
#  ---------------------------------------------
#  Created by: Jeffrey Hamilton, nfj513, 11393559.
#  Created on: November 25th, 2024, 2:30pm.
#  Last modified: November 25th, 2024, 3:15pm.
#  ---------------------------------------------

def add_to_pokedex(species: str,type: str,level: int):
    """
    :params: species: Name of newly caught Pokemon \n
        type: Type of the newly caught Pokemon \n
        level: Level of the newly caught pokemon \n
    Function: Adds Name and Attributes of the newly caught Pokemon to your PokeDex.
    """
    pokedex.append({"Species":species,"Type":type,"Level":level})


pokedex = []
do_loop = True


print("Welcome to PokeDex Logger!")
while do_loop:
    print("Enter info for a newly caught Pokemon")
    poke_species = input("Pokemon's Species?: ").capitalize()
    poke_type = input("Pokemon's Type?: ").capitalize()
    poke_level = int(input("Pokemon's Level?: "))
    add_to_pokedex(poke_species,poke_type,poke_level)
    print("----------")
    continue_loop = input("Are there more Pokemon to add? (Y/n):").lower()
    if continue_loop == "n":
        do_loop = False
        print("Logging complete. Printing final PokeDex:")
        print(pokedex)