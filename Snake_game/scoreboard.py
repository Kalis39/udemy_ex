from turtle import Turtle
ALIGNMENT = "center"
FONT = ("ABBVoice", 16, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.ht()
        self.goto(0, 270)
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def new_score(self):
        self.score += 1
        self.update_score()
