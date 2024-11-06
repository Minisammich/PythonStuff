#  CMPT-142 - A1Q2 - Fuel Cost Calculator.
#  Function: Calculate the cost of a roadtrip
#  based on distance of the trip, fuel cost,
#  and fuel efficiency (MPG) of the car.
#  ---------------------------------------------
#  Created by: Jeffrey Hamilton, nfj513, 11393559.
#  Created on: November 4th, 2024, 3:30pm.
#  Last modified: November 4th, 2024, 4:00pm.
#  ---------------------------------------------


# Function receives data about a planned trip, and gives the total fuel consumption and cost, along with converting fuel efficiency to metric for the user.
def roadtrip_cost_calculator(fuel_cost, mpg, distance):
    '''
    :params: (float, float, float) => (fuel_cost, mpg, distance)
    :output: (tuple) => 3 elements => refuel_cost, litres_used, litres_per_100km 
    '''
    litres_per_100km = 235.215/mpg # Converts MPG to L/100km
    litres_used = distance*(litres_per_100km/100) # Converts L/100km to L/km and multiplies it by the planned distance (km) to give total fuel consumption.
    refuel_cost = litres_used*fuel_cost # Calculates total cost of fuel by multipyling fuel cost and litres used.
    return(refuel_cost, litres_used, litres_per_100km) # Outputs refuel cost, litres used, and L/100km into a list to be used in its parts later.

# Asks user to input their planned roadtrip distance(km), fuel efficiency(mpg), and fuel cost($/L).
distance = float(input("Enter the distance of your roadtrip (km): "))
mpg = float(input("Enter the fuel efficiency of your car (MPG): "))
fuel_cost = float(input("Enter cost of fuel per litre: "))


# Assigns the returned tuple from the function to a their respective variable,
# rounds fuel efficiency to 2 decimal places and fuel usage and cost to 3 decimal points.
roadtrip_cost, roadtrip_fuel_usage, metric_fuel_econ = roadtrip_cost_calculator(fuel_cost, mpg, distance)

roadtrip_cost = round(roadtrip_cost,3)
roadtrip_fuel_usage = round(roadtrip_fuel_usage,3)
metric_fuel_econ = round(metric_fuel_econ,2)

# Prints out a sentence with all the desired information for the user.
print(f"At an efficiency of {mpg}MPG or {metric_fuel_econ}L/100km your roadtrip will consume about {roadtrip_fuel_usage} litres, which will cost ${roadtrip_cost}.")