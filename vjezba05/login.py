#!python
import base
import os
import cgi
import session
from http import cookies
import auth

params = cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    username = params.getvalue("username")
    password = params.getvalue("password")
    userCheck, user_ID = auth.authenticate(username, password)
    if userCheck and user_ID:
        session_id = session.create_session()
        dictionary = {"user_id": user_ID, "username": username}
        session.add_user_to_session(dictionary, session_id=session_id)
        cookies_object = cookies.SimpleCookie()
        cookies_object["username"] = username
        print (cookies_object.output())
        print("Location: index.py")


base.start_html()
print ('''
<form method="POST">
  <table>
    <tr>
      <th>Username</th>
      <td>
      <input type="text" name="username"  value="">
      </td>
    </tr>
    <tr>
        <th>Password</th>
        <td>
        <input type="password" name="password" value="" >
        </td>
      </tr>
      <tr>
        <td colspan="2"><input type="submit" value="Login" ></td>

      </tr>
  </table>
   <br>
  <a href="register.py"> Registracija </a> 
 ''')

if os.environ["REQUEST_METHOD"].upper() == "POST" and userCheck == False:
    print ("<p><b>ERROR:</b> Nepostojeci user</p>")
elif os.environ["REQUEST_METHOD"].upper() == "POST" and user_ID is None:
    print ("<p><b>ERROR:</b> Kriva lozinka</p>")

print('''</form>''')

base.end_html()