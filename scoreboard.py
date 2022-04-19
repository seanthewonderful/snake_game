from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
    
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", move=False, align="center", font=("Typewriter", 24, "normal"))


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.new_highscore()
        self.score = 0
        self.update_scoreboard()
        
    
    def new_highscore(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.highscore}")
            
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align='center', font=('Typewriter', 30, 'normal'))


    def up_score(self):
        self.score += 1
        self.update_scoreboard()
