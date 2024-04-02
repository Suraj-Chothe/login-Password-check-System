# password_strength.py 5
def check_password_strength(password):
    has_upper = has_lower = has_num = False
    
    for x in password:
        if 'A' <= x <= 'Z':
            has_upper = True
        elif 'a' <= x <= 'z':
            has_lower = True
        elif '0' <= x <= '9':
            has_num = True
    
    return len(password) >= 8 and has_upper and has_lower and has_num
