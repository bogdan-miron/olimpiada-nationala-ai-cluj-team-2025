# Identificarea figurilor geometrice în imagini - enunt vechi, README pentru enunt nou

## Enunț
Dezvoltati un algoritm inteligent care să identifice și să localizeze automat diferite figuri geometrice în imagini. 
Aveți la dispoziție 2 seturi de imagini 2D color (imagini RGB) care conțin diferite figuri geometrice. Setul 1 se regăsește în folderul "dataset1", iar setul 2 în folderul "dataset2". 

## Note despre setul de date:

Fiecare set conține $n$, respectiv $m$ imagini cu figuri geometrice de forma unui pătrat, dreptunghi, cerc, oval sau triunghi. O imagine poate conține una sau mai multe figuri geometrice. Figurile geometrice pot avea diferite dimensiuni, culori și poziții în cadrul imaginii.
Figurile geometrice sunt caracterizate astfel:
- pătrat: coordonatele (x,y) ale colțutui din stânga sus și lungimea laturii (în nr de pixeli) - (x, y, w)
- dreptunghi: coordonatele (x,y) ale colțutui din stânga sus, lungimea și lățimea (în nr de pixeli) - (x, y, w, h)
- cerc: coordonatele (x,y) ale centrului și raza (în nr de pixeli) - (x, y, r)
- oval: coordonatele (x,y) ale centrului, raza mare și raza mică (în nr de pixeli) - (x, y, r1, r2)
- triunghi: coordonatele (x,y) ale vârfurilor (x1, y1, x2, y2, x3, y3)

Toate figurile au dimensiunea de 256 x 256 pixeli, pixelul din colțul stânga jos al imaginii are coordonatele (0,0), iar colțul dreapta sus al imaginii are coordonatele (255, 255).

## Cerinte

Dezvoltați un algoritm inteligent care să identifice și să localizeze automat diferite figuri geometrice în imagini. Algoritmul trebuie să identifice tipul fiecărei figuri geometrice și să localizeze coordonatele acesteia în cadrul imaginii.

**P1 (40p)**. Pentru setul de date din folderul "dataset1" creați:
- un fișier "output_1.csv" în care să salvați, pe câte o linie, următoarele informații: 
    - linia 1: numărul de imagini din cadrul folderului (valoare lui $n$)
    - linia 2: numărul de figuri geometrice din fiecare imagine, separate prin spațiu
    - linia 3: numărul de figuri geometrice de fiecare tip (pătrat, dreptunghi, cerc, oval, triunghi) din cadrul setului de date sub forma unui vector de perechi de tipul (tipFigură, nrFiguri), separate prin spațiu
- un folder numit ”dataset1_masks” în care să salvați imagini binare (alb-negru) pentru fiecare imagine din setul de date. Imaginile binare sunt mastile imaginilor originale in care pixelii corespunzatori figurilor geometrice au valoarea 1, iar pixelii corespunzatori backgroundului au valoarea 0.

**P2 (60p)** 
Pentru setul de date din folderul "dataset2" creați:
- un fișier "output_2.csv" în care să salvați, pe câte o linie, următoarele informații: 
    - linia 1: numărul de imagini din cadrul folderului (valoare lui $m$)
    - linia 2: numărul de figuri geometrice din fiecare imagine, separate prin spațiu
    - linia 3: numărul de figuri geometrice de fiecare tip (pătrat, dreptunghi, cerc, oval, triunghi) din cadrul setului de date sub forma unui vector de perechi de tipul (tipFigură, nrFiguri), separate prin spațiu
- un folder numit ”dataset2_masks” în care să salvați imagini binare (alb-negru) pentru fiecare imagine din setul de date. Imaginile binare sunt mastile imaginilor originale in care pixelii corespunzatori figurilor geometrice au valoarea 1, iar pixelii corespunzatori backgroundului au valoarea 0.
