import re #re is enabled to use re.search for efficiency

def passwordcheck(passwd): #def is introducing function
    if len(passwd) < 8:
        return "Pass must be at least 8 characters long" 
#return allows us to use the resily of the function for further computations of the programm
    if not re.search('[a-z]', passwd):
        return "Pass must contain at least one lowercase letter"
    if not re.search('[A-Z]', passwd):
        return "Pass must contain at least one uppercase letter"
    if not re.search('[0-9]', passwd):
        return "Pass must contain at least one number"
    if not re.search('[!@#$%^&*()_+=-`]', passwd):
        return "Pass must contain at least one speacial character"

    return "Password created"

while True:
    passwd = (input(""" Please create a password that contains:\n
        must be at least 8 characters long
        must contain at least one uppercase letter
        must contain at least one lowercase letter
        must contain at least one digit
        must contain at least one special character
        """))
    check = passwordcheck(passwd)
    print(check)
    if check == "Password created":
        break
    else:
        print("Try again, some of the criteria was not met")