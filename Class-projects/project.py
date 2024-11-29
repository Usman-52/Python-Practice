import ast

select = input("What would you like Read or Write for Read = 'W' & Write = 'R' \n" )

if select.lower().strip() == "w":
    
    entries = int(input("How many Entries Would you like to Enter ? \n"))
    i = 0
    
    while i < entries:
        rollNo = int(input("Kindly Enter your Roll Number: \n"))
        name = input("kindly Enter your Name : \n")
        subjects = {
            "Professional Practice": int(input("Enter your Professional Practice subject Marks \n")),
            "AI": int(input("Enter your AI Subject Marks: \n")),
            "Web Design and Development": int(input("Enter your Web Design & Development Subject Marks: \n")),
            "Economics": int(input("Enter your Economics subject Marks: \n")),
            "NoSQL": int(input("Enter your NoSQL subject Marks: \n")),
            "Networking": int(input("Enter your Networking subject Marks: \n"))
        }
        
        with open("students-record.txt") as file:
            file.write(f"Roll No: {rollNo} \n Name: {name} \n Subjects-Marks: {subjects} \n")
            
    i += 1
# elif select.lower().strip() == "r":
    
        