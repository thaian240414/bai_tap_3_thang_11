from guizero import App, Picture, PushButton, Text
from random import randint

app = App(title="Hộp quà Gacha", width=400, height=400)

text = Text(app, text="Chạm để mở hộp quà!!!(☆▽☆)", size=20, color="Blue")


pic = Picture(app, image="question.png", width=100, height=100)
result = Text(app, text="", size=16)

def mo_hop():
    n = randint(1, 100)
    if n <= 60:
        pic.image = "normal.png"
        result.value = "🎉Bạn nhận được: Normal"
        result.text_color = "blue"
    elif n <= 90:
        pic.image = "epic.png"
        result.value = "🎉Bạn nhận được: Epic"
        result.text_color = "purple"
    else:
        pic.image = "rare.png"
        result.value = "🎉Bạn nhận được: Rare"
        result.text_color = "gold"

nut = PushButton(app, text="MỞ HỘP", command=mo_hop)

app.display()
