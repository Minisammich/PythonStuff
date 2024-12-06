#  CMPT-142 - A4Q2_pt2 - System of Linear Equations solver.
#  Function: Solves for variables in a system of linear 
#  equations based on coefficients and constants.
#  ---------------------------------------------
#  Created by: Jeffrey Hamilton, nfj513, 11393559.
#  Created on: December 3rd, 2024, 12:00pm.
#  Last modified: December 3rd, 2024, 5:00pm.
#  ---------------------------------------------

import numpy as np

def solve_system(coefficients: list, variables: list, constants: list) -> dict:
    """
    Parameters: coefficients: List of all coefficients from system of linear equations.
                variables: List of all variables names from system of linear equations.
                constants: List of all constants from the system of linear equations.
    Output: Dictionary containing all variables of the system of linear equations and their respective value.
    Function: Solves for variables in a system of linear equations based on coefficients and constants.
    """

    # Dictionary that will later be filled with variable names and their respective value.
    solution_dict = {}    

    # Assigns coefficients and constants to Left-hand-side and Right-hand-side of the system of linear equations.
    # Converts them into numpy arrays so that we can use the numpy linalg solver.
    LHS = np.array(coefficients)
    RHS = np.array(constants)

    # Solves system of linear equations based on the LHS and RHS previously assigned
    solution = np.linalg.solve(LHS,RHS)

    # Assigns the variable as key and solution as value to the solution dictionary.
    for i,var in enumerate(variables):
        solution_dict[var] = solution[i]

    return(solution_dict)