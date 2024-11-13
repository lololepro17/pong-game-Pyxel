import pyxel

#------ import de ball 
from random import randint
class Ball:
    def __init__(self) -> None:
        # Initialize ball position and speed
        self.x = 80
        self.y = 60
        self.speedX = -1.0 if randint(0, 1) == 0 else 1.0
        self.speedY = -1.5 if randint(0, 1) == 0 else 1.5
        self.r = 2
        self.out_of_bounds = False

    def draw(self):
        # Dessine ball
        pyxel.circ(self.x, self.y, self.r, 7)

    def update(self):
        # Update ball position
        self.x += self.speedX
        self.y += self.speedY
        
        # Difference de vitesse en fonction de ou on tape
        if self.y < 0 or self.y > 120:
            self.speedY *= -1
        
    
    def reset(self):
        # Reset ball position et speed
        self.x = 80
        self.y = 60
        self.speedX = -1.0 if randint(0, 1) == 0 else 1.0
        self.speedY = -1.5 if randint(0, 1) == 0 else 1.5
        self.out_of_bounds = False

#------ import de ball 
#------ import de player
class Player():
    def __init__(self, keyUp, keyDown, x) -> None:
        #Init player position dimensions et control
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

        # Garde notre joueur sur l’écran
        if self.y < 0:
            self.y = 0
        if self.y > 120 - self.h:
            self.y = 120 - self.h

    def reset(self): 
        # Reset la position
        self.y = 50

#------import de player
#------import de hud
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

#------import de hud

class App():
    def __init__(self) -> None:
        pyxel.init(160, 120,"Pong", fps=60)
        self.ball = Ball()
        self.player1 = Player(pyxel.KEY_W, pyxel.KEY_S, 0)
        self.player2 = Player(pyxel.KEY_UP, pyxel.KEY_DOWN, 157)
        self.score = [0, 0]
        self.game_over = False
        self.pause = True
        pyxel.run(self.update, self.draw)

    def update(self):
        # Mets en pause si on presse espace
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.pause = not self.pause

        if not self.pause:
            # Mise a jour des position
            self.player1.update()
            self.player2.update()
            # Vérifié si ya un point et un gagnant
            self.check_out_of_bounds()
            self.check_winner()
            if self.game_over:
                # Reset game Si espace et partie over
                if pyxel.btnp(pyxel.KEY_SPACE):
                    self.reset_game()
            # Update ball position
            self.ball.update()
            # Affiche score
            show_score(self.score[0], self.score[1])
        else:
            # Affiche "Press SPACE to play" quand c'est pause
            press_to_play()

    def draw(self):
        # Vide l’écran 
        pyxel.cls(0)
        # Dessine la ball et les player
        self.ball.draw()
        self.player1.draw()
        self.player2.draw()
        # Vérifie les collision entre joueur et ball 
        self.detect_collision()
        # Display score
        pyxel.text(50, 0, f"Score: {self.score}", 7)
        # Affiche le message de game over
        if self.game_over:
            if self.score[0] == 5:
                pyxel.text(55, 55, "Player 1 Wins", 8)
            else:
                pyxel.text(45, 40, "Player 2 Wins", 8)
            game_over()

        # Affiche le message de pause
        if self.pause and not self.game_over:
            press_to_play()

    def detect_collision(self):
        # Détecte les collision entre le joueur 1 et la balle 
        if self.ball.x > self.player1.x and self.ball.x < self.player1.x + self.player1.w:
            if self.ball.y > self.player1.y and self.ball.y < self.player1.y + self.player1.h:
                self.ball.speedX *= -1.2

        # Même chose avec le joueur 2
        if self.ball.x > self.player2.x and self.ball.x < self.player2.x + self.player2.w:
            if self.ball.y > self.player2.y and self.ball.y < self.player2.y + self.player2.h:
                self.ball.speedX *= -1.2

    def check_out_of_bounds(self):
        # Garde la ball dans le jeu 
        if self.ball.x < 0:
            self.ball.out_of_bounds = True
            self.ball.reset()
            self.player1.reset()
            self.player2.reset()
            self.score[1] += 1
            self.pause = True
        if self.ball.x > 160:
            self.ball.out_of_bounds = True
            self.ball.reset()
            self.player1.reset()
            self.player2.reset()
            self.score[0] += 1
            self.pause = True
        return self.ball.out_of_bounds

    def check_winner(self):
        # Vérifie si ya un gagnant
        if self.score[0] == 5 or self.score[1] == 5:
            self.game_over = True
            self.pause = True
            return True
        return False
    
    def reset_game(self):
        # Reset game
        self.score = [0, 0]
        self.game_over = False
        self.pause = True
        self.ball.reset()
        self.player1.reset()
        self.player2.reset()
 
                
if __name__ == "__main__":
    App()
