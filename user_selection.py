# user_selection.py 2
def select_user():
    usernew = []
    users = ['admin', 'employe', 'manager', 'worker', 'staff']
    x = input("Enter the postname:- 1) admin 2) employe 3) manager 4) worker 5) staff:-")
    usernew.append(x)
    
    for user in users:
        if x == user:
            print(f"Hello {user}, register first")
            break
    else:
        print("Hello staff, register first")
