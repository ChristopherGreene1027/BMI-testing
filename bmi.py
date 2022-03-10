def bmi_calc():
    height = float(input("Enter your height in inches: "))
    weight = float(input("Enter your weight in pounds (lb): "))
    bmi = round(float((weight*703)/(height*height)), 2)
    print("Your bmi is: ", bmi)