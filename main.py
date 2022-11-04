# input height in meters and weight in kilograms 

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Convert weight in integer and Height into float 

bmi = int(weight)/float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)