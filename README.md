# 📡 HotSpot 📡

## Enunț

În anul 2147, omenirea a renunțat la fire. Totul e wireless. În orașele-ruină ale unei societăți distopice, semnalul WiFi este sursa principală de energie, comunicare și control. Din cauza suprasaturării cu rețele și emițătoare, undele radio sunt instabile, interferențele sunt la ordinea zilei, iar zonele cu semnal clar – așa-numitele `HotSpots` – sunt rare și extrem de valoroase.

O agenție secretă, `Umbrella Corporation`, a dezvoltat un sistem de analiză vizuală pentru a cartografia aceste HotSpots folosind imagini satelitare modificate. Aceste imagini prezintă diferite forme geometrice (cercuri, elipse, dreptunghiuri și poligoane) care reprezintă  așa zisele HotSpots. Însă, acest sistem nu este perfect, iar imaginea este afectată de `zgomot de fundal aleatoriu` și `benzi (stripes) semi-transparente` care simulează  interferențele radio.

**Misiunea ta este vitală**: la fel ca  în vechile operațiuni din `Orașul Ratonilor`, ai fost activat pentru a identifica acele rare zone cu semnal curat - **HotSpots**. Semnalul e viață. Restul e interferență.

## Date de intrare


Arhiva `Satellite_Images-1` conține X imagini, care au dimensiunea de 256x256, conținând 3 canale - RGB, numerotate `image_00000.png`, până  la `image_X.png` . 

Arhiva `Satellite_Images-2` conține Y imagini, care au dimensiunea de 256x256, conținând 3 canale - RGB, numerotate `image_00000.png`, până  la `image_Y.png` .

Imaginile reprezintă  harta semnalelor din diferite puncte strategice ale țării.


## Cerințe


**Partea 1 (20p)** - Utilizând imaginile din arhiva `Satellite_Images-1`, determinați HotSpots pentru fiecare imagine din acea arhivă. 

**Partea 2 (80p)** - Utilizând imaginile din arhiva `Satellite_Images-2`, determinați HotSpots pentru fiecare imagine din acea arhivă.

## Formatul de ieșire

Formatul de ieșire  constă  într-un fișier `output.csv`, care să  includă  următoarele 3 coloane:
- `subtaskID` - reprezintă numărul subtaskului (1 sau 2)
- `datapointID` - care se referă  la denumirea fiecărei imagini din arhiva `Satellite_Images-subtaskID`.
- `answer` - care reprezintă **masca  binară a HotSpots-urilor** din imaginea respectivă, unde valoarea `1` este asociată unui pixel care aparține unui HotSpot, iar valoarea `0` este asociată celorlalte zone. Codificarea măștii  va fi făcută  utilizând  tehnica **Run-Length Encoding** (vezi mai jos) .

RLE este o metodă de **compresie** pentru măști binare. În loc să trimiteți toți pixelii (0 sau 1), trimiteți doar **pozițiile** unde încep secvențele de 1 și **lungimile** lor.

**Reguli pentru codificare**:
1.  Masca se parcurge **coloană cu coloană** (ordinea Fortran/column-major).
    
2.   Se indexează de la **1** (nu de la 0).
    
2.  Se codifică sub forma:  
    `start_1 length_1 start_2 length_2 ...`

**Exemplu**:
Fiecare element este un pixel (`1` = aparține obiectului, `0` = fundal). Avem o masca binară 2D:
```
0 0 1 0
0 1 1 0
0 0 1 0
0 0 1 0
0 0 0 0
```
În format coloană (flattened column-major):  
`[0, 0, 0, 0, 0,   0, 1, 0, 0, 0,   1, 1, 1, 1, 0,   0, 0, 0, 0, 0]`

**Codificare RLE**
- `7 1` -> secvența de `1` începe de la index 7, având lungimea 1.
- `11 4` -> secvența de `1` începe de la index 11, având lungimea 4.

**RLE Final**:

`7 1 11 4`


## Evaluare

Evaluarea se va face folosind **F1-score la nivel de pixel**, comparând masca prezisă cu masca reală. Decodificarea se face automat din RLE în mască binară pentru fiecare imagine.

Trimiteți un singur csv care să conțină răspunsurile pentru toate subtask-urile pe care le-ați rezolvat. Pentru a vedea un exemplu, descărcați fișierul `sample_output.csv`.

## Exemple de Ground Truth

În  următoarele imagini vor fi prezentate (în  stânga) un exemplu de imagini din arhivă, iar în  dreapta  va fi prezentat Ground-Truthul asociat imaginii. Acest exemplu are rolul de a ajuta concurentul de a face diferență  între ce se consideră `zgomot de fundal (random noise)`, `artefacte din imagine (image artefacts)`, `benzi semi-transparente`, și ce se consideră a fi `HotSpot`. Notă: `HotSpots` pot să fie doar de tip cerc, elipsă, dreptungi și polygon (convex sau concav).
