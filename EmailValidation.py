def ask():
    email = input("Enter your Email: ")
    return email


def validation(email):
    k=0
    for i in email:
            if i.isspace():
                k=1
    if not email[0].isalpha():
        print("First letter should be alphabet")
        
    elif len(email)<6:
        print("Email should atleast be 6 characters long")

        
    elif not email.islower():
        print("Email address can't have upper case")
    
    elif " " in email:    
        print("There should'nt be any spaces in the email address")
        
    elif email.count("@")!=1:
        print("Email should have exactly one '@' ")
            
    
        
    elif not email.endswith(".com"):
        print("Email must end with '.com'")
        
    else:
        print("VAlid email")
val= ask()  
res= validation(val)