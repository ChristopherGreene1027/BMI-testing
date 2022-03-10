def bmi_calc():
    height = float(input("Enter your height in inches: "))
    weight = float(input("Enter your weight in pounds (lb): "))
    bmi = round(float((weight*703)/(height*height)), 2)
    print("Your bmi is: ", bmi)

    # BMI classification

    if bmi <= 18.5:
        print("Classification: Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Classification: Normal Weight")
    elif 25 <= bmi < 29.9:
        print("Classification: Overweight")
    elif 30 <= bmi: 
        print("Classification: Obese")
    else: 
        print("System error or incorrect BMI values. Please retry.")