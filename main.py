# main.py 1
from user_selection import select_user
from password_handling import store_password_and_hash
from login_verification import verify_login
from password_strength import check_password_strength

def main():
    select_user()
    
    userfriend, newpass, oldpass = store_password_and_hash()
    
    verify_login(oldpass, newpass)
    
    n = input("Enter the password to check its strength: ")
    if check_password_strength(n):
        print("Good password")
    else:
        print("Bad password")

if __name__ == "__main__":
    main()
