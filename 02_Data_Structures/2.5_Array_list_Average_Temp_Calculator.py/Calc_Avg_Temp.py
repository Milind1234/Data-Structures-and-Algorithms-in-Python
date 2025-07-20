# Calculate Average Temperature
my_list = list()
def Calc_Avg_Temp(list,n):
    for i in range(n):
        temp_input =int(input(f"Enter day {i+1} temp: "))
        list.append(temp_input)
    avg = sum(list) // len(list)
    print(avg)

n=int(input("how many days you want to cal avg temp: "))
Calc_Avg_Temp(my_list,n)
