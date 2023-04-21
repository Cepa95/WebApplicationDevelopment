# Vježba 6 – autorizacija  
Izmijeniti vjezbu 5 na slijedeci nacin:  
U sesiji cuvati samo id korisnika. Status studenta na predmetu spremati u medju-tablicu upisni_list. Tablica ce imati sljedece stupce: id (primarni kljuc), id_studenta (strani kljuc), id_predmeta (strani kljuc) i status (tip podatka enum, a njegove vrijednosti 'pass' i 'enr').  Iz tablice upisni list dobiti informacije o upisnom listu i o tome koji radio botun treba biti oznacen.   

Tablicu „users” prosiriti sa jos jednim stupcem „uloga” (tip podatka enum, a njegove vrijednosti 'student' i 'admin'). Dodati jos jednu skriptu (popis_studenata) sa ispisom imena svih korisnika u tablici „users” koji imaju ulogu „student”. Toj stranici mogu pristupiti samo korisnici koji imaju ulogu administratora. Ukoliko korisnik sa ulogom student zeli pristupiti stranici, ispise mu se poruka „nemate pravo pristupa”.  

Klikom na svakog pojedinog studenta (anchor), otvara se nova stranica sa iscrtanim upisnim listom. Atribut href treba sadrzavati id studenta, na osnovu kojega ce se dohvatiti podaci o studentovom upisnom listu. Napomena-id studenta je get parametar i dohvaca ga se na isti nacin kao i post parametre.


