# Calculate Average Temperature Using Array
import array as arr
my_array = arr.array('i')
def Calc_Avg_Temp(temp_list, n):
    for i in range(n):
        temp_input = int(input(f"Enter day {i+1} temp: "))
        my_array.append(temp_input)
    
    avg = sum(my_array) // len(my_array)
    print(f"Average Temperature: {avg}")

    count_above_avg = 0
    for idx, temp in enumerate(temp_list):
        if temp > avg:
            print(f"The temperature {temp} of day {idx+1} is above the avg temp {avg}.")
            count_above_avg += 1
    print(f"Total number of days above average temperature: {count_above_avg}")

n = int(input("How many days you want to calculate avg temp for? "))
Calc_Avg_Temp(my_array, n)
