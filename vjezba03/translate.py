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
        
                         
def check(key, cookie, status_key): #provjera je li korisnik odabrao polje
   
    if cookie[key] == status_key:
        return ' checked/>'
    return ' />'

def print_subjects(key, cookie):
    print('''
    <tr>
        <td>''' + predmeti.subjects[key]["name"] + '''</td> 
        <td>
    ''')#ispis predmeta
   
    for status_key, value in predmeti.status_names.items():
        print(value + '<input type="radio" name="' + key + '" value="' + status_key + '"' + check(key, cookie, status_key)) #checkiranje
    print('''
        </td>
    </tr>
    ''')

def print_subjects_button(paramsValue, cookie):
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
                print_subjects(key, cookie)
    elif paramsValue == "2. godina":
        for key in predmeti.subjects:
            if predmeti.subjects[key]["year"] == 2:
                #print("provjera2")
                print_subjects(key, cookie)
    else:
        for key in predmeti.subjects:
            if predmeti.subjects[key]["year"] == 3:
                #print("provjera3")
                print_subjects(key, cookie)


def print_list_button(cookie):
    print('''
    <table>
        <tr>
            <th>Predmet</th>
            <th>Status</th>
            <th>Ects</th>
        </tr>
    ''')
    #kasni za jedan klik, dok to server ne rijesi
    sum = 0
    counter = 1
    #stavit cemo counter zbog finese, da ispise prvo prvi semestar, pa drugi, pa treci
    while counter !=4:
        for key in cookie:
            if key in cookie:
                if cookie[key] == "pass" and predmeti.subjects[key]["year"] == counter: #da mi ne ponovi isto vise puta trebam ovi drugi uvjet
                    sum += predmeti.subjects[key]["ects"]
                ## da se izbjegne TypeError mora se u Pythonu castati int u str, ne dopusta povezivanje
                ## stringova i non stringova
                if predmeti.subjects[key]["year"] == counter:

                    print('''
                    <tr>
                        <td>''' + predmeti.subjects[key]["name"] + '''</td>
                        <td>''' + predmeti.status_names[cookie[key]] + '''</td>
                        <td>''' + str(predmeti.subjects[key]["ects"]) + '''</td> 
                    </tr>''')   
        counter+=1
            
    print('''
    <tr>
        <td></td>
        <td>Total:</td>
        <td>''' + str(sum) + '''</td>
    </tr>''')
    print('</table>')