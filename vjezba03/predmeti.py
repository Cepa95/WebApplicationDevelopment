#!python.exe

subjects = {
    'uup' : { 'name' : 'Uvod u programiranje', 'year' : 1, 'ects' : 7 },
    'oiws' : { 'name' : 'Osnove izrade web stranica' , 'year' : 1, 'ects' : 6 },
    'ds' : { 'name' : 'Digitalni sustavi', 'year' : 1, 'ects' : 6 },
    'fur' : { 'name' : 'Fizika u racunarstvu', 'year' : 1, 'ects' : 5 },
    'la' : { 'name' : 'Linearna algebra', 'year' : 1, 'ects' : 6 },

    'os' : { 'name' : 'Operativni sustavi' , 'year' : 2, 'ects' : 5 },
    'bp' : { 'name' : 'Baze podataka', 'year' : 2, 'ects' : 6 },
    'spa' : { 'name' : 'Strukture podataka i algoritmi', 'year' : 2, 'ects' : 6 },
    'pinm' : { 'name' : 'Primijenjena i numericka matematika' , 'year' : 2, 'ects' : 6 },
    'oop' : { 'name' : 'Objektno programiranje' , 'year' : 2, 'ects' : 7 },


    'puc' : { 'name' : 'Programiranje u C#', 'year' : 3, 'ects' : 6 },
    'puj' : { 'name' : 'Programiranje u Javi' , 'year' : 3, 'ects' : 6 },
    'mu' : { 'name' : 'Mrezne usluge', 'year' : 3, 'ects' : 6 },
    'zr' : { 'name' : 'Zavrsni rad', 'year' : 3, 'ects' : 8 },
    'pr' : { 'name' : 'Prakticni rad', 'year' : 3, 'ects' : 12 }
    }
        
year_names = {
        1 : '1. godina',
        2 : '2. godina',
        3 : '3. godina'
    }

year_ids = {
        '1. godina' : 1,
        '2. godina' : 2,
        '3. godina' : 3
}

status_names = {
    'not' : 'Ne upisuje',
    'enr' : 'Upisuje',
    'pass' : 'Položen'
}