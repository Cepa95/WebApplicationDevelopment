#!python

import cgi
import cgitb
cgitb.enable(display=0, logdir="")
params = cgi.FieldStorage()

def checkbox_check():
    checkbox=params.getvalue("check") 
    if (not checkbox): #provjera jel checkbox odabran
        checkbox = "Ne"
    return checkbox

# radio = params.getvalue("just_one")
# if (radio !="Redovan" or radio != "Izvanredan"):
#     print("Location: vjezba2.py")

# email = params.getvalue("email")
# if (not email):
#     print("Location: vjezba2.py")
# if ("@" not in email):
#     print("Location: vjezba2.py")
# divide=email.split("@")
# if (len(divide) !=2):
#     print("Location: vjezba2.py")
# if (divide[1] !="unist.hr" or divide[1]!="oss.unist.hr"):
#     print("Location: vjezba2.py")
# if (not divide[0].islower()):
#     print("Location: vjezba2.py")

def print_html3(checkbox):
    print('''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tablica</title>
    <style>
        table,
        tr,
        th,
        td {
            border: 1px black solid;
        }

        th {
            text-align: left;
        }
    </style>
</head>

<body>
    <form action="vjezba4.py" method="post">
        <table>
            <tr>

                <th> Napomene:</th>
                <td><textarea rows="5" cols="19" placeholder="Prelazak na izvanredni studij...." name="tekstarea" value=""></textarea></td>
            </tr>
           ''')
    print('<input type="hidden" name="firstname" value="' + params.getvalue("firstname") + '">')
    print('<input type="hidden" name="password" value="' + params.getvalue("password") + '">')
    print('<input type="hidden" name="just_one" value="' + params.getvalue("just_one") + '">')
    print('<input type="hidden" name="email" value="' + params.getvalue("email") + '">')
    print('<input type="hidden" name="courses" value="' + params.getvalue("courses") + '">')
    print('<input type="hidden" name="check" value="' + checkbox + '">')
    print('''<tr>
                <th><button type="submit" value="Submit">Next</button></th>
                <td></td>
            </tr>

        </table>
    </form>
</body>
''')


checkbox=checkbox_check()
print_html3(checkbox)

#print ('')
# print (params.getvalue("firstname")) #ovaj firstname, tako i password =>name sad se odnose na vjezbu2.py i njihove input tipove
# print ('')
# print (params.getvalue("password")) #ispis cgi vrijednosti
# print (checkbox) #ispis varijable
# #print(email)
