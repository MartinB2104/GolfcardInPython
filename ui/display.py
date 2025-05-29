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

def display_hole_info(hole, score_bisher):
    print(f"""--- {hole.name} ---
    Länge: {hole.length} Meter
    Par: {hole.par}
    """)
    if score_bisher == 0:
        print("Score bisher: even par")
    elif score_bisher < 0:
        print(f"Score bisher: -{score_bisher}")
    else:
        print(f"Score bisher: +{score_bisher}")