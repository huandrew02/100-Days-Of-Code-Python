print("BMI")

weight = float(input('What is your weight in kg: '))
height = float(input('What is your height in m: '))
bmi = weight / (height**2)

user_weight = ''
if bmi <= 18.5:
    user_weight = 'underweight'
elif bmi <= 25:
    user_weight = 'normal weight'
elif bmi <= 30:
    user_weight = 'slightly overweight'
elif bmi <= 35:
    user_weight = 'obese'
else:
    user_weight = 'clinically obese'

print(f'Your BMI is {round(bmi)}, you are {user_weight}.')