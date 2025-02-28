Prezicerea Livrării Pachetelor la Timp

### Problema
În logistica modernă, livrarea la timp a pachetelor este esențială pentru satisfacția clienților și eficiența operațională. 
Dezvoltați un model care să prezică dacă un pachet va fi livrat la timp (`on_time = 1`) sau întârziat (`on_time = 0`). 

Veți antrena modelul folosind setul de date de antrenament furnizat și apoi veți genera predicții pentru un set de date ne-etichetat.

### Descrierea Setului de Date

1. **Setul de Date de Antrenament (`dataset_train.csv`):**
   - **Caracteristici:**
     - `distance_km (0.5-700)`: Distanța de la depozit până la destinația de livrare (în kilometri). Distanțele mai scurte indică, în general, o probabilitate mai mare ca livrarea să fie la timp.
     - `package_weight_kg (0.5-150)`: Greutatea pachetului (în kilograme). Pachetele mai ușoare sunt, de obicei, livrate mai rapid.
     - `traffic_level (1-12)`: Un indicator al condițiilor de trafic (tip intreg, 1-trafic redus, 12-trafic aglomerat maxim)
   - **Țintă:**
     - `on_time`: O variabilă binară în care `1` indică faptul că pachetul a fost livrat la timp, iar `0` indică întârzierea.

2. **Setul de Date pentru Predicție (`dataset_predict.csv`):**
   - Conține 50 de eșantioane cu aceleași caracteristici (`distance_km`, `package_weight_kg` și `traffic_level`) ca setul de antrenament, dar fără coloana `on_time`.
   - Modelul vostru va genera predicții pentru aceste eșantioane.

### Rezultatul Așteptat: Un fisier csv `dataset_predict.csv` care să includă urmatoarele 3 coloane:
- **P1 (20p)**: `mean_traffic_level`(20p) - reprezentand media nivelelor de trafic din setul de date pentru predictie, precizie de 2 decimale (doar prima linie se i-a in considerare).
- **P2 (20p)**: `std_traffic_level` (20p) - reprezentand deviatia standard a aceluiasi camp, precizie de 2 decimale  (doar prima linie se i-a in considerare).
- **P3 (60p): `on_time` - cu predicțiile modelului vostru, `1` pentru livrare la timp, respectiv `0` pentru întârziere.
