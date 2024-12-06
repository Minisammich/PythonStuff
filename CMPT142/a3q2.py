# This is the function that I am whitebox testing in a3q2_testdriver.py

def closest_to_zero(num1: int, num2: int, num3: int) -> int:
    """
    :params: num1, num2, num3 -> Each integer values.\n
    Function: Outputs whichever value is closest to zero. In the result of a tie between positive and negative values, outputs the positive value.
    """
    # We get the absolute values of the three inputs
    a1, a2, a3 = abs(num1),abs(num2),abs(num3)
    if (a1 < a2 and a1 < a3): # If a1 is the lowest
        return(num1)
    elif a2 < a1 and a2 < a3: # If a2 is the lowest
        return(num2)
    elif a3 < a1 and a3 < a2: # If a3 is the lowest
        return(num3)
    elif a1 == a2 and a1 == a3: # If all absolute values are equal:
        if(num1 < 0 and num2 < 0 and num3 < 0): # Check if all are negative:
            return(num1) # If all are negative, returns num1
        else:
            return(a1) # If one or more is positive, returns a1
    