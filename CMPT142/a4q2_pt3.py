#  CMPT-142 - A4Q2 - System of Linear Equations parser.
#  Function: Parses systems of linear equations from a text file
#  inputs the correct parameters into my previously created System of
#  Linear Equations solver, and prints results in a neat fashion.
#  ---------------------------------------------
#  Created by: Jeffrey Hamilton, nfj513, 11393559.
#  Created on: December 3rd, 2024, 12:00pm.
#  Last modified: December 3rd, 2024, 8:45pm.
#  ---------------------------------------------

from a4q2_pt2 import solve_system
import math

def isolate_constants(path: str) -> tuple[list,list]:
    """
    Parameter: path: path to system of linear equations text file
    Output: tuple[list,list] -> Tuple containing List of equations and List of constants.
    Function: Takes in a path to text file containing a system of linear equations, seperates constants from equations.
    """

    # Opens text file containing the system of linear equations as "system"
    system = open(path, "r")

    # Empty lists to be populated later.
    equations = []
    constants = []

    # Strips line of any line delimiters or whitespace, splits it at the equals sign.
    # Left of the equals sign is the equation, Right is the constant.
    for line in system:
        line_split = line.strip().split(" = ")
        equations.append(line_split[0]) 
        constants.append(int(line_split[1]))

    return(equations,constants)

def isolate_variables(equations: list) -> list:
    """
    Parameter: equations: List of equations from system.
    Output: List containing variable names.
    Function: Extracts all variable names from equations without repeats.
    """

    var_list = []

    # Runs through each equation
    for eqn in equations:

        # Within equation, iterates through each character with "i" being the current index.
        for i,x in enumerate(eqn):

            # If "x" is not a digit, plus sign, space, or minus sign, set var = x.
            if not x.isdigit() and (x != "+" and x != " " and x != "-"):
                var = x
                # If two indexes to the right of the text character is a number (i.e. x10 - x99) set var to be "x" plus the two digits following.
                if i+2 < len(eqn) and eqn[i+2].isdigit():
                    var = (x+eqn[i+1]+eqn[i+2])

                # If only one idex to the right of the text character is a number (i.e. x0 - x9) set var to be "x" plus the following digit.
                elif i+1 < len(eqn) and eqn[i+1].isdigit():
                    var = (x+eqn[i+1])

                # Add var to var_list only if it is not a duplicate.
                if var not in var_list:
                    var_list.append(var)

    return(var_list)

def isolate_coefficients(equations: list) -> list:
    """
    Parameter: equations: List of equations from the system of linear equations.
    Output: List containing coefficients in a matrix format (list of lists in nxn size)
    Function: Isolates coefficients from equations while maintaining the form of the original system of equations.
    """

    # Splits equation at "+" and "-" signs
    split_eqn = []
    for eqn in equations:
        temp_eqn = eqn.split(" + ")
        for x in temp_eqn:
            temp2eqn = x.split(" - ")
            split_eqn.append(temp2eqn)

    # Checks if each character in each split segment of the equation is the variable, takes everything prior if so and appends it to a list.
    temp_coef_list = []
    var_list = ['a','b','c','d','e','x','y','z'] # List of all variable names in provided systems.
    for element in split_eqn:
        for x in element:
            for i,char in enumerate(x): 
                # Checks if char is not a digit, space, or dash, the value at the index prior is not a dash, and the index is not 0.
                if not char.isdigit() and char != "-" and char != " " and x[i-1] != "-" and i != 0:
                    temp_coef_list.append(int(x[0:i]))
                    break
                # If only a dash comes before the variable, the coefficient is -1.
                elif x[i-1] == "-" and (x[i] in var_list) :
                    temp_coef_list.append(-1)
                    break
                # If the variable is in index 0, the coefficient must be 1.
                elif (char in var_list) and i == 0:
                    temp_coef_list.append(1)
                    break
    
    # Takes a list of all coefficients in the system of equations, compiles them into the original form of the system of equations (nxn matrix).
    coefficients_list = []
    n = int(math.sqrt(len(temp_coef_list))) # Square root of the length of the temp coefficients list is the same as the number of rows or columns in the system of equations.
    for i in range(0,len(temp_coef_list),n):
        coefficients_list.append(temp_coef_list[i:i+n])

    return(coefficients_list)

        


# Gets user to choose the file name of a system to solve. 
system_path = input("Input file name of equation system to solve: ")

# Uses path to find file, isolates equations and constants from file.
equations, constants = isolate_constants(system_path)

# From isolated equations list, isolates variables.
variables = isolate_variables(equations)

# From isolated equations, isolate coefficients.
coefficients = isolate_coefficients(equations)

# Uses my system solver to solve based on the isolated coefficients, variables, and constants.
soln = solve_system(coefficients, variables, constants)

# Prints the variable and solution pair line by line.
for key,value in soln.items():
    print(str(key) + " = " + str(value))
