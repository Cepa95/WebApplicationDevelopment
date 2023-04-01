#!python.exe
import predmeti
 
def read_session_data(data):
    dictionary = {subject_id: 'not' for subject_id in predmeti.subjects} #sve postavlja na not
    for subject_id in dictionary: # u slucaju da je korisnik checka neke predmete, ili je izmjenia svoj prethodni check
        if subject_id in data:
            dictionary[subject_id] = data[subject_id]
    return dictionary

def print_subjects(key, dict):
    print('''
    <tr>
        <td>''' + predmeti.subjects[key]["name"] + '''</td> 
        <td>
    ''')#ispis predmeta
    for status_key, value in predmeti.status_names.items():  #provjera je li korisnik odabrao polje, defaultno je 'not'

        if dict[key] == status_key:
            print(value + '<input type="radio" name="' + key + '" value="' + status_key + '" checked/>') #checkiranje
        else:
            print(value + '<input type="radio" name="' + key + '" value="' + status_key + '" >')

    print('''
        </td>
    </tr>
    ''')

def print_subjects_button(paramsValue, dict):
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
                print_subjects(key, dict)
    elif paramsValue == "2. godina":
        for key in predmeti.subjects:
            if predmeti.subjects[key]["year"] == 2:
                #print("provjera2")
                print_subjects(key, dict)
    else:
        for key in predmeti.subjects:
            if predmeti.subjects[key]["year"] == 3:
                #print("provjera3")
                print_subjects(key, dict)


def print_list_button(dict):
    print('''
    <table border="1">
        <tr>
            <td>Subject</td>
            <td>Status</td>
            <td>Ects</td>
        </tr>
    ''')
    sum = 0
    for subject_id in predmeti.subjects:
        if dict[subject_id] == 'pass':
            sum += predmeti.subjects[subject_id]['ects']   
        print('''
                    <tr>
                        <td>''' + predmeti.subjects[subject_id]["name"] + '''</td>
                        <td>''' + predmeti.status_names[dict[subject_id]] + '''</td>
                        <td>''' + str(predmeti.subjects[subject_id]["ects"]) + '''</td> 
                    </tr>''')       
    print('''
    <tr>
        <td></td>
        <td>Total:</td>
        <td>''' + str(sum) + '''</td>
    </tr>''')
    print('</table>')