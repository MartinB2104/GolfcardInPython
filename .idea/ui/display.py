from core.file_io import list_round_files, load_round

def show_saved_rounds():
    files = list_round_files()
    if not files:
        print("Keine gespeicherte Runde gefunden.")
        return

    for idx, file in enumerate(files):
        print(f"{idx+1}. {file}")
    try:
        choice = int(input("Welche Runde anzeigen? "))
        if 1 <= choice <= len(files):
            data = load_round(files[choice-1])
            print(f"\nInhalt von {files[choice-1]}:")
            for h in data:
                print(h)
    except (ValueError, IndexError):
        print("Ungültige Auswahl.")