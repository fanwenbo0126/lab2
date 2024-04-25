def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    # Calculate BMI using the formula
    bmi = weight / (height ** 2)
    
    # Display calculated BMI
    print("BMI = {:.2f}".format(bmi))

calculate_bmi(weight=57, height=1.73)
