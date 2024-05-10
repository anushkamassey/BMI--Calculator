height = float(input("Enter height in centimeter:"))
weight = float(input("Enter the weight in Kg:"))


height = height /100
BMI = weight / (height*height)


print("YOUR BMI is :", BMI)

if(BMI>0):
   if(BMI<=16):
       print("You are severely underweight")
   elif(BMI<=18.5):
       print("You are underweight")
   elif(BMI<=25):
       print("You are Healthy")
   elif(BMI<=30):
       print("You are overweight")
   else:
       print("You are Obese")
else:
    print("Enter valid details...")