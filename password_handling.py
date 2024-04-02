# password_handling.py 3
import json
import hashlib

def store_password_and_hash():
    p = input("Enter the password:-")
    
    file_name = 'userfriend.json'
    with open(file_name, 'w') as obj:
        json.dump(p, obj)
    
    userfriend = p
    
    a = hashlib.sha512(p.encode('utf-8')).hexdigest()
    
    file_name = 'newpass.json'
    with open(file_name, 'w') as obj:
        json.dump(a, obj)
    
    newpass = a
    
    n = input("Enter the old password:-")
    
    filename = 'oldpass.json'
    with open(filename, 'w') as obj:
        json.dump(n, obj)
    
    oldpass = hashlib.sha512(n.encode('utf-8')).hexdigest()
    
    return userfriend, newpass, oldpass
