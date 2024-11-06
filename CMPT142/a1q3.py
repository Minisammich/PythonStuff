#  CMPT-142 - A1Q3 - Paint cost calculator.
#  Function: Calculates the cost of paint for
#  a square house with a pyramid roof.
#  ---------------------------------------------
#  Created by: Jeffrey Hamilton, nfj513, 11393559.
#  Created on: November 4th, 2024, 4:10pm
#  Last modified: November 5th, 2024, 2:20pm.
#  ---------------------------------------------

# Function to calculate area of all 4 walls based on the width and height.
def area_of_walls(w,h):
    area = w*h*4
    return(area)

# Function to calculate the area of all 4 isoceles triangles in the roof based on width and slant height.
def area_of_roof(w,t):
    area = 4*w*(t/2)
    return(area)

# Function to calculate the total cost using the areas of the walls and roof given by the two above functions.
def paint_cost_calculator(w,h,t,paint_cost):
    total_sq_m = (area_of_walls(w,h) + area_of_roof(w,t))
    cost_per_sq_m = total_sq_m*paint_cost
    return(cost_per_sq_m, total_sq_m)


# Prints the title.
print("|Paint Cost Calculator|")

# Gathers needed measurements from the user.
width = float(input("Enter the width of the house: "))
height = float(input("Enter the height of the walls: "))
slant_height = float(input("Enter the slant height of the roof: "))
paint_cost = float(input("Enter the cost of paint per square metre: "))

# Uses the functions to calculate the total paint cost based on the given dimensions.
total_cost, total_area = paint_cost_calculator(width,height,slant_height,paint_cost)
total_cost = round(total_cost,2)

# Prints the total paint cost in a sentence.
print(f"The cost to paint the entire house will be ${total_cost} and cover {total_area} square metres.")