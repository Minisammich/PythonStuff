import numpy as np

system_path = input("Input file name of equation system to solve: ")

def isolate_constants(path):
    system = open(path, "r")

    equations = []
    constants = []

    for line in system:
        line_split = line.strip().split(" = ")
        equations.append(line_split[0]) 
        constants.append(int(line_split[1]))

    return(equations,constants)

def isolate_variables(equations):
    var_list = []
    for eqn in equations:
        for i,x in enumerate(eqn):
            if not x.isdigit() and (x != "+" and x != " " and x != "-"):
                var = x
                if i+2 < len(eqn) and eqn[i+2].isdigit():
                    var = (x+eqn[i+1]+eqn[i+2])
                elif i+1 < len(eqn) and eqn[i+1].isdigit():
                    var = (x+eqn[i+1])
                if var not in var_list:
                    var_list.append(var)
    return(var_list)

def isolate_coefficients(equations: list, variables: list) -> list:
    """
    Parameters: equations: List containing equations from system.
                variables: List containing all variable names in equations.
    Output: List of coefficients.
    Function: Extracts all coefficients from all equations in the system of linear equations.
    """

    coefficient_list = []

    # Runs through each equation, prepare empty coefficient list for only coefficients within one equation.
    for eqn in equations:
        eqn_coef_list = []

        # Runs through each character in equation with "i" being the index.
        for i, val in enumerate(eqn):
            val_is_var = False # val_is_var False by default, set True later if applicable.

            # If value is a variable following the x0 - x99 format, val_is_var is set True.
            if(i+1 < len(eqn) and val == "x" and eqn[i+1].isdigit()):
                if val+eqn[i+1] in variables:
                    val_is_var = True

            # Else if value is a variable following the x, y, z, etc. format, val_is_var is set True.
            elif val in variables:
                val_is_var = True

            # If value is a variable,
            if val_is_var:
                # Checks if leading character is a space or is out of range, therefore Coefficient is 0.
                if eqn[i-1] == " " or i == 0:
                    eqn_coef_list.append(0)
                else:
                    # If the index two to the right of the variable is a negative sign (i.e. -5x) appends value with negative sign to eqn_coef_list
                    if i > 1 and (eqn[i-2] == "-"):
                        eqn_coef_list.append(int(eqn[i-2:i]))
                    # Else if the index directly to the right of the variable is a negative sign (i.e. -x) appends -1 to the eqn_coef_list
                    elif i > 0 and eqn[i-1] == "-":
                        eqn_coef_list.append(-1)
                    # Else, coefficient is positive.
                    else:
                        eqn_coef_list.append(int(eqn[i-1]))
        coefficient_list.append(eqn_coef_list)
    return(coefficient_list)

def solve_system(path):
    equations, constants = isolate_constants(path)            
    variables = isolate_variables(equations)
    coefficients = isolate_coefficients(equations,variables)

    solution_dict = {}    

    LHS = np.array(coefficients)
    RHS = np.array(constants)

    solution = np.linalg.solve(LHS,RHS)

    for i,var in enumerate(variables):
        solution_dict[var] = solution[i]

    return(solution_dict)

    

soln = solve_system(system_path)

for key,value in soln.items():
    print(str(key) + " = " + str(value))


