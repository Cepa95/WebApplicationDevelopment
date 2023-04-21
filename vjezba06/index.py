#!python

import base
import cgi
import translate
import session
import os
import db
import predmeti
from http import cookies

http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)

params = cgi.FieldStorage()

if not get_all_cookies_object.get("session_id"):
    print("Location: login.py")
if not get_all_cookies_object.get("username"):
    print("Location: login.py")
else:
    data = session.get_session_data()
    for key, value in data.items():
        if key=='user_id':
            student_id=value
            dataList = db.get_upisni_list(student_id)
        if key=='username':
            name=value
            
subjects = db.get_subjects()

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    for predmet in params.keys():
        if predmet.isnumeric():
            predmet_id=predmet
            status=params.getvalue(predmet)
            db.add_upisni_list(student_id,predmet_id,status)


base.start_html()
print('<form action ="" method="post">')
print('<b> Hej', name ,'!</b><br><br>')
for key in predmeti.year_ids:
        print('<input type="submit" name="button" value="' + key + '"/>') #petlja za kreiranje botuna za godine
print('<input type="submit" name="button" value="Upisni list"/>') 


if params.getvalue("button") == "1. godina" or params.getvalue("button") == "2. godina" or params.getvalue("button") == "3. godina":
    #print("provjera")
    translate.print_subjects_button(params.getvalue('button'), subjects, dataList)
elif params.getvalue("button") == "Upisni list":
    translate.print_list_button(subjects, dataList)

print('<br><input type="submit" name="submit" value="Submit"><br><br>')

print('''
<table>
  <tr>
    <td><a href="popis.py">Popis studenata</a></td>
  </tr>
  <tr>
    <td><a href="change.py">Promjena lozinke</a></td>
  </tr>
  <tr>
    <td><a href="logout.py">Log out</a></td>
  </tr>
</table>
''')
print('</form>')
base.end_html()