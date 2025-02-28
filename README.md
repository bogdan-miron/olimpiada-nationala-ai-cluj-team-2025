# Credit Score Challenge

## Prezentare generală

Setul de date utilizat pentru această provocare provine de la o bancă și conține informații despre utilizatori, având ca scop prezicerea dacă un utilizator este un bun platnic. Problema este una de clasificare cu 3 posible etichete asociate unui client: `POOR CREDIT SCORE`, `STANDARD CREDIT SCORE` și `GOOD CREDIT SCORE`.

## Setul de date

Setul de date initial pentru această problema poate fi găsit aici: [Clasificarea Scorului de Credit](https://www.kaggle.com/datasets/parisrohan/credit-score-classification/data).

## Sarcini

### Task 1: Explorarea datelor

1. Cate linii de intrare sunt in `dataset_train`?
2. Care este media pentru 'Salariul în mână' ('the monthly in hand salary of a person') al clienților care au un `Credit_Utilization_Ratio` mai mare sau egal cu 25?
3. Câte valori unice sunt înregistrate pentru atributul `Months`?
4. Câte valori unice ale atributului `SSN` care se termină în `20` există în dataset?

   Fisierul de iesire output_1.csv va contine 4 coloane: `Samples`, `Avg_Debt`, `Unique_Months` si `SSN_Count`, in aceasta ordine.

### Task 2: Construirea modelului

Construieste un model de învățare automată pentru a prezice categoria scorul de credit pentru fiecare înregistrare din setul de date.

  Fisierul de iesire output_2.csv va contine doua coloane: `ID` si `Credit_Score. IMPORTANT, A NU SE SCHIMBA ORDINEA ID-URILOR DIN FISIERUL dataset_train.

## General notes & about:
Setul de date este echilibrat pentru nivel de judeteana si ofera elevilor urmatoarele provocari:

- Gestionarea valorilor lipsă
- Diferențierea dintre date categorice și numerice
- Imbalanced data set (but not to heavily imbalanced) 
- Dimensionalitate mare a datelor
- Outliers

## Sfaturi si imbunatatiri
- Utilizați tehnici adecvate pentru gestionarea datelor lipsă.
- Înțelegeți și preprocesați corect caracteristicile categorice și numerice.
- Abordați dezechilibrul setului de date, dacă este necesar.
- Luați în considerare selecția sau ingineria caracteristicilor pentru o performanță mai bună a modelului.
- Alegeți un algoritm de învățare automată potrivit și ajustați-l pentru rezultate optime.
- Considerati custom thresholds. Merg mai bine?
- Hyperparam tuning - grid search, optuna etc.

