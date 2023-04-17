#!python

import db
import password_utils

def register(username, password, email):
    user_id = db.create_user(username, password, email)
    if user_id:
        return True
    else:
        return False
        
#provjera korisnika
def authenticate(username, password):
    user = db.get_user(username)
    #ako postoji user i verify_password vraca true i usera
    if user and password_utils.verify_password(password, user[3]):
        return True, user[0]
    #ako postoji user, ali je kriva lozinka vrati usera i none tako da mogu
    #ispisati koji mi je error u login.py
    elif user and not password_utils.verify_password(password, user[3]):
        return True, None
    elif not user:
        return False, None
    else:
        return False, None
        
def change_password(username, old, new, new2):
    user = db.get_user(username)
    #dovoljan broj uvjeta za ispis ako bude greske u change.py
    if password_utils.verify_password(old, user[3]) and new !=new2:
        return True, False
    elif not password_utils.verify_password(old, user[3]) and new !=new2:
        return False, False
    elif password_utils.verify_password(new, user[3]) and new == new2:
        passwordUpdate = db.change_user_password(username, new)
        if passwordUpdate:
            return True, True
        else:
            return False, False
    else:
        return False, False
        