import json
from datetime import datetime
import os

class Holes:
    scoreToPar = {
        -3: "Albatross",
        -2: "Eagle",
        -1: "Birdie",
        0: "Par",
        1: "Bogey",
        2: "Double Bogey",
        3: "Triple Bogey"
    }


    def __init__(self, name, length, par, score,
             had_UpAndDown, made_UpAndDown,
             had_Bunkershot, made_Bunkershot,
             hit_Fairway, hit_Green):
        self.name = name
        self.length = length
        self.par = par
        self.score = score
        self.had_UpAndDown = had_UpAndDown
        self.made_UpAndDown = made_UpAndDown
        self.had_Bunkershot = had_Bunkershot
        self.made_Bunkershot = made_Bunkershot
        self.hit_Fairway = hit_Fairway
        self.hit_Green = hit_Green

# Instanzen
hole_one = Holes("Bahn 1", 495, 5, 0, False, False, False, False, False, False)
hole_two = Holes("Bahn 2", 159, 3, 0, False, False, False, False, False, False)
hole_three = Holes("Bahn 3", 363, 4, 0, False, False, False, False, False, False)
hole_four = Holes("Bahn 4", 458, 5, 0, False, False, False, False, False, False)
hole_five = Holes("Bahn 5", 140, 3, 0, False, False, False, False, False, False)
hole_six = Holes("Bahn 6", 455, 5, 0, False, False, False, False, False, False)
hole_seven = Holes("Bahn 7", 370, 4, 0, False, False, False, False, False, False)
hole_eight = Holes("Bahn 8", 99, 3, 0, False, False, False, False, False, False)
hole_nine = Holes("Bahn 9", 360, 4, 0, False, False, False, False, False, False)

# Liste der Instanzen
holes_list = [
    hole_one, hole_two, hole_three,
    hole_four, hole_five, hole_six,
    hole_seven, hole_eight, hole_nine
]

# Konvertiere in Dictionaries
holes_dict_list = [hole.__dict__ for hole in holes_list]

# In Datei schreiben
with open("data.json", "w") as outfile:
    json.dump(holes_dict_list, outfile, indent=4)


def processFairway(hole):
    while True:
        hit_Fairway = input("Hast du das Fairway getroffen? (True/False)").strip().lower()
        if hit_Fairway == "true":
            hole.hit_Fairway = True
            break
        elif hit_Fairway == "false":
            hole.hit_Fairway = False
            break
        else:
            print("ungültige Eingabe. Bitte nur True oder False eingeben.")


def processGreenHit(hole):
    while True:
        hit_Green = input("Hast du das Grün in regulation getroffen? (True/False)").strip().lower()
        if hit_Green == "true":
            hole.hit_Green = True
            break
        elif hit_Green == "false":
            hole.hit_Green = False
            break
        else:
            print("ungültige Eingabe. Bitte nur True oder False eingeben.")


def processBunkershot(hole):
    while True:
        had_Bunkershot = input("Hattest du ein Bunkerschlag? (True/False)").strip().lower()
        if had_Bunkershot == "true":
            hole.had_Bunkershot = True
            while True:
                made_Bunkershot = input("Hast du das bunker up and down gemacht? (True/False)").strip().lower()
                if made_Bunkershot == "true":
                    hole.made_Bunkershot = True
                    break
                elif made_Bunkershot == "false":
                    hole.made_Bunkershot = False
                    break
                else:
                    print("ungültige Eingabe. Bitte nur True oder False eingeben.")
            break
        elif had_Bunkershot == "false":
            hole.had_Bunkershot = False
            hole.made_Bunkershot = False
            break
        else:
            print("ungültige Eingabe. Bitte nur True oder False eingeben.")


def processUpAndDown(hole):
    while True:
        had_UpAndDown  = input("Hast du ein Up and Down gehabt? (True/False)").strip().lower()
        if had_UpAndDown == "true":
            hole.had_UpAndDown = True
            while True:
                made_UpAndDown = input("Hast du dein Up and Down gemacht? (True/False)").strip().lower()
                if made_UpAndDown == "true":
                    hole.made_UpAndDown = True
                    processBunkershot(hole)
                    break
                elif made_UpAndDown == "false":
                    hole.made_UpAndDown = False
                    break
                else:
                    print("ungültige Eingabe. Bitte nur True oder False eingeben.")
            break
        elif had_UpAndDown == "false":
            hole.had_UpAndDown = False
            break
        else:
            print("ungültige Eingabe. Bitte nur True oder False eingeben.")


def processPutts(hole):
    while True:
        try:
            putts = int(input("Wie viele Putts hast du gemacht? (Zahl eingeben!)"))
            if putts <= 0:
                print("Bitte eine positive Zahl eingeben.")
            else:
                hole.putts = putts
                break
        except ValueError:
            print("Bitte eine Zahl eingeben.")


def processScore(hole):
    while True:
        try:
            score = int(input("Wie war dein score? (Zahl eingeben!)"))
            if score < 1:
                print("Bitte eine sinnvolle Zahl eingeben!")
            else:
                hole.score = score
                break
        except ValueError:
            print("Bitte eine Zahl eingeben.")


def calculate_round_stats():
    files = [f for f in os.listdir() if f.startswith("runde_") and f.endswith(".json")]

    if not files:
        print("Keine gespeicherte Runde gefunden.")
        return

    print("\nGespeicherte Runde(n):")
    for idx, file in enumerate(files):
        print(f"{idx+1}. {file}")
    while True:
        try:
            choice = int(input("\nFür welche Runde sollen Statistiken ausgerechnet werden? (Zahl eingeben!): "))
            if 1 <= choice <= len(files):
                filename = files[choice-1]
                with open(filename, "r") as infile:
                    data = json.load(infile)
            else:
                print("Bitte eine Zahl zwischen 1 und", len(files), "eingeben.")
        except ValueError:
            print("Bitte eine Zahl eingeben.")
            continue


def show_saved_rounds():
    files = [f for f in os.listdir() if f.startswith("runde_") and f.endswith(".json")]

    if not files:
        print("Keine gespeicherte Runde gefunden.")
        return

    print("\nGespeicherte Runde(n):")
    for idx, file in enumerate(files):
        print(f"{idx+1}. {file}")

    while True:
        try:
            choice = int(input("\nWelche Runde soll angezeigt werden? (Zahl eingeben!): "))
            if 1 <= choice <= len(files):
                filename = files[choice-1]
                with open(filename, "r") as infile:
                    data = json.load(infile)
                    print(f"\nInhalt von {filename}:\n")
                    for hole in data:
                        print(hole)
                print()
                break
            else:
                print("Bitte eine Zahl zwischen 1 und", len(files), "eingeben.")
        except ValueError:
            print("Bitte eine Zahl eingeben.")
            continue

def main():
    while True:
        try:
            menu_nmbr = int(input("""Was möchtest du tun: 
            (1) Neue Runde
            (2) Alte Runde einsehen
            (3) Statistiken
            (4) Beenden
            """))
            if menu_nmbr < 1 or menu_nmbr > 4:
                print("Bitte eine Zahl zwischen 1 und 4 eingeben.")
                continue  # Eingabe wiederholen
        except ValueError:
            print("Bitte eine Zahl eingeben.")
            continue  # Eingabe wiederholen

        # Nach der Validierung kommen hier die Aktionen:
        if menu_nmbr == 1:
            for hole in holes_list:
                print(f"--- {hole.name} ---")
                processFairway(hole)
                processGreenHit(hole)
                if hole.hit_Green == False:
                    processUpAndDown(hole)
                processPutts(hole)
                processScore(hole)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"runde_{timestamp}.json"

            holes_dict_list = [hole.__dict__ for hole in holes_list]
            with open(filename, "w") as outfile:
                json.dump(holes_dict_list, outfile, indent=4)
            print(f"Runde gespeichert unter {filename}.\n")

        elif menu_nmbr == 2:
            show_saved_rounds()

        elif menu_nmbr == 3:
            stats_nmbr = int(input("""Was möchtest du tun: 
            (1) alte Rundenstatistik anzeigen
            """))
            if stats_nmbr == 1:
                show_saved_rounds()
                calculate_round_stats()

        elif menu_nmbr == 4:
            print("Programm wird beendet.")
        break  # Hier beenden
    # WICHTIG: Wird nur ausgeführt, wenn das Skript direkt gestartet wird
if __name__ == "__main__":
    main()