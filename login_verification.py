# login_verification.py 4
def verify_login(old_pass, newpass):
    while True:
        if old_pass == newpass:
            print("Login Successfully!")
            break
        elif old_pass != newpass:
            print("Try Again!!!")
            break
        response = input('Would you want to try again (type y or n):-')
        
        if response == 'n':
            break
