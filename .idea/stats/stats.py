import json
from statistics import mean
from core.file_io import list_round_files, load_round

def calculate_round_stats():
    files = list_round_files()
    if not files:
        print("Keine gespeicherte Runde gefunden.")
        return

    for idx, file in enumerate(files):
        print(f"{idx+1}. {file}")

    try:
        choice = int(input("Wähle eine Runde für Statistiken: "))
        if not (1 <= choice <= len(files)):
            raise ValueError
        data = load_round(files[choice-1])
        punkte = [h["score"] for h in data if "score" in h]
        if not punkte:
            print("Keine gültigen Scores.")
            return
        print(f"\n📊 Statistik für {files[choice-1]}:")
        print(f"Anzahl Bahnen: {len(punkte)}")
        print(f"Durchschnitt: {mean(punkte):.2f}")
        print(f"Max: {max(punkte)}, Min: {min(punkte)}")
    except (ValueError, IndexError):
        print("Ungültige Auswahl.")