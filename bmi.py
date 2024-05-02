def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

if __name__ == "__main__":
    main()

def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height ** 2)
    print("BMI = {:.2f}".format(bmi))

def display_main_menu():
    print("display_main_menu")
def get_user_input():
    print("user_input")

def calc_average(): 
    print(“calc_average”)