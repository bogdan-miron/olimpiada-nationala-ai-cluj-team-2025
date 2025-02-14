# Recomandări pentru propunătorii de probleme

## Input si Output (v. si folderul Solutii)

Candidații primesc un set de date pentru a face antrenarea – dataset_train.csv si unul pentru evaluare – dataset_eval.csv. La cel de-al doilea, campul tinta, “Price”, este ascuns.

Candidații au doua fisiere de salvat in folderul lor:

- Output_1.csv in care sunt cele 4 valori punctate
- Output_2.csv, fiecare linie contine predictia campului target corespunzator liniei din dataset_eval.csv

Candidații trebuie sa știe dinainte metrica de evaluare.

## Procesarea si crearea unui dataset

Porniti de la un dataset existent, nu foarte cunoscut de preferat dar incercati sa evidentiati capcanele pe cat posibil sau dificultatile ulterioare in incarcare si procesare.

Spre exemplu mi-am dat seama ca ar trebui sa las coloanele din setul original care sunt clare sau care sa le pot procesa astfel incat sa fie usor de vizualizat.

In acest sens am procesat dataset-ul original cu Dataset.ipynb, posibil sa gasiti acest cod util.

## Implementati solutia si iterati asupra ei astfel incat sa fie realizabila cu cat mai puține librarii aditionale sau API-uri.

Spre exemplu, intentionat in solutia din Solutii am lasat procesarea datelor manuala, cu cat mai putin interactiuni.
