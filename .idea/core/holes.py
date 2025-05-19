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

def get_default_holes():
    return [
        Holes("Bahn 1", 495, 5, 0, False, False, False, False, False, False),
        Holes("Bahn 2", 159, 3, 0, False, False, False, False, False, False),
        Holes("Bahn 3", 363, 4, 0, False, False, False, False, False, False),
        Holes("Bahn 4", 458, 5, 0, False, False, False, False, False, False),
        Holes("Bahn 5", 140, 3, 0, False, False, False, False, False, False),
        Holes("Bahn 6", 455, 5, 0, False, False, False, False, False, False),
        Holes("Bahn 7", 370, 4, 0, False, False, False, False, False, False),
        Holes("Bahn 8", 99, 3, 0, False, False, False, False, False, False),
        Holes("Bahn 9", 360, 4, 0, False, False, False, False, False, False),
    ]