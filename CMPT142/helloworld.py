# CMPT 142 Assignment 0
# -------------------------------------------
# Name: Jeffrey Hamilton
# NSID: nfj513
# Date Created: October 16th, 2024, 11:20am
# Date Modified: October 16th, 20242 11:45am
# -------------------------------------------
# Purpose: Print "Hello, World!" in an overly complicated way for no reason.
# 
# Simple Solution: print("Hello, World!")


# Interlaces two lists into a string. (Makes list_1 odd indexes and list_2 even indexes)
def interlace_lists_to_string(list_1,list_2):
    output_str = ''
    for char1,char2 in zip(list_1,list_2):
        output_str += char1 + char2
    return(output_str)


# Prints the interlaced string of two lists that come together to make "Hello, World!"
print(interlace_lists_to_string(['H','l','o',' ','o','l','!'],['e','l',',','W','r','d','']))