#!python

import cgitb #za formatiranje iznimki koje se dogode u cgi skriptama
cgitb.enable(display=0, logdir="")

print('''
<!DOCTYPE html>
<html lang="hrv">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lozinka</title>
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
    <form action="vjezba2.py" method="post">
        <table>
            <tr>
                <th>Ime:</th>
                <th><input type="text" name="firstname" value=""></th>
            </tr>
            <tr>
                <th>Lozinka:</th>
                <td><input type="password" name="password" value=""></td>
            </tr>
            <tr>
                <th>Ponovi lozinku:</th>
                <td><input type="password" name="password_repeat" value=""></td>
            </tr>
            <tr>
                <th><button type="submit" name="submit" value="Submit">Next</button></th>
                <td></td>
            </tr>
        </table>
    </form>
</body>

</html>
''')

