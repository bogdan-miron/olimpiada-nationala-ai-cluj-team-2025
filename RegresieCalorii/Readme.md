# Exemplu de problema (predicția numărului de calorii)

## Enunț
Implementați un model de AI/ML pentru a prezice consumul caloric al unei activități având la dispoziție un set de antrenare `dataset_train.csv` și două seturi de testare (pe care trebuie sa realizați doar predicția/inferența): `task1_dataset_eval.csv` și `task2_dataset_eval.csv`.

Setul de date conține următoarele câmpuri având semnificațiile:

- `User_ID`: ID-ul utilizatorului care a realizat activitatea
- `Gender`: genul utilizatorului
- `Age`: vârsta utilizatorului
- `Height`: înălțimea utilizatorului în cm
- `Weight`: greutatea utilizatorului în kg
- `Duration`: durata activității
- `Heart_Rate`: ritmul cardiac mediu pe parcursul activității
- `Body_Temp`: temperatura medie pe parcursul activității
- `Calories`: numărul de calorii consumate pe parcursul activității

## Note despre setul de date:

- Atributul-ținta este `Calories`. Date fiind celelalte atribute, scopul este de a prezice `Calories`. Setul de date de evaluare vizibil pentru candidați nu conține acest atribut, însă el este necesar platformei de evaluare. Metrica de evaluare folosită este MAE (media sumei diferențelor absolute dintre valoarea prezisă de către algoritm și valoarea corectă).
- Atributul `Gender`, având tipul string, trebuie transformat într-o dată de tip numeric pentru a putea fi folosit, mai simplu, în algoritmii de ML.
- Unele atribute pot fi inutile în predicția atributului-țintă. Încercați să analizați datele și să selectați doar atributele necesare sau pe cele care ar putea explica predicția realizată.

## Cerințe

**P1 (40p)**. Încărcați setul de date de antrenare și creați un fișier `output_0.csv` în care să aveți header-ul:

"Samples, No.Males, AverageDuration, SeniorUsers”

- `Samples`: numărul de linii de input din setul de date de antrenare, folosit în scop de verificare locală
- `No.Males`: numărul de exemple de antrenament care descriu activități realizate de către bărbați
- `AverageDuration`: durata medie a activitățiilor, aproximată la 2 zecimale
- `SeniorUsers`: numărul de utilizatori care au implinit 75 de ani. 

Fiecare din cele 4 componente valoreaza 10p.

**P2 (60p)** 

(a) (40p) Dezvoltați un model de AI/ML și efectuați predicția pentru atributul `Calories` pentru fiecare exemplu din fișierul `task1_dataset_eval.csv`. Valorile prezise se vor salva într-un fișier `output_1.csv` cu o singură coloană numită `Calories`.

(b) (20p) O echipă de handbal masculin are nevoie să estimeze consumul caloric pentru a optimiza dieta jucătorilor. Dezvoltați un model de AI/ML si realizați predicția numărului de calorii pentru fiecare exemplu din `task2_dataset_eval.csv`. Valorile prezise se vor salva într-un fișier `output_2.csv` cu o singură coloană numită `Calories`.

## Note despre problemă

Problema este relativ ușoară, fiind o variantă pentru clasele IX - X, dar prezintă și anumite aspecte mai dificile care pot departaja elevii. Setul de date are 9 coloane, dar unele dintre acestea au un scor de corelație ridicat. Astfel, pentru un model cât mai performant este necesară, mai întâi, selecția acestora. Structura setului poate afecta modelele mai adânci (ANN). De aceea selecția tipului de model trebuie realizată cu atenție. 

Sub-punctul (b) îi duce pe elevi în situația de a decide dacă să antrenze un model specializat pentru bărbați sau să se foloseasca de modelul antrenat la subpunctul anterior. La această problemă, din cauza numărului mic de exemple, varianta câștigătoare pare să fie utilizarea modelului de la punctul (a) (deci nu antrenarea unui nou model, folosind doar exemplele de antrenare corespunzătoare bărbaților). 

Cel mai probabil valorile MAE obținute (Candidat avansat) mai pot fi îmbunătățite, necesitând o revizie a punctajelor oferite de evaluator.
