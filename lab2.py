print ("helloworld")
def funcName(parameter1, parameter2): 

    def display_main_menu():
         print("display_main_menu")

def display_main_menu():
    print("Main Menu:")
    print("1. Option 1")
    print("2. Option 2")
    # Add more options as needed

def get_user_input():
    temperatures = []
    num_temps = int(input("Enter the number of temperatures: "))
    for i in range(num_temps):
        temperature = float(input("Enter temperature {}: ".format(i+1)))
        temperatures.append(temperature)
    return temperatures

def calc_average(temperatures):
    if not temperatures:
        return None
    return sum(temperatures) / len(temperatures)

def find_min_max(temperatures):
    if not temperatures:
        return None
    return [min(temperatures), max(temperatures)]

def sort_temperature(temperatures):
    if not temperatures:
        return None
    return sorted(temperatures)

def calc_median_temperature(temperatures):
    if not temperatures:
        return None
    sorted_temps = sorted(temperatures)
    n = len(sorted_temps)
    if n % 2 == 0:
        return (sorted_temps[n//2 - 1] + sorted_temps[n//2]) / 2
    else:
        return sorted_temps[n//2]
