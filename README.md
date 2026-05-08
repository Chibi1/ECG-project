\# 🫀 ECG Real-Time Monitoring System (100+ Hz)



\## 📌 Informacje o projekcie

\- \*\*Przedmiot:\*\* Systemy współbieżne i aplikacje webowe

\- \*\*Temat:\*\* Wizualizacja sygnału EKG (100+ Hz)

\- \*\*Rok studiów:\*\* \[UZUPEŁNIJ]

\- \*\*Prowadzący:\*\* \[UZUPEŁNIJ]

\- \*\*Autorzy:\*\* \[Twoje imię i nazwisko]

\- \*\*Katedra:\*\* KIB

\- \*\*Uczelnia:\*\* \[Logo uczelni]



\---



\# 🎯 Cel projektu



Celem projektu jest zaprojektowanie i implementacja systemu webowego do symulacji i analizy sygnału EKG w czasie rzeczywistym (100+ Hz).



System został zaprojektowany w celu analizy kluczowych problemów systemów współbieżnych i systemów czasu rzeczywistego w środowisku medycznym:



\- współbieżność (multithreading, race conditions)

\- opóźnienia (latency)

\- jitter (zmienność opóźnień)

\- drift zegara (rozjazd czasu backend–frontend)

\- spójność danych w czasie rzeczywistym

\- przeciążenie systemu

\- mechanizmy synchronizacji

\- analiza metryk systemowych



\---



\# 🏥 Analiza potrzeb i wymagań klinicznych



\## 🔍 Identyfikacja problemu



Systemy monitorowania EKG w medycynie wymagają przetwarzania danych w czasie rzeczywistym. Nawet niewielkie opóźnienia mogą prowadzić do błędnej interpretacji stanu pacjenta.



Kluczowy problem:

> alarmy medyczne muszą być liczone od momentu zdarzenia, a nie od momentu dostarczenia danych.



\---



\## 👥 Użytkownicy systemu



\- personel medyczny (lekarze, pielęgniarki)

\- systemy monitoringu pacjentów

\- systemy analizy danych EKG



\---



\## ⚠️ Analiza ryzyk



\- opóźnienia transmisji danych (latency)

\- jitter wpływający na dokładność wykresu

\- drift zegara backend–frontend

\- utrata synchronizacji danych

\- przeciążenie systemu przy wielu źródłach danych

\- race conditions w środowisku współbieżnym



\---



\# 🏗️ Projekt architektury systemu



\## 🔙 Backend (Python + Flask + SocketIO)



Odpowiada za:

\- generowanie sygnału EKG (syntetycznego lub z pliku)

\- streaming danych w czasie rzeczywistym

\- API REST (`/start`, `/stop`)

\- komunikację WebSocket



\---



\## ⚙️ Warstwa usług



\- `ecg\_loader.py` → generowanie lub ładowanie sygnału EKG

\- `ecg\_streamer.py` → streaming danych w osobnym wątku

\- `clock\_simulator.py` → (planowane) symulacja driftu zegara



\---



\## 📡 Komunikacja



\- WebSocket (Flask-SocketIO)

\- REST API



\---



\## 🖥️ Frontend



\- HTML + JavaScript

\- Chart.js (wizualizacja EKG)

\- WebSocket client (odbiór danych w czasie rzeczywistym)



\---



\# ⚙️ Etap 1 – Implementacja bazowa



\## ✔️ Zrealizowana funkcjonalność



\- uruchomienie generowania sygnału EKG (`/start`)

\- zatrzymanie generowania (`/stop`)

\- streaming danych EKG przez WebSocket

\- wizualizacja sygnału w przeglądarce (Chart.js)

\- architektura API-first



\---



\## 🧪 Sygnał EKG



W projekcie wykorzystano:

\- syntetyczny generator sygnału EKG

\- możliwość rozszerzenia o dane z Kaggle



\---



\## 🏗️ Struktura repozytorium



backend/

├── app.py

├── api/

├── services/

│ ├── ecg\_loader.py

│ ├── ecg\_streamer.py

│ └── clock\_simulator.py

├── models/

├── data/

├── logs/

└── tests/



frontend/

└── index.html





\---



\# 📊 Plan realizacji etapów projektu



\## 🟢 Etap 1 – Odtwarzanie sygnału z pliku ✔️

\- generator EKG

\- streaming danych

\- podstawowa wizualizacja



\---



\## 🟡 Etap 2 – Symulacja zaburzeń (planowane)



\- opóźnienia transmisji (latency injection)

\- jitter (losowe odchylenia czasowe)

\- pomiar czasu renderowania

\- logowanie metryk systemowych



\---



\## 🔴 Etap 3 – Współbieżność i błędy



\- race conditions w streamingu danych

\- drift zegara backend–frontend

\- mechanizmy synchronizacji (locki, buforowanie)

\- analiza błędów przed i po poprawkach



\---



\## 🔵 Etap 4 – Analiza końcowa



\- raport metryk systemowych

\- analiza kompromisów:

&#x20; - wydajność vs spójność danych

&#x20; - opóźnienia vs bezpieczeństwo

\- demonstracja działania systemu



\---



\# 🧪 Technologie



\- Python 3

\- Flask

\- Flask-SocketIO

\- threading

\- JavaScript

\- Chart.js

\- WebSocket



\---



\# 🚧 Ograniczenia (Etap 1)



\- brak bazy danych (planowane w dalszych etapach)

\- brak systemu kolejkowego (zgodnie z wymaganiami)

\- sygnał EKG syntetyczny

\- brak mechanizmów korekcji driftu (Etap 3–4)



\---



\# 📌 Podsumowanie



Projekt stanowi symulację systemu monitoringu EKG w czasie rzeczywistym, skupiając się na analizie:



\- współbieżności

\- opóźnień i jittera

\- synchronizacji systemów rozproszonych

\- spójności danych medycznych

\- wpływu czasu na interpretację sygnałów



\---



\# 🚀 Status



✔ Etap 1 – ukończony  

⏳ Etap 2 – w przygotowaniu  

⏳ Etap 3 – w przygotowaniu  

⏳ Etap 4 – w przygotowaniu

