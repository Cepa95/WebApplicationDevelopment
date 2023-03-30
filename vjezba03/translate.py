#!python.exe

from http import cookies
import predmeti
import os


def set_cookies(params):
    for key in predmeti.subjects:
        if params.getvalue(key): #u slucaju da smo mijenjali checkboxove ili vec postoji
            cookie = cookies.SimpleCookie()
            cookie[key] = params.getvalue(key)
            print(cookie.output()) #salje cookie klijentu

def get_cookies():
    cookie_string = os.environ.get('HTTP_COOKIE', '')       #dohvacanje cookie-ja u obliku stringa, trebamo ovu
    cookie_dict = cookies.SimpleCookie(cookie_string)       #funkciju da mozemo dohvatit cookie od klijenta ->HTTP_COOKIE
                                                            #dok, SimpleCookie nam omogucuje da izvadimo podatke na individualane
                                                            #cookie vrijednosti, daje nam to u obliku dictionaryja
    dict = {}
    for key in predmeti.subjects: 
        if cookie_dict.get(key):
            dict[key] = cookie_dict.get(key).value #moramo paziti da izvucemo samo vrijednost jer key sadrzi i atribute poput
        else:                                      #max-age, secure, expires....
            dict[key] = 'not' #dosta bitan uvjet za prvi put jer da ne postoji cookie u pocetku              
    return dict               #kada se pokrene xampp, u browseru bi doslo to poteskoca, primjerice ne bi se ispisala tablica zbog print_subjects
        
                         

def print_subjects(key, cookie, params):
    print('''
    <tr>
        <td>''' + predmeti.subjects[key]["name"] + '''</td> 
        <td>
    ''')#ispis predmeta

    if key in params:
        for status_key, value in predmeti.status_names.items():  #provjera je li korisnik odabrao polje, defaultno je 'not'

            if params.getvalue(key) == status_key: #params vamo sluzi da cookie ne kasni jedan korak
                print(value + '<input type="radio" name="' + key + '" value="' + status_key + '" checked/>') #checkiranje
            else:
                print(value + '<input type="radio" name="' + key + '" value="' + status_key + '" >')
   
    else:
        for status_key, value in predmeti.status_names.items():  #provjera je li korisnik odabrao polje, defaultno je 'not'

            if cookie[key] == status_key:
                print(value + '<input type="radio" name="' + key + '" value="' + status_key + '" checked/>') #checkiranje
            else:
                print(value + '<input type="radio" name="' + key + '" value="' + status_key + '" >')

    print('''
        </td>
    </tr>
    ''')



def print_subjects_button(paramsValue, cookie, params):
    print('''
    <table>
        <tr>
            <th>''' + paramsValue + '''</th>
        </tr>
        <tr>
            <th>Predmet</th>
            <th>Status</th>
        </tr>
    ''')

    ## Prosljedeni parametar paramsValue provjeravamo koji je string i obavljamo sve moguce radnje
    ## tako ako je paramsValue "1 godina uzimamo sve kljuceve koji imaju vrijednost godine 1, else
    ## je sam po sebi dovoljan vamo jer smo dovoljnu provjeru napravili u index.py
    if paramsValue == "1. godina":
        for key in predmeti.subjects:
            if predmeti.subjects[key]["year"] == 1:
                #print("provjera1")
                print_subjects(key, cookie, params)
    elif paramsValue == "2. godina":
        for key in predmeti.subjects:
            if predmeti.subjects[key]["year"] == 2:
                #print("provjera2")
                print_subjects(key, cookie, params)
    else:
        for key in predmeti.subjects:
            if predmeti.subjects[key]["year"] == 3:
                #print("provjera3")
                print_subjects(key, cookie, params)



def print_list_button(cookie, params):
    print('''
    <table>
        <tr>
            <th>Predmet</th>
            <th>Status</th>
            <th>Ects</th>
        </tr>
    ''')
  
    sum = 0
    for subject_id in predmeti.subjects:
        if subject_id in params:
            if params.getvalue(subject_id) == 'pass':
                sum += predmeti.subjects[subject_id]["ects"]
            ## da se izbjegne TypeError mora se u Pythonu castati int u str, ne dopusta povezivanje
            ## stringova i non stringova
            print('''
            <tr>
                <td>''' + predmeti.subjects[subject_id]['name'] + '''</td>
                <td>''' + predmeti.status_names[params.getvalue(subject_id)] + '''</td>
                <td>''' + str(predmeti.subjects[subject_id]['ects']) + '''</td>
            </tr>''') 

        elif subject_id in cookie:
            if cookie[subject_id] == 'pass':
                sum += predmeti.subjects[subject_id]["ects"]
               
            print('''
                    <tr>
                        <td>''' + predmeti.subjects[subject_id]["name"] + '''</td>
                        <td>''' + predmeti.status_names[cookie[subject_id]] + '''</td>
                        <td>''' + str(predmeti.subjects[subject_id]["ects"]) + '''</td> 
                    </tr>''')      
    print('''
    <tr>
        <td></td>
        <td>Total:</td>
        <td>''' + str(sum) + '''</td>
    </tr>''')
    print('</table>')