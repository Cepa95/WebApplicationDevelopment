#!python.exe

import cgi
import base
import os
import translate
import session
import predmeti


params = cgi.FieldStorage()


if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)

data = session.get_session_data()
dict = translate.read_session_data(data)

base.start_html()

for key in predmeti.year_ids:
        print('<input type="submit" name="button" value="' + key + '"/>') #petlja za kreiranje botuna za godine
print('<input type="submit" name="button" value="Upisni list"/>') 


if params.getvalue("button") == "1. godina" or params.getvalue("button") == "2. godina" or params.getvalue("button") == "3. godina":
    #print("provjera")
    translate.print_subjects_button(params.getvalue('button'), dict)
elif params.getvalue("button") == "Upisni list":
    translate.print_list_button(dict)

base.end_html()