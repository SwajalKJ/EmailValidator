email = input("Enter Your Email ID: ")
k,j,d = 0,0,0
if len(email) >= 6: #Email Length should be 6 or more than 6 of letters
    if email[0].isalpha(): #first letter in email should be a character
        if ('@' in email) and (email.count("@")==1): #there should be only one '@' symbol  
            if(email[-4] == ".") ^ (email[-3] == "."): # .com [-4] and .in[-3]
                for i in email:
                    if i == i.isspace(): #check for spaces in email
                        k = 1
                    elif i.isalpha():
                        if i == i.upper(): #check for uppercase letter
                            j = 1
                    elif i.isdigit(): #check for digits
                        continue
                    elif i == "_" or i == "." or i == "@": #check for Special Characters
                        continue
                    else: # check for symbols like "<", "|", "?", ","
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Your Email is Invalid (error code 5)") 
            else:
                print("Your Email is Invalid (error code 4)")    
        else:
            print("Your Email is Invalid (error code 3)")
    else:
        print("Your Email is Invalid (error code 2)")
else:
    print("Your Email is Invalid (error code 1)")

print("Your Email is Valid")
