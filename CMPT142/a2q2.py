#  CMPT-142 - A2Q2 - Plotting polynomials with Matplotlib
#  Function: Plot polynomials with different values input by the user.
#  ---------------------------------------------
#  Created by: Jeffrey Hamilton, nfj513, 11393559.
#  Created on: November 18th, 2024, 6:00pm.
#  Last modified: November 19th, 2024, 10:00pm.
#  ---------------------------------------------

# Importing any required libraries
import matplotlib.pyplot as plt


## USER INPUTS ##

# Getting user inputs for A, B, and C of the polynomial Ax^B+C
A, B, C = float(input("Input a value for A: ")), float(input("Input a value for B: ")), float(input("Input a value for C: "))

# If user inputs an integer, variable type gets converted to int in order to make the plot title cleaner (Removes decimal point).
# Not essential to the function of the program, but makes output more visually appealing.
if A%1 == 0:
    A = int(A)
if B%1 == 0:
    B = int(B)
if C%1 == 0:
    C = int(C)

# Getting user input for number of plots (How high the X value goes to from 0).
N = int(input("Number of plots?: "))


## CALCULATIONS ##

# Preparing empty lists to be filled with values.
x, y = [], []

# Filling x and y lists with values 0 -> N for x, and A(0)^B+C -> A(N)^B+C for y.
for i in range(N):
    x.append(i)
    y.append(A*(i**B)+C)


## PLOTTING ##

# Plotting the lists x and y.
fig, ax = plt.subplots(layout="constrained")
ax.plot(x,y)

# Setting title of plot using TeX to make a visually appealing title.
ax.set_title(r"$y = {{{}}}x^{{{}}}+{{{}}}$".format(A,B,C))

# Labelling x and y axes.
ax.set_xlabel("x")
ax.set_ylabel("y")

# Shows plot in plot window.
plt.show()