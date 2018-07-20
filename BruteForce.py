student = {'Ben': ["bird", "540-231-8746", "Math", "2000"], 'Nicole': ["dog", "914-606-0566", "English", "2001"], "Eli": ["cat", "917-664-5368", "History", "2002"]}
username = input ("please enter your username")
while not student.get(username):
    print("Please enter a valid user name")
    username = input ("enter username")
password = input ("please enter your password")
actualPassword = student[username][0]

while password != actualPassword:
    print("Incorrect, please try again.")
    password = input ("Please try again!")
    
if (student == actualPassword):
    print("Welcome to your account!!")
   
input ("would you like to update?")
if (input == "Yes"):
    changeNumber = input ("whose number do you want to change?")
    newNumber = input ("what is their new number?")
    changeSubject = input ("what is their new subject major?")
    student[changeNumber][1] = newNumber
    student[subject][2] = changeSubject
    print(student)
else:
    print("Ok, this is your phonebook right now:")
    print(student)
