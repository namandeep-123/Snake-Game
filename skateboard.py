from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 20, "normal")
FONT_GAME_OVER = ("arial", 50, "normal")
FINAL_SCORE_FONT = ("arial", 10, "normal")


class Skateboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_increase()

    def high_Score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_sores()

    def update_sores(self):
        self.goto(0, 260)
        self.clear()
        self.write(f"Score: {self.score} High score : {self.high_score}", True, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", True, align=ALIGNMENT, font=FONT_GAME_OVER)
    #     self.final_score()

    # def final_score(self):
    #     self.goto(0, -60)
    #     self.write(f" Your Final Score = {self.score -1}", True, align=ALIGNMENT, font=FINAL_SCORE_FONT)

    def score_increase(self):
        self.clear()
        self.score += 1
        self.update_sores()
