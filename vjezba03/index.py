#!python.exe

import cgi
import base
import translate
import predmeti


params = cgi.FieldStorage()

translate.set_cookies(params) #ne smije u body ici, inace vraca na defaulte vrijednosti
cookie = translate.get_cookies()


base.start_html()

for key in predmeti.year_ids:
        print('<input type="submit" name="button" value="' + key + '"/> <br>') #petlja za kreiranje botuna za godine
print('<input type="submit" name="button" value="Upisni list"/>') 


if params.getvalue("button") == "1. godina" or params.getvalue("button") == "2. godina" or params.getvalue("button") == "3. godina":
    print("provjera")
    translate.print_subjects_button(params.getvalue('button'), cookie)
elif params.getvalue("button") == "Upisni list":
    translate.print_list_button(cookie)


 
