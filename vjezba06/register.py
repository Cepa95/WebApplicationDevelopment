#!python

import base
import cgi
import os
import db
import auth


params = cgi.FieldStorage()
if os.environ["REQUEST_METHOD"].upper() == "POST":
    
    username = params.getvalue("username")
    email = params.getvalue("email")
    password = params.getvalue("password")
    passwordCheck = params.getvalue("passwordCheck")
    userCheck, user_ID = auth.authenticate(username, password)
    #iako je unique, ali za provjeru postojanja emaila
    mail = db.get_email()
    # u slucaju da nema usera onda tek stvori novog
    if password==passwordCheck and userCheck is False and user_ID is None:
      if email not in mail:
        newUser = auth.register(username, password, email)
        if newUser:
          print('Location: login.py')

base.start_html()
print ('''<form method="POST">
<table>
  <tr>
    <td>username</td>
    <td><input type="text" name="username" placeholder="korisnicko ime"></td>
  </tr>
  <tr>
    <td>email</td>
    <td><input type="email" name="email" placeholder="example@gmail.com"></td>
  </tr>
  <tr>
    <td>password</td>
    <td><input type="password" name="password" placeholder="*************"></td>
  </tr>
  <tr>
    <td>PasswordCheck</td>
    <td><input type="password" name="passwordCheck" placeholder="*************"></td>
  </tr>
  <tr>
    <td colspan="2"><input type="submit" value="Register"></td>
  </tr>
</table>
<br>
<a href="login.py">Log In</a>''')

if userCheck is True:
    print ("<p><b>ERROR:</b> User pod tim imenom vec postoji</p>")
elif email in mail:
    print ("<p><b>ERROR:</b> Postoji korisnik pod tim mail-om</p>")
elif password != passwordCheck:
    print ("<p><b>ERROR:</b> Nisu unesene iste lozinke</p>")
('''</form>''')

base.end_html()