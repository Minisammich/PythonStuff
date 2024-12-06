#  CMPT-142 - A3Q2 - Whitebox testing.
#  Function: Making a function, then writing
#  test cases to find errors.
#  ---------------------------------------------
#  Created by: Jeffrey Hamilton, nfj513, 11393559.
#  ---------------------------------------------

from a3q2 import closest_to_zero

def print_test_result(test: tuple,expected: int):
    """
    :params: test: Numbers to test in the closest_to_zero function. A tuple containing three integers. \n
        expected: Integer containing the value that is the closest of the three test numbers to zero. \n
    Function: Prints out the test case, expected result, and actual result in the event of a disagreement.
    """
    result = closest_to_zero(*test)
    if result != expected:
        print("Testing closest_to_zero() with", test, "   Expected:", expected, " Got: ", result)

###### Base Functionality #######
# Testing lowest being num1.
test = (1,2,3)
expected = 1
print_test_result(test,expected)

# Testing lowest being num2.
test = (2,1,3)
expected = 1
print_test_result(test,expected)

# Testing lowest being num3.
test = (3,2,1)
expected = 1
print_test_result(test,expected)
################################

## Base Functionality (Negative) ##
test = (-1,-2,-3)
expected = -1
print_test_result(test,expected)

# Testing lowest being num2.
test = (-2,-1,-3)
expected = -1
print_test_result(test,expected)

# Testing lowest being num3.
test = (-3,-2,-1)
expected = -1
print_test_result(test,expected)
################################


######## Three-way ties ########
# Testing a three-way positive tie.
test = (2,2,2)
expected = 2
print_test_result(test,expected)

# Testing a three-way Negative tie.
test = (-2,-2,-2)
expected = -2
print_test_result(test,expected)
################################


### Rolling single negative ###
# Testing num1 negative.
test = (-2,2,2)
expected = 2
print_test_result(test,expected)

# Testing num2 negative.
test = (2,-2,2)
expected = 2
print_test_result(test,expected)

# Testing num3 negative.
test = (2,2,-2)
expected = 2
print_test_result(test,expected)
################################


### Rolling double negatives ###
# Testing nums 1 and 2 negative.
test = (-2,-2,2)
expected = 2
print_test_result(test,expected)

# Testing nums 1 and 3 negative.
test = (-2,2,-2)
expected = 2
print_test_result(test,expected)

# Testing nums 2 and 3 negative.
test = (2,-2,-2)
expected = 2
print_test_result(test,expected)
################################