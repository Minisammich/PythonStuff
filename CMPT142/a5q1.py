#  CMPT-142 - A5Q1 - Reverse Phrase
#  Function: Use recursion to reverse the order of a sentence.
#  ---------------------------------------------
#  Created by: Jeffrey Hamilton, nfj513, 11393559.
#  Created on: December 10th, 2024, 10:15am.
#  Last modified: December 10th, 2024, 12:00pm.
#  ---------------------------------------------

def reverse_phrase(sentence: str) -> str:
    """
    Parameter: sentence: String containing multiple words seperated by spaces.
    Output: Reverse word order of the input "sentence"
    """
    # Splits string to list to process it.
    sentence_list = sentence.split()
    # Returns the output of the recursive_re
    return(recursive_reverse(sentence_list,len(sentence_list)-1))
    

def recursive_reverse(sentence_list: list, i: int) -> str:
    """
    Parameters: sentence_list: List containing the words from the input of reverse_phrase.
                        i: Integer value of the recursion depth.
    Output: String of the reverse of the input list.
    Function: Moves the "i-1"th element of the list to the last index, done recursively with a depth (initial i value) of the length 
                    of the list minus one (last element is skipped because it's already in the last index) such as to reverse the order of the list.
    """
    if i == 0: # Recursion depth has been reached.
        return(" ".join(sentence_list)) # Returns list elements as a string seperated by spaces.
    else: # Recursion depth has NOT been reached.
        m_sent_list = sentence_list
        m_sent_list.append(m_sent_list[i-1]) # Takes "i-1"th element and puts it at the last position of the list.
        m_sent_list.pop(i-1) # Removes the "i-1"the element from the list.
        return recursive_reverse(m_sent_list,i-1) # Recursively runs the function decreasing i by one each time.
    
print(reverse_phrase("Do I Choose You Pikachu"))