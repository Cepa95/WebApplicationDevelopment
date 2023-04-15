# Vježba 5 – autentikacija
Izmijeniti vjezbu 4 na slijedeci nacin:  
Potrebno je dodati stranice za registraciju, prijavu, odjavu i promjenu lozinke.   
•	Registracijska forma
o	sadrži: ime, e-mail, lozinku, ponovljenu lozinku  
o	potrebno je provjeriti da ime ili e-mail nisu zauzeti i da su lozinke jednake te korisnika   
o	u slucaju greske vratiti korisnika na istu stranicu sa opisom greske.  
o	U slucaju uspjeha prosljediti korisnika na stranicu za prijavu (login)  
•	Prijavljivanje  
o	Standardna login forma sa imenom i lozinkom  
o	U slucaju greske u autentikaciji, vratiti korisnika na stranicu sa porukom o greski.  
o	U slucaju uspjesne autentikacije, prosljediti korsnika na pocetnu stranicu.  
•	Odjava  
o	Unistiti sesiju (izbrisati sesiju iz baze i ukloniti cookie session_id iz preglednika) i preusmjeriti korsnika na stranicu za prijavu.  
•	Promjena lozinke  
o	Za promjenu lozinke je potrebno ponoviti staru lozinku i upisati dva puta novu lozinku (kao pri registraciji)  
o	U slucaju greske vratiti korisnika na istu stranicu sa porukom o greski.  
Koristiti gdje je prikladno password_hash() i password_verify(). Prilikom zahtijevanja pocetne stranice, neprijavljene korisnike preusmjeravati na stranicu za prijavu. Podatke o korisniku cuvati u bazi podataka u tablici users. Tablica ce imati cetiri stupca: id (primarni kljuc), ime (varchar 100),  email (varchar 100 i postaviti ga na razini baze na unique) te password (binary 64, jer ce sadrzavati hash).  Prilikom potvrde identiteta (uspjesne autentikacije) kreirati sesiju u koju ce se spremiti id autenticiranog korisnika. Na vrhu stranice dodati pozdravnu poruku „Hej [ime korisnika]!”. Razdvojite kod na sljedece funkcije i pomocne funkcije:  
register()  
login()  
create_user()  
get_user()  
Rjecnik subjects iz datoteke subjects.py zamijeniti tablicom „subjects” u bazi podataka. Tablica ce imati sljedece stupce: id (int, AI, primarni kljuc), kod (varchar), ime (varchar 100), bodovi (int), godina (int). Rucno popuniti tablicu podacima iz rjecnika. Listu predmeta na stranici dohvatiti iz baze podataka.
 


