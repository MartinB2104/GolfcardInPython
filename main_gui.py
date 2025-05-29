import tkinter as tk
from tkinter import messagebox

from datetime import datetime
from core.holes import get_default_holes
from core.inputs import *
from core.file_io import save_round
from stats.stats import calculate_round_stats
from ui.display import show_saved_rounds, display_hole_info

def play_round_gui():
    try:
        holes = get_default_holes()
        score_bisher = 0
        for hole in holes:
            display_hole_info(hole, score_bisher)
            processFairway(hole)
            processGreenHit(hole)
            if not hole.hit_Green:
                processUpAndDown(hole)
            processPutts(hole)
            processScore(hole)

            score_bisher += hole.score - hole.par

        file_name = f"runde_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
        save_round(holes, file_name)
        messagebox.showinfo(f"Runde gespeichert unter {file_name}.\n")
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Speichern der Runde: {e}")

def show_saved_rounds_gui():
    try:
        show_saved_rounds()
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Anzeigen der gespeicherten Runde: {e}")

def stats_gui():
    try:
        calculate_round_stats()
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Berechnen der Statistiken: {e}")

#GUI setup
root = tk.Tk()
root.title("Golf card")
root.geometry("1000x600")

tk.Label(root, text="Golf card Menü")

tk.Button(root, text="Neue Runde", command=play_round_gui).pack()
tk.Button(root, text="Alte Runde einsehen", command=show_saved_rounds_gui).pack()
tk.Button(root, text="Statistiken zu einer Runde", command=stats_gui).pack()
tk.Button(root, text="Beenden", command=root.quit).pack()


root.mainloop()