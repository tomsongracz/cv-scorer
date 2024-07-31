import os
import fitz  
import docx
import tkinter as tk
from tkinter import filedialog
import re
import subprocess  
import platform  

# Funkcja do ekstrakcji tekstu z pliku PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Funkcja do ekstrakcji tekstu z pliku DOCX
def extract_text_from_word(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

# Funkcja do ekstrakcji tekstu z pliku
def extract_text(file_path):
    if file_path.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith('.docx'):
        return extract_text_from_word(file_path)
    return ""

# Funkcja do ekstrakcji imienia i nazwiska z tekstu
def extract_name_from_text(text):
    lines = text.split("\n")
    for line in lines:
        if line.strip():
            name = line.strip()
            parts = name.split(' ')
            if len(parts) == 2:
                first_name = parts[0].capitalize()
                last_name = parts[1].capitalize()
                return f"{first_name} {last_name}"
            else:
                return name.capitalize()
    return "Nieznane"

# Funkcja do obliczania punktów za słowa kluczowe
def score_cv(text, keywords):
    score = 0
    # Tworzymy zestaw słów kluczowych, aby uniknąć duplikatów
    keyword_set = set(keyword.strip().lower() for keyword in keywords)
    # Sprawdzamy każde słowo kluczowe
    for keyword in keyword_set:
        # Używamy wyrażenia regularnego do sprawdzenia, czy słowo kluczowe występuje w tekście
        pattern = r'\b' + re.escape(keyword) + r'\b'
        if re.search(pattern, text, re.IGNORECASE):
            score += 1
    return score

# Funkcja do przetwarzania CV
def process_cvs(file_paths, keywords):
    results = []
    for file_path in file_paths:
        text = extract_text(file_path)
        if text:
            name = extract_name_from_text(text)
            score = score_cv(text, keywords)
            results.append((name, file_path, score))
    return sorted(results, key=lambda x: x[2], reverse=True)

# Funkcja do wgrywania plików
def upload_files():
    global file_paths
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF and Word files", "*.pdf *.docx"), ("PDF files", "*.pdf"), ("Word files", "*.docx")])
    result_list.delete(0, tk.END)
    result_list.insert(tk.END, f"Załadowano {len(file_paths)} plików.\n")


# Funkcja do przeszukiwania CV pod kątem słów kluczowych
def search_keywords():
    if not file_paths:
        result_list.delete(0, tk.END)
        result_list.insert(tk.END, "Najpierw załaduj pliki CV.\n")
        return
    keywords = entry_keywords.get().split(',')
    results = process_cvs(file_paths, keywords)
    result_list.delete(0, tk.END)
    for name, file_path, score in results:
        result_list.insert(tk.END, f"{name} - {file_path} - Score: {score}")

# Funkcja do otwierania pliku CV po podwójnym kliknięciu
def open_file(event):
    try:
        selected_index = result_list.curselection()[0]
        file_path = result_list.get(selected_index).split(" - ")[1].split(" - ")[0]
        if platform.system() == 'Darwin':  # macOS
            subprocess.call(['open', file_path])
        elif platform.system() == 'Windows':  # Windows
            os.startfile(file_path)
        else:  # Inne systemy operacyjne (np. Linux)
            subprocess.call(['xdg-open', file_path])
    except IndexError:
        pass

# GUI
root = tk.Tk()
root.title("CV Scorer")

frame = tk.Frame(root)
frame.pack(pady=10)

label_keywords = tk.Label(frame, text="Wpisz słowa kluczowe (oddzielone przecinkami):")
label_keywords.pack(pady=5)

entry_keywords = tk.Entry(frame, width=50)
entry_keywords.pack(pady=5)

btn_upload = tk.Button(frame, text="Załaduj pliki CV", command=upload_files)
btn_upload.pack(pady=5)

btn_search = tk.Button(frame, text="Szukaj słów kluczowych", command=search_keywords)
btn_search.pack(pady=5)

# Dodajemy etykietę informacyjną nad tabelą wyników
info_label = tk.Label(root, text="Kliknij w wybraną pozycję, aby otworzyć CV")
info_label.pack(pady=5)

result_list = tk.Listbox(root, height=20, width=100)
result_list.pack(pady=10)

result_list.bind("<Double-1>", open_file)  # Bind the double click event to the open_file function

file_paths = []  # Przechowywanie ścieżek do załadowanych plików

root.mainloop()
