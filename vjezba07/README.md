                                                  Vježba 7  
Izraditi Django aplikaciju za prodaju kino karata. Putem admin sucelja napraviti registraciju korisnika i 
iskoristiti gotovu tablicu user koja dolazi sa Django-vim paketom auth. Izraditi modele Projekcija (ime 
filma, vrijeme filma i kapacitet dvorane-broj sjedala) i Karta (broj sjedala) i postaviti ih u odgovarajuće 
relacije (Karta ima dvije relacije-na korisnika i na projekciju).  

Izraditi stranice (template-e) na kojima se moze vidjeti:  
- sve projekcije (ime filma + vrijeme + koliko je slobodnih mjesta za projekciju ostalo)  
- karte za projekcije (ime filma + vrijeme + korisnikovo sjedalo) za korisnika ciji je id unesen putem url-a  

Odredjivanje sjedala prilikom kupovine karte ce se realizirati na slejdeci nacin. Svakom kupovinom   
provjerava se ima li projekcija dovoljno kapaciteta te ako ima daje se sljedeci broj karte. Napomena: ukoliko se karte brisu doci ce do dupliciranja broja karte, no ukupan broj karata nece preci kapacitet 
projekcije.  
