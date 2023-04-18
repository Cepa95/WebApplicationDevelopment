#! python.exe
import base
import cgi
import translate
import session
import os
import db
import predmeti
from http import cookies

params = cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)

http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)

#vrati na login.py ako ne postoji user
if not get_all_cookies_object.get("username"):
    print("Location: login.py")
else:
    data = session.get_session_data()
    for key, value in data.items():
        # kljucu username dodaj vrijednost imena
        if key == "username":
            name=value

subjects = db.get_subjects()


base.start_html()
print('<form action ="" method="post">')
print('<b> Hej', name ,'!</b><br><br>')
for key in predmeti.year_ids:
        print('<input type="submit" name="button" value="' + key + '"/>') #petlja za kreiranje botuna za godine
print('<input type="submit" name="button" value="Upisni list"/>') 


if params.getvalue("button") == "1. godina" or params.getvalue("button") == "2. godina" or params.getvalue("button") == "3. godina":
    #print("provjera")
    translate.print_subjects_button(params.getvalue('button'), subjects, data)
elif params.getvalue("button") == "Upisni list":
    translate.print_list_button(subjects, data)

print('<br><input type="submit" name="submit" value="Submit"><br><br>')
print('''
<a href=change.py> Promjena lozinke </a><br><br>
<a href=logout.py> Log Out </a>
''')
print('</form>')
base.end_html()