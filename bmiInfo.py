def bmi_calc():
    height1 = float(input("Enter the feet part of your height: "))
    height = float(input("Enter the inches part of your height : "))
    weight = float(input("Enter your weight in pounds (lb): "))
    height = (height1*12) + height
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