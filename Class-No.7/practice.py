
#? ================================= if else / elif condition ===================================//

#? students grade finder 

std_marks = int(input("How much marks you got it :"))

if (std_marks >= 90 and std_marks <= 100):
    grade = "A"
elif(std_marks >= 80 and std_marks <= 89):
    grade = "B"
elif(std_marks >= 70 and std_marks <= 79):
    grade = "C"
elif(std_marks >=60 and std_marks <=69):
    grade = "D"
else:
    print("Oh you are Fail")
    
print(f"You got Grade : ", grade)

#? Check that the user entered an even number or odd 

entered_number = int(input("Please any number : "))
if (entered_number % 2 == 0):
    print(f"{entered_number} is Even")
else:
    print(f"{entered_number} is Odd")

#? Find Greater number among entered 3 numbers

entered_number1 = int(input("Enter the first number: \n"))
entered_number2 = int(input("Enter the second number: \n"))
entered_number3 = int(input("Enter the third number: \n"))

if(entered_number1 > entered_number2 > entered_number3):
    print(f"{entered_number1} is the Greater number")
elif(entered_number2 > entered_number3):
    print(f"{entered_number2} is the Greater number")
else:
    print(f"{entered_number3} is the Greater number")

#? Check if the number is multiple by 7 or not 

entered_Number = int(input("Please Enter Any Number : "))
if (entered_Number % 7 == 0):
    print(f"{entered_Number} is multiple of 7")
else:
    print(f"{entered_Number} is not multiple of 7")