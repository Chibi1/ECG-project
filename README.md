# 🫀 ECG Real-Time Monitoring System (100+ Hz)

---

## 🏫 Informacje o projekcie

- **Autor:** Dominika Rogowska  
- **Przedmiot:** Rozwój aplikacji internetowych w medycynie  
- **Rok studiów:** 3  
- **Prowadzący:** dr inż. Anna Węsierska  
- **Uczelnia:** Politechnika Gdańska  
- **Wydział:** ETI  
- **Katedra:** Katedra Inżynierii Biomedycznej (KIB)

---

## 🎯 Cel systemu

Celem projektu jest implementacja systemu symulującego monitorowanie sygnału EKG w czasie rzeczywistym (≥100 Hz), z naciskiem na analizę problemów systemów współbieżnych i rozproszonych.

System służy do badania:

- opóźnień transmisji danych (latency)
- zmienności opóźnień (jitter)
- driftu zegara backend–frontend
- współbieżności i race conditions
- spójności danych w systemach czasu rzeczywistego
- przeciążenia systemu
- mechanizmów synchronizacji

---

## 🏥 Kontekst kliniczny

W systemach medycznych monitorujących EKG kluczowe znaczenie ma czas reakcji systemu.

Błędna interpretacja czasu zdarzeń może prowadzić do:

- opóźnionych alarmów
- fałszywych odczytów stanu pacjenta
- utraty spójności danych monitoringu

> W medycynie krytyczne jest, aby alarm był generowany w momencie zdarzenia fizjologicznego, a nie w momencie jego dostarczenia do systemu.

---

## ⚠️ Problem badawczy

Projekt analizuje problem:

> Jak opóźnienia, jitter i rozjazd zegarów wpływają na poprawność wizualizacji sygnału EKG w systemie czasu rzeczywistego?

---

## 🏗️ Architektura systemu

System składa się z trzech warstw:

### 🔙 Backend (Flask + SocketIO)
- generacja sygnału EKG (syntetycznego)
- streaming danych w czasie rzeczywistym
- API (`/start`, `/stop`)
- WebSocket communication

### ⚙️ Warstwa przetwarzania
- `ecg_loader.py` → generator sygnału EKG
- `ecg_streamer.py` → streaming w wątku
- `clock_simulator.py` → symulacja driftu zegara (Etap 3)

### 🖥️ Frontend
- HTML + JavaScript
- Chart.js (wizualizacja sygnału)
- WebSocket client

---

## 📡 Model komunikacji

ECG Generator → Backend (Flask) → WebSocket → Frontend → Chart.js


---

## ⚙️ Etap 1 – System bazowy

### ✔ Funkcjonalność
- generowanie sygnału EKG
- streaming danych 100+ Hz
- wizualizacja w czasie rzeczywistym
- API-first design

---

## 📊 Etapy badawcze

### 🟢 Etap 1 – Odtwarzanie sygnału
- generacja EKG
- streaming danych

### 🟡 Etap 2 – Zaburzenia systemowe
- latency injection
- jitter simulation
- pomiar opóźnień renderowania
- logging metryk

### 🔴 Etap 3 – Współbieżność
- race conditions
- drift zegara backend–frontend
- synchronizacja (locks, buffering)
- analiza przed/po korekcji

### 🔵 Etap 4 – Analiza końcowa
- raport metryk systemowych
- analiza kompromisów:
  - wydajność vs spójność
  - latency vs bezpieczeństwo
- demonstracja działania systemu

---

## 🧪 Instrumentacja i metryki

System umożliwia analizę:

- latency (ms)
- jitter (odchylenie czasu)
- throughput (Hz)
- drift czasowy (ms/s)
- opóźnienie renderowania frontend

---

## 🧰 Technologie

- Python 3
- Flask
- Flask-SocketIO
- threading
- WebSocket
- JavaScript
- Chart.js

---

## 🚧 Ograniczenia

- brak bazy danych (celowo – Etap 1)
- brak systemu kolejkowego (zgodnie z wymaganiami)
- dane syntetyczne EKG
- brak mechanizmów korekcji driftu (Etap 3–4)

---

## 📌 Wnioski wstępne

System pokazuje, że:

- nawet małe opóźnienia wpływają na interpretację danych medycznych
- synchronizacja czasu jest krytyczna w systemach EKG
- współbieżność wprowadza problemy spójności danych
- frontend i backend mogą interpretować czas inaczej

---

## 🚀 Status projektu

✔ Etap 1 – ukończony  
⏳ Etap 2 – w trakcie  
⏳ Etap 3 – w przygotowaniu  
⏳ Etap 4 – planowany