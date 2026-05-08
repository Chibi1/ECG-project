# 🫀 ECG Real-Time Monitoring System (100+ Hz)

## 📌 Informacje o projekcie
- **Przedmiot:** Systemy współbieżne i aplikacje webowe  
- **Temat:** Wizualizacja sygnału EKG (100+ Hz)  
- **Rok studiów:** [UZUPEŁNIJ]  
- **Prowadzący:** [UZUPEŁNIJ]  
- **Autorzy:** [Twoje imię i nazwisko]  
- **Katedra:** KIB  
- **Uczelnia:** [Logo uczelni]

---

# 🎯 Cel projektu

Celem projektu jest zaprojektowanie i implementacja systemu webowego do symulacji i analizy sygnału EKG w czasie rzeczywistym (100+ Hz).

System analizuje:

- współbieżność (multithreading, race conditions)
- opóźnienia (latency)
- jitter
- drift zegara (backend–frontend)
- spójność danych
- przeciążenie systemu
- synchronizację
- metryki systemowe

---

# 🏥 Analiza potrzeb i wymagań klinicznych

## 🔍 Identyfikacja problemu

Systemy EKG muszą działać w czasie rzeczywistym. Opóźnienia mogą prowadzić do błędnej diagnozy.

Kluczowe założenie:
> alarmy liczone są od momentu zdarzenia, nie od dostarczenia danych

---

## 👥 Użytkownicy

- personel medyczny
- systemy monitoringu pacjentów
- systemy analizy sygnałów

---

## ⚠️ Ryzyka

- latency
- jitter
- drift zegara
- race conditions
- przeciążenie systemu

---

# 🏗️ Architektura

## Backend (Flask + SocketIO)
- generowanie EKG
- streaming danych
- API `/start`, `/stop`
- WebSocket

## Warstwa usług
- ecg_loader.py
- ecg_streamer.py
- clock_simulator.py (planowane)

## Frontend
- HTML + JavaScript
- Chart.js
- WebSocket

---

# ⚙️ Etap 1

✔ start/stop EKG  
✔ streaming danych  
✔ wizualizacja Chart.js  
✔ API-first architecture  

---

# 📊 Etapy projektu

## 🟢 Etap 1
- odtwarzanie sygnału

## 🟡 Etap 2
- latency injection
- jitter
- pomiar renderowania

## 🔴 Etap 3
- race conditions
- drift zegara
- synchronizacja

## 🔵 Etap 4
- analiza metryk
- raport
- kompromisy systemowe

---

# 🧪 Technologie

- Python
- Flask
- Flask-SocketIO
- threading
- JavaScript
- Chart.js
- WebSocket

---

# 🚧 Ograniczenia

- brak bazy danych (Etap 1)
- brak kolejek (zgodnie z wymaganiami)
- sygnał syntetyczny

---

# 📌 Podsumowanie

System analizuje:

- współbieżność
- czas rzeczywisty
- spójność danych
- problemy synchronizacji
- wpływ czasu na EKG

---

# 🚀 Status

✔ Etap 1 ukończony  
⏳ Etap 2 w trakcie  
⏳ Etap 3 w trakcie  
⏳ Etap 4 w trakcie

