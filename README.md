# Spot-the-Mask

Aceasta este o soluție de bază pentru problema **Spot-the-Mask**, o problemă de **computer vision** care presupune detectarea purtării măștii într-un set de imagini. Soluția urcată pe GitHub este un **schelet de bază**, care obține aproximativ **95%** pe **[https://zindi.africa/competitions/spot-the-mask](https://zindi.africa/competitions/spot-the-mask)**, dar poate fi îmbunătățită semnificativ prin optimizări.

## Descrierea Problemei

Problema constă în clasificarea imaginilor pentru a determina dacă o persoană poartă sau nu mască. Modelul trebuie antrenat pe un set de imagini etichetate și apoi testat pe un set necunoscut pentru a evalua performanța.

## Structura Soluției

Soluția este împărțită în mai multe etape:

1. **Parsarea inputului** – Citirea și procesarea dataset-ului.
2. **Preprocesarea imaginilor** – Redimensionare, normalizare
3. **Antrenarea unui model de bază** – Model CNN simplu, cu posibilități de îmbunătățire.

## Modificări pentru Elevi

Pentru a ușura înțelegerea și implementarea, se poate oferi direct dataset-ul organizat în foldere etichetate (`mask/` și `no_mask/`), astfel încât elevii să se concentreze pe antrenarea modelului fără a se preocupa de parsarea inițială a datelor.

## Posibile Îmbunătățiri

- **Arhitecturi mai avansate**: Transfer learning cu modele pre-antrenate (ResNet, MobileNet, EfficientNet)
- **Augmentare avansată**: Tehnici precum rotații, flip, blur etc.
- **Optimizarea hiperparametrilor**: Learning rate tuning, batch size tuning
- **Postprocesare mai inteligentă**: Ensemble learning, threshold tuning
