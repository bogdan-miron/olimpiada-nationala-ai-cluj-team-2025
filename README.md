# Credit Score Challenge

## Prezentare generală

Setul de date utilizat pentru această provocare provine de la o bancă și conține informații despre utilizatori, având ca scop prezicerea dacă un utilizator este un bun platnic.

Setul de date este echilibrat pentru nivel de judeteana si ofera elevilor urmatoarele provocari:

- Gestionarea valorilor lipsă
- Diferențierea dintre date categorice și numerice
- Imbalanced data set (but not to heavily imbalanced) 
- Dimensionalitate mare a datelor
- Outliers

## Setul de date

Setul de date pentru această problema poate fi găsit aici: [Clasificarea Scorului de Credit](https://www.kaggle.com/datasets/parisrohan/credit-score-classification/data).

## Sarcini

### Task 1: Explorarea datelor

1. Câte valori nule sunt prezente în coloana `Amount_Invested_Monthly`?
2. Care este datoria medie a înregistrărilor care au un `Credit_Utilization_Ratio` mai mare sau egal cu 25?
3. Câte valori unice există în coloana `Months`?
4. Câte linii de intrare sunt în `train.csv`? (verificare locală)

### Task 2: Construirea modelului

Construieste un model de învățare automată pentru a prezice categoria scorul de credit pentru fiecare înregistrare din setul de date (Poor, Standard, Good). Pentru o dificultate mai redusa, se poate modifica setul pentru o clasificare binara (Poor, Good).

## Sfaturi

- Utilizați tehnici adecvate pentru gestionarea datelor lipsă.
- Înțelegeți și preprocesați corect caracteristicile categorice și numerice.
- Abordați dezechilibrul setului de date, dacă este necesar.
- Luați în considerare selecția sau ingineria caracteristicilor pentru o performanță mai bună a modelului.
- Alegeți un algoritm de învățare automată potrivit și ajustați-l pentru rezultate optime.
- Considerati custom thresholds. Merg mai bine?
- Hyperparam tuning - grid search, optuna etc.

