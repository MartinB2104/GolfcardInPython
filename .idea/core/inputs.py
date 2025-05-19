def processFairway(hole):
    while True:
        val = input("Hast du das Fairway getroffen? (True/False): ").strip().lower()
        if val in ["true", "false"]:
            hole.hit_Fairway = val == "true"
            break
        print("Ungültige Eingabe.")

def processGreenHit(hole):
    while True:
        val = input("Hast du das Grün in regulation getroffen? (True/False): ").strip().lower()
        if val in ["true", "false"]:
            hole.hit_Green = val == "true"
            break
        print("Ungültige Eingabe.")

def processBunkershot(hole):
    val = input("Hattest du ein Bunkerschlag? (True/False): ").strip().lower()
    if val == "true":
        hole.had_Bunkershot = True
        val2 = input("Hast du das bunker up and down gemacht? (True/False): ").strip().lower()
        hole.made_Bunkershot = val2 == "true"
    else:
        hole.had_Bunkershot = False
        hole.made_Bunkershot = False

def processUpAndDown(hole):
    val = input("Hattest du ein Up and Down? (True/False): ").strip().lower()
    if val == "true":
        hole.had_UpAndDown = True
        val2 = input("Hast du dein Up and Down gemacht? (True/False): ").strip().lower()
        hole.made_UpAndDown = val2 == "true"
        processBunkershot(hole)
    else:
        hole.had_UpAndDown = False

def processPutts(hole):
    while True:
        try:
            hole.putts = int(input("Wie viele Putts hast du gemacht? "))
            if hole.putts > 0:
                break
        except ValueError:
            pass
        print("Bitte eine gültige Zahl eingeben.")

def processScore(hole):
    while True:
        try:
            hole.score = int(input("Wie war dein Score? "))
            if hole.score > 0:
                break
        except ValueError:
            pass
        print("Bitte eine gültige Zahl eingeben.")