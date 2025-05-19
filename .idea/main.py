from datetime import datetime
from core.holes import get_default_holes
from core.inputs import *
from core.file_io import save_round
from stats.stats import calculate_round_stats
from ui.display import show_saved_rounds

def main():
    while True:
        try:
            menu = int(input("""
Was möchtest du tun:
(1) Neue Runde
(2) Alte Runde einsehen
(3) Statistiken
(4) Beenden
"""))
        except ValueError:
            print("Bitte eine Zahl eingeben.")
            continue

        if menu == 1:
            holes = get_default_holes()
            for hole in holes:
                print(f"--- {hole.name} ---")
                processFairway(hole)
                processGreenHit(hole)
                if not hole.hit_Green:
                    processUpAndDown(hole)
                processPutts(hole)
                processScore(hole)
            filename = f"runde_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
            save_round(holes, filename)
            print(f"Runde gespeichert unter {filename}.\n")
        elif menu == 2:
            show_saved_rounds()
        elif menu == 3:
            calculate_round_stats()
        elif menu == 4:
            print("Beende Programm.")
            break
        else:
            print("Ungültige Auswahl.")

if __name__ == "__main__":
    main()