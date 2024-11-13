import pyxel

class Player():
    def __init__(self, keyUp, keyDown, x) -> None:
        #Init player position dimensions et controls
        self.x = x
        self.y = 50
        self.w = 3
        self.h = 20
        self.keyUp = keyUp
        self.keyDown = keyDown
        self.speed = 0

    def draw(self):
        # Dessine un joueur
        pyxel.rect(self.x, self.y, self.w, self.h, 7)

    def update(self):
        # Update player position quand une touche est pressée
        if pyxel.btn(self.keyUp):
            self.y -= 1.5
        if pyxel.btn(self.keyDown):
            self.y += 1.5

        # Garde notre joueur sur l'ecran
        if self.y < 0:
            self.y = 0
        if self.y > 120 - self.h:
            self.y = 120 - self.h

    def reset(self): 
        # Reset la position
        self.y = 50
