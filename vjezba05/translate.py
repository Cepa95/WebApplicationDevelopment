#!python

import predmeti

def print_subjects(row, data):
    print('''
    <tr>
        <td>''' + row[2] + '''</td> 
        <td>
    ''')#ispis predmeta
    #ako predmet ne postoji setiraj vrijednost na not
    if (data.get(row[1])==None):
        print('<input type="radio" name="' + row[1] + '" value=''not'' checked>' + predmeti.status_names.get('not'))
        print('<input type="radio" name="' + row[1] + '" value=''enr''>' + predmeti.status_names.get('enr'))
        print('<input type="radio" name="' + row[1] + '" value=''pass''>' + predmeti.status_names.get('pass'))
    else:
         for status_key, value in predmeti.status_names.items():  #provjera je li korisnik odabrao polje, defaultno je 'not'

                if data[row[1]] == status_key:
                        print(value + '<input type="radio" name="' + row[1] + '" value="' + status_key + '" checked/>') #checkiranje
                else:
                        print(value + '<input type="radio" name="' + row[1] + '" value="' + status_key + '" >')
    print('''
        </td>
    </tr>
    ''')

def print_subjects_button (godina, subjects, data):
    print('''
    <table>
        <tr>
            <th>''' + godina + '''</th>
        </tr>
        <tr>
            <th>Predmet</th>
            <th>Status</th>
        </tr>
    ''')
    for row in subjects:
        if(row[4]==predmeti.year_ids[godina]):
            print_subjects(row,data)
            print('</td></tr>')
    print('</table>')


def print_list_button(subjects,data):
    print('''
     <table border="1">
        <tr>
            <th>Subject</th>
            <th>Status</th>
            <th>Ects</th>
        </tr>
    ''')
    sum = 0
    for row in subjects:
        if (data[row[1]] == "pass"):
            sum+=row[3]
        print('''
                    <tr>
                        <td>''' + row[2] + '''</td>
                        <td>''' + predmeti.status_names.get(data[row[1]]) + '''</td>
                        <td>''' + str(row[3]) + '''</td> 
                    </tr>''')       
    print('''
    <tr>
        <td></td>
        <td>Total:</td>
        <td>''' + str(sum) + '''</td>
    </tr>''')
    print('</table>')

    


       



































def printPaperDb(subjects,data):
    suma = 0
    print('<table>')
    print('<tr><td>Predmet</td><td>Status</td><td>Bodovi</td></tr>')
    for row in subjects:
        if (data[row[1]] == "enr"):
            suma+=row[3]
        print('<tr><td>')
        print(row[2])
        print('</td><td>')
        print(predmeti.status_names.get(data[row[1]]))
        print('</td><td>')
        print(row[3])
        print('</td></tr>')
    print('<tr><td></td><td>Ukupno bodova:</td><td>' + str(suma) + '</td></tr>') 
    print('</table>')
