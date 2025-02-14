# Exemplu de problema (predictia preturilor jocurilor de pe platforma Steam)

## Enunt
Implementati un model de AI pentru a prezice cosumul caloric a unei activitati avand la dispozitie un set de antrenare `dataset_train.csv` si doua pe care trebuie sa faceti doar predictia: `task1_dataset_eval.csv`. si `task2_dataset_eval.csv`

Setul de date contine urmatoarele campuri avand semnificatiile:

- `User_ID`: ID-ul utilizatorului care a facut activitatea
- `Gender`: genul utilizatorului
- `Age`: varsta utilizatorului
- `Height`: inaltimea utilizatorului in cm
- `Weight`: greutate utilizatorului in kg
- `Duration`: durata activitatii
- `Heart_Rate`: ritm cardiac mediu pe parcursul activitatii
- `Body_Temp`: temperatura medie pe parcursul activitatii
- `Calories`: numarul de calorii consumata

## Note despre setul de date:

- Câmpul-ținta este Calories. Date fiind celelalte feature-uri, scopul este de a prezice Calories. Setul de date de evaluare vizibil pentru candidați nu conține acest câmp, însă el este necesar platformei de evaluare. Metrica de evaluare folosita este MAE (media sumei diferentelor in modul dintre output-ul predictiei voastre si cea corecta).
- Câmpul Gender, avand tipul string trebuie transformat in date numerice într-un fel sau altul pentru a putea fi folosit in algoritmii de ML.
- Unele câmpuri pot fi inutile in predicția campului-tinta. Incercati sa analizati datele si sa selectați doar ce este nevoie sau ar putea explica predictia.

## Cerinte

**P1 (40p**). Incarcati setul de date de antrenare si scrieți un fișier output_0.csv in care sa aveți header-ul:

"Samples,No. Males,Average Duration,SeniorUsers”

- Samples: numarul de linii de input din setul de date de antrenare, folosit in scop de verificare locala
- No. Males: numarul de date care descriu activitati realizate de barbati
- Average Duration: durata medie a activitatiilor, aproximata la 2 zecimale
- SeniorUsers: numarul de utilizatori peste 75 de ani 

Fiecare din cele 4 componente valoreaza 10p.

**P2 (60p)** 

(a) Implementati un model de AI si rulați predicția pentru fiecare rând din `task1_dataset_eval.csv` (40p)

Output-ul trebuie sa fie un fișier output_1.csv cu o singura coloana numita Calories.

(b) O echipa de handbal masculin are nevoie sa estimeze consumul caloric pentru a optimiza dieta jucatorilor. Implementati un model de AI si rulați predicția pentru fiecare rând din `task2_dataset_eval.csv` (20p)

Output-ul trebuie sa fie un fișier output_2.csv cu o singura coloana numita Calories.
