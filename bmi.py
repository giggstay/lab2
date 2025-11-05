def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight/(height*height)
    print("BMI ="+str(bmi))
    if bmi <= 18.5:
        print("Underweight"+" -1")
    
    elif bmi >=25:
        print("Overweight"+" 1")
    
    else:
        print("Normal Weight"+" 0")
    
calculate_bmi(weight=57, height=1.73)