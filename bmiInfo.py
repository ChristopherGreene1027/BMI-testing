def main():
    print("\n=======BMI CALCULATOR=======")
    print("\nWelcome to the BMI calculator! Enter your measurements below.\n")
    choice = str(input("\nTo continue, type 'y'. To exit, type 'n': "))

#takes in user data

    height_feet = float(input("Enter the feet part of your height: "))
    height_inches = float(input("Enter the inches part of your height : "))
    weight = float(input("Enter your weight in pounds (lb): "))

#prompts user 

    if choice == 'y':
        bmi_calc(height_feet, height_inches, weight)
        return 0
    if choice == 'n':
        print("Good day!")
    else: 
        print("Invalid input. Please try again.")

    

def bmi_calc(height_feet, height_inches, weight):
    total_height_inches = (height_feet*12) + height_inches
    bmi = round(float((weight*703)/(total_height_inches*total_height_inches)), 2)
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


if __name__ == "__main__":
    main()