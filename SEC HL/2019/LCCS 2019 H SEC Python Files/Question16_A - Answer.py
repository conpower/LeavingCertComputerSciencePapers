# Question 16(a)
# Examination Number:

def display_intro():
    print("Welcome to my BMI calculator!") #(v)

display_intro()
weight = int(input("Enter weight (in kilograms): ")) # read weight (i)
height = int(input("Enter height (in cm): ")) # centimetres (ii)

bmi = weight / pow(height,2) * 10000 #(iv)

print("BMI is: ", round(bmi,1)) #(iii)

#(vi)
if bmi < 18.5: 
    print('Underweight')
elif bmi >=18.5 and bmi <=25.9:
    print('Normal')
elif bmi >=25 and bmi <=29.9:
    print('Overweight')
else:
    print('Obese')