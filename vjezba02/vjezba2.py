#!python
import cgi
import cgitb
cgitb.enable(display=0, logdir="")

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
<html lang="hr">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Drop down</title>
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
    <form action="vjezba3.py" method="post">
        <table>
            <tr>
                <th>Status:</th>
                <td>Redovan:<input type="radio" name="just_one" value="Redovan">
                    Izvanredan:<input type="radio" name="just_one" value="Izvanredan">
                </td>
            </tr>
            <tr>
                <th>E-mail</th>
                <td><input type="email" name="email" size ="23"></td>
            </tr>
            <tr>
                <th>Smjer:</th>
                <td>
                    <select name="courses">
                        <option value="Uvod u programiranje">Uvod u programiranje</option>
                        <option value="Osnove izrade web stranica">Osnove izrade web stranica</option>
                        <option selected value="Baze podataka">Baze podataka</option>
                        <option value="Objektno programiranje">Objektno programiranje</option>
                        <option value="Strukture podataka">Strukture podataka</option>
                    </select>
                </td>
            <tr>
                <th>Zavrsni:</th>
                <td><input type="checkbox" name="check" value="Da"></td>
            </tr>
            </tr>''')
print ('<input type="hidden" name="firstname" value="' + params.getvalue("firstname") + '">')
print('<input type="hidden" name="password" value="' + params.getvalue("password") + '">')
print('''<tr>
                <th><button type="submit" value="Submit">Next</button></th>
                <td></td>
            </tr>

        </table>
    </form>
</body>
''')

# print ('<br>')
# print (params.getvalue("firstname"))
# print ('<br>')
# print (params.getvalue("password")) #ispis cgi vrijednosti

