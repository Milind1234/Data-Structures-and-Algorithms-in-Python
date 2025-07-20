# Calculate Average Temperature
my_list = []

def Calc_Avg_Temp(temp_list, n):
    for i in range(n):
        temp_input = int(input(f"Enter day {i+1} temp: "))
        temp_list.append(temp_input)
    
    avg = sum(temp_list) // len(temp_list)
    print(f"Average Temperature: {avg}")
    
    for idx, temp in enumerate(temp_list):
        if temp > avg:
            print(f"The temperature {temp} of day {idx+1} is above the avg temp {avg}.")

n = int(input("How many days you want to calculate avg temp for? "))
Calc_Avg_Temp(my_list, n)
