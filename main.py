from bmiInfo import * 

def main():
    print("\n=======BMI CALCULATOR=======")
    print("\nWelcome to the BMI calculator! Enter your measurements below.\n")
    choice = str(input("\nTo continue, type 'y'. To exit, type 'n': "))

    if choice == 'y':
        bmi_calc()
    else: 
        print("Invalid input. Please try again.")

  

if __name__ == "__main__":
    main()

