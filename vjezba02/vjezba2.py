#!python
import cgi
import os

params = cgi.FieldStorage()
first_name = params.getvalue("firstname")
password = params.getvalue("password")
password_repeat = params.getvalue("password_repeat")

if ((password != password_repeat) or not password or not first_name):
    print("Location: vjezba1.py") #http header koji vraca na prethodnu stranicu 
                                 #ako lozinke nisu istovjetne ili su prazne ili 
                                 # ako korisnik upisao bar jedan znak za svoje ime



print ('''
<!DOCTYPE html>
<html>
<body>

<h2>Odaberite smjer:</h2>

<form action="vjezba3.py" method="post">
  <select name="smjer_studija">
    <option value="programiranje">programiranje</option>
    <option value="baze_podataka">baze podataka</option>
    <option value="mreze">mreze</option>
    <option value="informacijski_sustavi">informacijski sustavi</option>
  </select>
  <br><br>''')
print ('<input type="hidden" name="ime" value="' + params.getvalue("firstname") + '">')
print ('''
<br>
<input type="submit" value="submit">
</form>

</body>
</html>''')
print("Ovako se zovu post parametri iz skripte koja se submit-ala na test3.py: ")
print (params.getvalue("firstname"))
print ('<br>')
print("Parametri pod ovim imenom ne postoje: ")
print (params.getvalue("ime"))
