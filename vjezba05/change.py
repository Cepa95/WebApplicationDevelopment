#!python
import base
import os
import cgi
from http import cookies
import auth
import db
import session

params = cgi.FieldStorage()


http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
username = get_all_cookies_object.get("username").value

user = db.get_user(username)

if os.environ["REQUEST_METHOD"].upper() == "POST":
    password = params.getvalue("password")
    newPassword = params.getvalue("newPassword")
    newPassword2 = params.getvalue("newPassword2")
    passwordCheck, newPasswordUpdate = auth.change_password(str(username), password, newPassword, newPassword2)
    if passwordCheck and newPasswordUpdate:
        session.destroy_session()
        print('Location: login.py')


base.start_html()
print('''
<form method="POST">
<table>
  <tr>
    <td>
        <h1>Change Password</h1>
        <p> Username:''', str(username), '''</p>
        <input type="password" name="password" placeholder="Stara lozinka"><br><br>
        <input type="password" name="newPassword" placeholder="Nova lozinka"><br><br>
        <input type="password" name="newPassword2" placeholder="Ponovi novu lozinku"><br><br>
        <input type="submit" value="Promijeni">
    </td>
  </tr>
</table>
</form>
''')
if (os.environ["REQUEST_METHOD"].upper() == "POST" and not passwordCheck):
    print ("<p><b>ERROR:</b> Krivo unesena stara lozinka</p>")
elif (os.environ["REQUEST_METHOD"].upper() == "POST" and not newPasswordUpdate):
    print ("<p><b>ERROR:</b> Nisu unesene iste lozinke</p>")
base.end_html()