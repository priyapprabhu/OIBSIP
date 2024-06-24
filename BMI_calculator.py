''' Create a command-line BMI calculator in Python. Prompt users for their weight (in kilograms) 
and height (in meters). Calculate the BMI and classify it into categories (e.g., underweight, normal, overweight) 
based on predefined ranges. Display the BMI result and category to the user.'''

def calculate_BMI(weight, height):
    return weight / (height **2)

def BMI(bmi):
    if bmi < 18.5:
        return "Underweight" 
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
    
def main():
    weight = float(input("Enter the weight in kg:"))
    height = float(input("Enter the height in m:")) 

    if weight <= 0 or height <=0:
        print("Weight and Height must be positive.")
        return
    
    bmi = calculate_BMI(weight, height)
    category = BMI(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category} ")

main()

