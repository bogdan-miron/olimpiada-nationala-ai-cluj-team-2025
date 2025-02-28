### Problema Prezicerii Livrării Pachetelor la Timp

În logistica modernă, livrarea la timp a pachetelor este esențială pentru satisfacția clienților și eficiența operațională. 
Dezvoltați un model care să prezică dacă un pachet va fi livrat la timp (`on_time = 1`) sau întârziat (`on_time = 0`). 

Veți antrena modelul folosind setul de date de antrenament furnizat și apoi veți genera predicții pentru un set de date ne-etichetat.

### Descrierea Setului de Date

1. **Setul de Date de Antrenament (`train_data.csv`):**
   
**Caracteristici:**
     - `id (număr natural)`: Numărul care identifică livrarea - număr natural unic.
     - `distance_km (0.5-700)`: Distanța de la depozit până la destinația de livrare (în kilometri). Distanțele mai scurte indică, în general, o probabilitate mai mare ca livrarea să fie la timp.
     - `package_weight_kg (0.5-150)`: Greutatea pachetului (în kilograme). Pachetele mai ușoare sunt, de obicei, livrate mai rapid.
     - `traffic_level (1-12)`: Un indicator al condițiilor de trafic (tip intreg, 1 - trafic redus, 12 - trafic aglomerat maxim)
**Țintă:**
     - `on_time`: O variabilă binară în care `1` indică faptul că pachetul a fost livrat la timp, iar `0` indică întârzierea.

2. **Setul de Date pentru Predicție (`test_data.csv`):**
   - Conține 50 de eșantioane cu aceleași caracteristici (`id`,`distance_km`, `package_weight_kg` și `traffic_level`) ca setul de antrenament, dar fără coloana `on_time`.
   - Modelul vostru va genera predicții pentru aceste eșantioane.

### Rezultatul așteptat: 
   Un fisier csv `output.csv` care să includă următoarele 4 coloane: pe prima coloană sunt `id`-urile din `test_data.csv` urmate de alte 3 coloane pentru următoarele 3 cerințe. 
- **P1 (20p)**: `mean_traffic_level` - reprezentând media nivelelor de trafic din setul de date pentru predictie, precizie de 2 decimale (aceeași valoare pe întreaga coloană).
- **P2 (20p)**: `std_traffic_level` - reprezentând deviația standard a aceluiași câmp, cu precizie de 2 decimale  (aceeași valoare pe întreaga coloană).
- **P3 (60p)**: `on_time` - cu predicțiile modelului vostru, `1` pentru livrare la timp, respectiv `0` pentru întârziere.

### Evaluare:
Trimiteți un singur csv combinând fiecare `id` cu răspunsul pentru fiecare subtask pe coloana corespunzătoare, ca în fișierul dat ca exemplu în `sample_output.csv`.
Această problemă nu are scor final diferit de scorul parțial. Scorul din timpul concursului e cel cu care veți rămâne la final.

Judging function:
acc = 1 if (submission['correct_values'] - submission['output_values']).abs().mean() <= 0.02 else 0
score = acc * 20
return score, acc, score, acc

acc = metrics.accuracy_score(list(submission['correct_values']), list(submission['output_values']))
score = round(min(max(60.0 * (acc - 0.8) / 0.178, 0), 60),2)
return score, acc, score, acc