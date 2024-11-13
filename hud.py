import pyxel

def show_score(p1, p2):
    # Score joueur 1
    pyxel.text(80, 0, f"Player 1: {p1}", 7)

def counter(count):
    # Affiche le conteur
    pyxel.text(70, 0, f"Count: {count}", 7)

def game_over(): 
    # Affiche quand ta perdu
    pyxel.text(45, 55, "Game Over", 8)
    pyxel.text(45, 80, "Press Space to Replay", 8)

def press_to_play():
    # Affiche le message "press to play"
    pyxel.text(40, 55, "Press Space to Play", 8)
