# CV Scorer – Analiza i ocena CV na podstawie słów kluczowych

Aplikacja w Pythonie umożliwiająca analizę i ocenę plików CV (`.pdf` i `.docx`) pod kątem występowania określonych słów kluczowych.  
Użytkownik może wgrać wiele plików, wpisać interesujące go słowa kluczowe, a następnie uzyskać listę CV posortowaną według liczby dopasowań.  
Po dwukrotnym kliknięciu na wynik aplikacja automatycznie otworzy wybrane CV.

---

## 🚀 Funkcje
- Obsługa plików **PDF** i **Word (DOCX)**  
- Automatyczna **ekstrakcja tekstu** z dokumentów  
- Identyfikacja **imienia i nazwiska** z treści CV  
- **Ocena punktowa** na podstawie słów kluczowych  
- **Sortowanie wyników** od najlepiej dopasowanych  
- **Podgląd CV** przez dwukrotne kliknięcie w wynik  
- Prosty **graficzny interfejs (Tkinter)**  

---

## 🛠️ Wymagania
- Python **3.8+**
- Zainstalowane biblioteki:
  ```bash
  pip install PyMuPDF python-docx
  ```

(Opcjonalnie: tkinter jest częścią standardowej biblioteki Pythona — nie trzeba instalować osobno.)

---

▶️ Jak uruchomić

Sklonuj repozytorium:
```bash
git clone https://github.com/tomsongracz/cv-scorer.git
cd cv-scorer
```

Zainstaluj wymagane pakiety:
```bash
pip install -r requirements.txt
```

(Jeśli nie masz pliku requirements.txt, użyj:)
```bash
pip install PyMuPDF python-docx
```

Uruchom aplikację:
```bash
python cv_scorer.py
```

---

💡 Jak używać

1. Kliknij „Załaduj pliki CV” i wybierz swoje pliki .pdf lub .docx.

2. Wpisz słowa kluczowe oddzielone przecinkami, np.:

3. Python, Excel, SQL, analiza danych

4. Kliknij „Szukaj słów kluczowych”, aby rozpocząć analizę.

Wyniki pojawią się w oknie listy – kliknij dwukrotnie, by otworzyć wybrane CV.

---

📂 Struktura projektu
```bash
cv-scorer/
│
├── cv_scorer.py        # Główny plik aplikacji
├── requirements.txt    # Lista zależności
└── README.md           # Dokumentacja projektu
```
---

👤 Autor

Projekt przygotowany w celach edukacyjnych i demonstracyjnych.
Możesz mnie znaleźć na GitHubie: tomsongracz

---
