#  CMPT-142 - A2Q3 - 2023 Saskatoon High temperatures
#  Function: Calculates the average temperature highs of Saskatoon in 2023 by the month.
#  ---------------------------------------------
#  Created by: Jeffrey Hamilton, nfj513, 11393559.
#  Created on: November 19th, 2024, 10:00pm.
#  Last modified: November 19th, 2024, 11:10pm.
#  ---------------------------------------------

## FUNCTIONS ##

def Fahrenheit_To_Celsius(temp_f: float) -> float:
    """
    :param temp_f: Float value contaning a temperature in degrees Fahrenheit
    :outputs: A float value containing the temperature converted to Celsius
    """
    # Conversion factor from F to C.
    return (temp_f - 32)*(5/9) 

def List_Replace(input_list: list):
    """
    :param input_list: A list containing lists of temperatures in Fahrenheit
    :output: none
    """
    # Gets sublist and its index for each element in the input_list
    for m_index, month in enumerate(input_list):
        # Gets number and its index from each element of the sublist
        for t_index, temp in enumerate(month):
            # Replaces the value at [sublist index][number index] with its value converted from F to C.
            temperatures[m_index][t_index] = round(Fahrenheit_To_Celsius(temp),1)

def Monthly_Avg_Temp(input_list: list) -> list:
    """
    :param input_list: A list of lists corresponding to months containing daily temperatures
    :output: A list of monthly average temperatures corresponding to the months in input_list
    """
    # Empty avg list
    monthly_avg = []

    # Adds each element of a sublist together, divides it by the number of elements, rounds it, and appends it to the avg list.
    for month in input_list:
        monthly_sum = 0
        for temp in month:
            monthly_sum += temp
        monthly_avg.append(round(monthly_sum/len(month),2))

    # Returns the filled out monthly average list.
    return(monthly_avg)


## DATA ##

# Saskatoon 2023 high temperatures given in the starter file. Each sublist represents a month, starting from January.
temperatures = [
    [17.4, 17.6, 22.8, 14.2, 7.5, 9.9, 13.6, 16.7, 10.8, 14.0, 16.9, 14.4, 10.4, 17.6, 18.1, 20.3, 15.8, 21.9, 24.3, 20.3, 25.3, 34.3, 30.0, 20.8, 27.3, 38.7, 24.4, -0.4, -1.5, -2.2, 2.7], 
    [4.6, -3.3, 15.4, 26.6, 30.9, 32.2, 34.0, 28.8, 26.8, 37.6, 31.6, 32.5, 35.1, 30.0, 9.3, 21.7, 26.2, 19.4, 11.5, 5.4, -7.2, -16.8, -7.6, -2.9, 7.2, 16.2, 17.2, 10.8], 
    [17.6, 29.1, 30.0, 17.8, 7.5, 6.8, 9.7, 8.1, 11.8, 18.5, 19.6, 20.7, 25.0, 24.6, 21.6, 14.0, 16.3, 30.2, 23.9, 23.7, 21.2, 19.4, 32.0, 25.9, 24.6, 18.9, 12.6, 19.0, 28.6, 32.5, 32.0], 
    [32.0, 25.5, 18.0, 21.2, 21.2, 29.3, 36.5, 41.9, 43.9, 50.0, 48.7, 50.5, 51.6, 52.9, 56.8, 60.3, 62.1, 44.6, 31.3, 30.4, 37.6, 47.5, 52.2, 52.2, 61.5, 57.0, 53.8, 66.9, 59.9, 60.4], 
    [68.5, 80.2, 79.3, 80.2, 65.7, 63.7, 66.6, 68.7, 68.9, 72.1, 72.7, 68.9, 77.5, 81.0, 82.6, 87.6, 57.7, 63.1, 79.2, 75.2, 73.4, 85.8, 70.0, 63.7, 58.1, 68.2, 67.8, 71.6, 81.7, 84.0, 88.5], 
    [83.5, 74.8, 80.6, 87.4, 92.5, 77.2, 83.3, 84.7, 75.0, 76.8, 84.2, 88.3, 85.5, 88.9, 69.3, 77.5, 74.8, 77.4, 73.8, 72.0, 66.6, 75.2, 80.6, 82.9, 86.0, 77.2, 79.5, 74.1, 81.5, 86.5], 
    [90.7, 72.7, 65.7, 65.7, 75.4, 75.9, 74.8, 82.2, 85.3, 72.3, 69.4, 77.2, 77.4, 66.9, 73.8, 76.1, 79.2, 65.5, 75.7, 78.4, 83.1, 83.1, 84.0, 91.2, 91.2, 77.5, 65.3, 70.9, 75.0, 86.2, 91.4], 
    [85.8, 85.6, 99.5, 81.3, 79.7, 80.8, 79.5, 73.6, 72.7, 73.8, 67.6, 76.6, 79.2, 92.8, 85.3, 72.5, 87.1, 75.6, 67.8, 72.3, 67.1, 59.7, 69.3, 70.2, 72.7, 83.7, 81.1, 85.1, 89.8, 83.3, 67.6], 
    [80.8, 79.9, 79.5, 66.4, 62.2, 71.4, 66.6, 71.6, 75.7, 73.8, 67.8, 79.0, 72.1, 61.9, 71.2, 83.5, 87.4, 80.8, 65.5, 67.8, 72.0, 73.2, 71.8, 73.9, 79.3, 85.6, 73.2, 68.5, 65.5, 52.2], 
    [47.7, 52.2, 63.1, 55.4, 47.8, 52.2, 70.9, 72.0, 70.2, 67.5, 61.0, 46.0, 53.4, 53.2, 56.8, 62.8, 63.0, 60.8, 70.2, 60.3, 49.8, 50.4, 35.2, 26.2, 24.4, 30.6, 30.4, 26.1, 31.1, 26.8, 34.5], 
    [31.6, 40.6, 35.6, 39.2, 35.6, 37.2, 35.8, 38.7, 30.6, 37.2, 46.4, 46.4, 46.6, 45.9, 43.7, 38.7, 50.0, 52.7, 52.2, 41.5, 35.8, 25.9, 16.7, 36.3, 33.4, 20.5, 31.1, 43.3, 36.0, 30.2], 
    [30.2, 20.1, 24.6, 33.1, 36.1, 37.9, 38.1, 31.3, 28.6, 31.1, 27.5, 29.1, 41.4, 43.3, 39.6, 39.6, 34.5, 29.7, 27.1, 36.3, 33.6, 42.1, 35.6, 28.8, 33.3, 42.8, 38.1, 43.2, 31.8, 32.0, 34.7]
    ]


## CALCULATION AND DATA FORMATTING ##
        
# List of the names of each month.
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Replaces Fahrenheit values with their repsective value in Celsius.
List_Replace(temperatures)

# Gets the monthly averages of the data.
monthly_avg = Monthly_Avg_Temp(temperatures)


## PRINTING TO CONSOLE##

# Prints the title of what the data is for
print('''2023 Saskatoon average temperature highs.
-------------------------------------------------''') # Opening data separator

# Prints each average high with it's corresponding month.
for i in range(len(monthly_avg)):
    print(f"The average temperature in {months[i]} was: {monthly_avg[i]}°C")

# Closing data separator
print("-------------------------------------------------") 
