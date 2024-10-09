import ast
read_or_write = input('To write in file Enter "w" and to search from file Enter "r" \n')
# condition for reading or writing in file
if read_or_write.lower().strip() == 'w':
    enteries = int(input('How many Enteries you want to add \n'))
    i = 0

# loops number of enteries
    while i < enteries:
        roll_no = int(input('Enter your Roll No \n'))
        name: str = input("Enter your name \n") 
        dic = {
        'AI':int(input("Enter your AI marks \n")),
        'Computer Network':int(input("Enter your Computer Network marks \n")),
        'NoSQL':int(input("Enter your NoSQL marks \n")),
        'Web Desing and Devlopment':int(input("Enter your Web Desing and Devlopment marks \n")),
        'Ecnomics':int(input("Enter your Ecnomics marks \n")),
        'Professional Practice':int(input("Enter your Professional Practice marks \n"))
    }
        
# Append data to file
        with open('students_result.txt','a+',) as file:
            file.write(f"Roll No:{roll_no} \nName: {name} \nSubjects_Marks:\n {dic} \n\n")
        i += 1
        
# condition check for reading data from file
elif read_or_write.lower().strip() == 'r':
    roll_no = int(input("Enter Roll No to search his details \n"))
    with open('students_result.txt', 'r') as file:
        l_sentences = file.readlines()
        counter = 0
        index = 0
        while counter < len(l_sentences):
            if str(roll_no).strip() in l_sentences[counter]:
                index = counter
                break
            else:
                pass
            
            counter = counter + 5

# calculating obtained marks and percentage for the require student
    total_marks = 600
    obtained_marks = 0
    
# The below line used to convert str to dict for futher calculation
    dic =  ast.literal_eval(l_sentences[index+3])
    for value in dic.values():
        obtained_marks += int(value )
    percentage = round((obtained_marks/total_marks) * 100,1)
        
    print(f'{l_sentences[index].strip()} \n{l_sentences[index+1].strip()} \nTotal_marks {obtained_marks} \nPercentage: {percentage}%')

else:
    print('Enter a valid input and Try again!!')