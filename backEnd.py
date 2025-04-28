import sys

def booking():
    bookings = open("bookings.txt", "a+") 
    
    print("\nWhat would you like to book a consultation for?\n")
    print("1. Solar Panel Installation\n")
    print("2. Solar Panel Maintenance\n")
    print("3. EV Charger Installation\n")
    serviceChoice = input("To choose a service, enter the corresponding number: ")
    
    print("\n----------")
    print("BOOKING FORM")
    print("\nYour Information:")
    
    name = input("Name: ")
    
    while len(name) < 2:   # If name is less than 2 characters long:
        print("\nInvalid name - must be at least 2 characters long.\nPlease enter another name.\n")
        name = input("Name: ")
    else:
        pass
    
    while name.isalpha == False:    # If name includes a special character or number:
        print("\nInvalid name - numbers and special characters cannot be used.\n")
        name = input("Name: ")
    else:
        pass
    
    email = input("Email Address: ")
    
    while email.count("@") != 1:    # If email does not include @ symbol:
        print("Invalid email address. Please try again.\n")
        email = input("Email Address: ")
    else: 
        pass
    
    while len(email) < 5:  # If email is under 5 characters long:
        print("\nInvalid email - must be at least 5 characters long.\nPlease enter another email.\n")
        email = input("Email: ")
    else:
        pass
    
    phoneNum = input("Phone Number (starting in 07): ")
    
    while len(phoneNum) < 10 and len(phoneNum) > 11:   # If phone number is not 10 or 11 characters long:
        print("\nInvalid phone number - must be at 10 / 11 characters long.\nPlease enter another phone number.\n")
        phoneNum = input("Phone Number: ")
    else:
        pass
    
    while phoneNum[:2] != "07":     # If the first 2 characters in the number are not 07:
        print("\nInvalid phone number - must begin with 07.\nPlease enter another phone number.\n")
        phoneNum = input("Phone Number: ")
    else:
        pass
    
    while phoneNum.isnumeric == False:  # If the phone number includes any letters:
        print("Invalid phone number - must only include numbers. Please try again.\n")
        phoneNum = input("Phone Number: ")
    else: 
        pass
    
    address = input("Home Address: ")
    
    while any(char.isdigit() for char in address):   # If address does not include a number:
        break
    else: 
        print("Invalid home address - must include a house number. Please try again.\n")
        address = input("Home Address: ")
        
    while len(address) < 10:   # If address is under 10 characters long:
        print("\nInvalid address - must be at least 10 characters long.\nPlease enter another address.\n")
        address = input("Home Address: ")
    else:
        pass
    
    postcode = input("Postcode: ")
    
    while len(postcode) < 2:  # If postcode is under 2 characters long:
        print("\nInvalid postcode - must be at least 2 characters long.\nPlease enter another postcode.\n")
        postcode = input("Postcode: ")
    else:
        pass
    
    
    print("")
    print("Time and Date:")
    print("Please enter the date in DD/MM/YY format, and the time in HH:MM format.")
    print("Available working hours: 7am - 9pm")
    print("Example: 13/07/25\n         15:30")
    
    
    # If this time is already full on this day:
    validDate = 0
    
    while validDate != 1:
        date = input("Date: ")
        
        def dateDetails():
            global dateBreakdown
            dateBreakdown = date.split("/")
            dateBreakdown = list(map(int, dateBreakdown))
            
        dateDetails()
    
        while dateBreakdown[0] > 31:   # If the day is over 31:
            print("Invalid date, please try again:\n")
            date = input("Date: ")
            dateDetails()
        else: pass
            
        while dateBreakdown[1] > 12:   # If the month is over 12:
            print("Invalid date, please try again:\n")
            date = input("Date: ")
            dateDetails()
        else: pass
        
        while dateBreakdown[2] < 25:   # If the year is in the past
            print("Invalid date - date must be in the future.\nPlease try again:\n")
            date = input("Date: ")
            dateDetails()
        else: pass
        
        time = input("Time: ")
        
        def timeDetails():
            global timeBreakdown 
            timeBreakdown = time.split(":")
            timeBreakdown = list(map(int, timeBreakdown))
        
        timeDetails()
        
        while timeBreakdown[0] > 24:
            print("Invalid time, please try again:\n")
            time = input("Time: ")
            timeDetails()
        else: pass
        
        while timeBreakdown[1] > 59:
            print("Invalid time, please try again:\n")
            time = input("Time: ")
            timeDetails()
        else: pass
        
        while timeBreakdown[0] < 7 or timeBreakdown[0] > 21:
            print("Sorry! This time is outside of our working hours.\nPlease try again:")
            time = input("Time: ")
            timeDetails()
        else: pass
        
        
        bookedDate = (date +", "+ time)
        
        if bookedDate in open("bookings.txt").read():
            print("Sorry! This time has already been booked. Please enter a different date or time:")
        else: 
            validDate = 1
    
    bookings.write("\n-----" + "\n" + serviceChoice + ", " + name + ", " + email + ", " + phoneNum + ", " + address + ", " + postcode + ", " + date + ", " + time)
    print("\nThank you for booking a consultation!")
    print("You should get an email from our team soon. We look forward to meeting you!")

#-------------------------------------------------------------

def feedback():
    feedbackDoc = open("feedback.txt", "a+")
    print("\nWhat would you like to give feedback for?\n")
    print("1. Service / Consultation")
    print("2. Website")
    userChoice = int(input())
    if userChoice == 1:
        print("\n----------")
        print("SERVICE / CONSULTATION FEEDBACK FORM:")
        print("     * These fields are required.\n")
        name = input("*Name: ")
    
        while len(name) < 2:   # If name is less than 2 characters long:
            print("\nInvalid name - must be at least 2 characters long.\nPlease enter another name.\n")
            name = input("*Name: ")
        else:
            pass
        
        while name.isalpha == False:    # If name includes a special character or number:
            print("\nInvalid name - numbers and special characters cannot be used.\n")
            name = input("*Name: ")
        else:
            pass
        
        email = input("*Email Address: ")
    
        while email.count("@") != 1:    # If email does not include @ symbol:
            print("Invalid email address. Please try again.\n")
            email = input("*Email Address: ")
        else: 
            pass
        
        while len(email) < 5:  # If email is under 5 characters long:
            print("\nInvalid email - must be at least 5 characters long.\nPlease enter another email.\n")
            email = input("*Email Address: ")
        else:
            pass
        
        date = input("Date of Consultation: ")
        time = input("Time of Consultation: ")
        feedback = input("Feedback:\n")
        
        while feedback == "":
            print("Please enter feedback.")
            feedback = input("*Feedback:\n")
        else: pass
        
        feedbackDoc.write("\n-----" + "\n" + name + ", " + email + ", " + date + ", " + time + ", " + feedback)
        
        print("\nThank you for your feedback!")
        
    elif userChoice == 2:
        print("\n----------")
        print("WEBSITE FEEDBACK FORM:")   
        print("     * These fields are required.\n")
        name = input("*Name: ")
    
        while len(name) < 2:   # If name is less than 2 characters long:
            print("\nInvalid name - must be at least 2 characters long.\nPlease enter another name.\n")
            name = input("*Name: ")
        else:
            pass
        
        while name.isalpha == False:    # If name includes a special character or number:
            print("\nInvalid name. Numbers and special characters cannot be used.\n")
            name = input("*Name: ")
        else:
            pass
        
        email = input("*Email Address: ")
    
        while email.count("@") != 1:    # If email does not include @ symbol:
            print("Invalid email address. Please try again.\n")
            email = input("*Email Address: ")
        else: 
            pass
        
        while len(email) < 5:  # If email is under 5 characters long:
            print("\nInvalid email - must be at least 5 characters long.\nPlease enter another email.\n")
            email = input("*Email Address: ")
        else:
            pass
      
        feedback = input("*Feedback:\n")
        
        while feedback == "":
            print("Please enter feedback.")
            feedback = input("*Feedback:\n")
        else: pass
        
        feedbackDoc.write("\n-----" + "\n" + name + ", " + email + ", " + feedback)
        
        print("\nThank you for your feedback!")
    else: 
        print("Invalid choice.\nPlease try again:")
        userChoice = int(input("\n")) 

#-------------------------------------------------------------

def detailsChange():
    textFind = input("Please enter previous details / date / time:\n")
    textReplace = input("New details / date / time: ")
    with open ("bookings.txt","r") as file:
        newData = file.read()
        while textFind not in newData:
            print("Error: Information not found, please try again.\n")
            textFind = input("Please enter previous details / date / time:\n")
            textReplace = input("New details / date / time: ")
        else:
            newData = newData.replace(textFind, textReplace)
                
    with open ("bookings.txt","w") as file:
        file.write(newData)


def alterDetails():
    print("\n----------")
    print("What would you like to change?")
    print("1. Contact Details")
    print("2. Time or Date")
    userChoice = input()
    if userChoice == "1":
        emailorNum = input("Which would you like to alter?\n\n1. Email\n2. Phone Number\n")
        if emailorNum =="1":
            detailsChange()   
            print("\nYour email address has been changed.")
        elif emailorNum =="2":
            detailsChange()
            print("\nYour phone number has been changed.")
            
    elif userChoice =="2":
        timeorDate = input("Which would you like to alter?\n\n1. Date\n2. Time\n")
        if timeorDate =="1":
            detailsChange()
            print("\nThe date of your consultation has been changed.")
        elif timeorDate =="2":
            detailsChange()
            print("\nThe time of your consultation has been changed.")

#-------------------------------------------------------------

def userAction():
    choice = "0"
    while choice == "0":
        print("\nWhat would you like to do?\n")
        print("1. Book a Consultation")
        print("2. Manage a Consultation")
        print("3. Give Feedback")
        print("4. Log Out")
        choice = input("\n")
            
        while choice == "1":
            booking()
            print("\nWhat would you like to do?\n")
            print("1. Book a Consultation")
            print("2. Manage a Consultation")
            print("3. Give Feedback")
            print("4. Log Out")
            choice = input("\n")
        else: pass
            
        while choice =="2":
            alterDetails()
            print("\nWhat would you like to do?\n")
            print("1. Book a Consultation")
            print("2. Manage a Consultation")
            print("3. Give Feedback")
            print("4. Log Out")
            choice = input("\n")
            
        while choice == "3":
            feedback()  
            print("\nWhat would you like to do?\n")
            print("1. Book a Consultation")
            print("2. Manage a Consultation")
            print("3. Give Feedback")
            print("4. Log Out")
            choice = input("\n")
        else: pass
            
        while choice == "4":
            sys.exit("\nYou have been logged out.")
            break
        else: pass
            
        while choice != "1" or choice != "2" or choice != "3" or choice != "4": 
            print("Invalid choice, please try again:")
            choice = input("\n")   
        else: pass    
        
        
#-------------------------------------------------------------
    
def signUp():
    print("\n----------")
    print("Want to stay in the know about Rolsa Technologies and our services?\nCreate an account today.\n")
    
    name = input("Name: ")

    while len(name) < 2:   # If name is less than 2 characters long:
        print("\nInvalid name - must be at least 2 characters long.\nPlease enter another name.\n")
        name = input("Name: ")
    else:
        pass
    
    while name.isalpha == False:     # If name includes a special character or number:
        print("\nInvalid name. Numbers and special characters cannot be used.\n")
        name = input("Name: ")
    else:
        pass
    
    
    email = input("Email Address: ")
    
    while email.count("@") != 1:    # If email does not include @ symbol:
        print("Invalid email address. Please try again.\n")
        email = input("Email Address: ")
    else: 
        pass
    
    while len(email) < 5:   # If email is under 5 characters long:
        print("\nInvalid email - must be at least 5 characters long.\nPlease enter another email.\n")
        email = input("Email: ")
    else:
        pass
    
    # If email is already used:
    accounts = open("accounts.txt", "a+") # Opens the 'accounts' text file  
    
    while email in open("accounts.txt").read():
        print("This email address is already in use. Please try a different one.\n")
        email = input("Email Address: ")
    else:
        pass
        
        
    password = input("Password (Minimum 6 Characters): ")
    
    while len(password) < 6:     # If password is under 6 characters:
        print("\nInvalid password - must be at least 6 characters long.\nPlease enter another password.\n")
        password = input("Password: ")
    
    accounts.write("\n-----" + "\n" + name + ", " + email + ", " + password)
    accounts.close()
    
    print("\nThank you for signing up!\nAn email has been sent to confirm your registration.")
    print("----------")
    userAction()
    
#-------------------------------------------------------------
    
def logIn():
    valid = 0
    print("\n----------")
    print("Already have an account?\nLog In\n")
    
    while valid != 1:   # While the input is not valid:
        email = input("Email address: ")
        password = input("Password: ")
        details = (email+ ", "+ password)
        
        if details in open("accounts.txt").read():  # Search the text file for the specified email and password.
            print("\nWelcome back\n")
            print("----------")
            userAction()
            valid = 1
        else:
            print("\nIncorrect username or password. Please try again:")
            
#-------------------------------------------------------------
 
print("\n----------")
print("Welcome to the Rolsa Technologies website\nWhat would you like to do?\n")
validChoice = 0
print("1. Sign Up")
print("2. Log In\n")

while validChoice == 0:
    userChoice = input("")
    
    if userChoice == "1":
        signUp()
        validChoice == 1
        
    elif userChoice == "2":
        logIn()
        validChoice == 1
        
    else:
        print("\nInvalid choice, please try again.\n")