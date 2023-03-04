#!python

import cgi
import cgitb
cgitb.enable(display=0, logdir="")
params = cgi.FieldStorage()

def textarea_check():
  note =params.getvalue("tekstarea") 
  if (not note): #provjera jeli ista upisano u textarea
    note = "nema napomene"
  return note

def print_html4(note):
  print('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Podaci</title>
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
      .th {
        text-align: center;
      }
    </style>
  </head>
  <body>
  <table>
    <tr>
      <th colspan="2" class="th">Uneseni podaci</th>
    </tr>
    <tr>
      <th>Ime:</th>
      ''') 
  print('<td>', params.getvalue("firstname"), '</td>') 
  print('''
    </tr>
    <tr>
      <th>E-mail:</th>''')
  print('<td>', params.getvalue("email"), '</td>') 
  print('''</tr>
    <tr>
      <th>Status:</th>''')
  print('<td>', params.getvalue("just_one"), '</td>') 
  print('''</tr>
    <tr>
      <th>Smjer:</th>''')
  print('<td>', params.getvalue("courses"), '</td>') 
  print('''</tr>
    <tr>
      <th>Zavrsni rad:</th>''')
  print('<td>', params.getvalue("check"), '</td>') 
  print('''<tr>
      <th>Napomene:</th>''')
  print('<td>', note, '</td>') 
  print('''</tr>
  </table>
  <a href="vjezba1.py">Na pocetak</a>
 </body>
</html>
''')
  
note = textarea_check()
print('') # mora biti ovdi '' prije print_html4 ili ce mi bacati server error, a baca mi error jer
print_html4(note)             # za razliku od prijasnih vjezbi nisam <!DOCTYPE html> odvojio od ''' <== PRIMJER GRESKE KOJA MOZE DOCI
                             

# print (params.getvalue("email"))
# print(note)