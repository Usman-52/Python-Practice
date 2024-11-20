
#?===================================== FUNCTIONS =================================#

# def greeting():
#     print("Hello")
    
# greeting()

#? ====================== Function With Parameters =========================#


# def greeting(name, rollNo = " Not Unknown"):
#     print(f"Hello Mr. {name}, your RollNo is {rollNo}")
    
# # greeting("Usman")
# greeting(name = "Khan", rollNo = "48") #* Keyword Arguments


#?==================== if the arguments are unknown =========================#

# def sum(*num):
#     result = 0
#     for number in num:
#         result = result + number
        
#     print(result)
# sum(10, 20, 30)

#?===================== when you have unknown Keyword Arguments =================#

# def studentRecord(**record):
#     for i in record:
#         print(i)

# studentRecord(name = "Hadi", rollNo = 3, regNo = "AUP-2021-3134")

#?======================= Return keyword in function ===========================#

# def multi(*sum1):
#     stor = 0
    
#     for i in sum1:
#         stor = stor + i
#     return stor
# finalResult = multi(10 , 10) * 2
# print(finalResult)