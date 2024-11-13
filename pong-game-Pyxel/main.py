import pyxel
import ball
import player
import hud

class App():
    def __init__(self) -> None:
        pyxel.init(160, 120,"Pong", fps=60)
        self.ball = ball.Ball()
        self.player1 = player.Player(pyxel.KEY_W, pyxel.KEY_S, 0)
        self.player2 = player.Player(pyxel.KEY_UP, pyxel.KEY_DOWN, 157)
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
            # Verfifie si ya un point et un gagnant
            self.check_out_of_bounds()
            self.check_winner()
            if self.game_over:
                # Reset game Si espace et partie over
                if pyxel.btnp(pyxel.KEY_SPACE):
                    self.reset_game()
            # Update ball position
            self.ball.update()
            # Affiche score
            hud.show_score(self.score[0], self.score[1])
        else:
            # Affiche "Press SPACE to play" quand c'est pause
            hud.press_to_play()

    def draw(self):
        # Vide l'ecran 
        pyxel.cls(0)
        # Dessine la ball et les players
        self.ball.draw()
        self.player1.draw()
        self.player2.draw()
        # Verifie les collision entre joueur et ball 
        self.detect_collision()
        # Display score
        pyxel.text(50, 0, f"Score: {self.score}", 7)
        # Affiche le message de game over
        if self.game_over:
            if self.score[0] == 5:
                pyxel.text(55, 55, "Player 1 Wins", 8)
            else:
                pyxel.text(45, 40, "Player 2 Wins", 8)
            hud.game_over()

        # Affiche le pessage de pause
        if self.pause and not self.game_over:
            hud.press_to_play()

    def detect_collision(self):
        # Detecte les collsiison entre le joueur 1 et la balle 
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
        # Verifie si ya un gagnant
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
