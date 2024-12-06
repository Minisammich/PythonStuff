#  CMPT-142 - A3Q1 - Blackbox testing.
#  Function: Writing test cases to test a function
#  that I have not seen the code for.
#  ---------------------------------------------
#  Created by: Jeffrey Hamilton, nfj513, 11393559.
#  ---------------------------------------------


## PROVIDED FILE ##

from testing_blackbox_improvedAverage import improvedAverage
# i.e. the improvedAverage() function is sitting in a file called "testing_blackbox_improvedAverage.py"

# The empty list is a special case, so always test it!
test = []
expected = None
result = improvedAverage(test)
if result != expected:
    print("Testing improvedAverage() with", test, "   Expected:", expected, " Got: ", result)

## END OF PROVIDED FILE ##
    
#TODO: Expand this file with several more tests!

def test_results(expected: int, test: list):
    """
    :params: test: List to test in the improvedAverage() function. \n
        expected: True if the average of the last 10 elements is greater than the average of all others not including the last 10 elements, false if not. None if list is <20 elements. \n
    Function: Prints out the test case, expected result, and actual result in the event of a disagreement.
    """
    result = improvedAverage(test)
    if result != expected:
        print("Testing improvedAverage() with", test, "   Expected:", expected, " Got: ", result)

    
# List under 20 numbers should return None.
test = [67, 70, 65, 82, 91, 97, 80, 56, 67, 96, 92, 53, 86, 65, 69, 85, 69, 74, 95]
expected = None
test_results(expected,test)

# Testing proper list indexing 1/2. (1 in index 10)
test = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
expected = True
test_results(expected,test)

# Testing proper list indexing 2/2. (1 in index 9)
test = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
expected = False
test_results(expected,test)

# Base Functionality 1/2.
test = [10,10,10,10,10,10,10,10,10,10,11,11,11,11,11,11,11,11,11,11]
expected = True
test_results(expected,test)

# Base Functionality 2/2.
test = [11,11,11,11,11,11,11,11,11,11,10,10,10,10,10,10,10,10,10,10]
expected = False
test_results(expected,test)