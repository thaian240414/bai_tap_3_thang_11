from guizero import App, Box, Text

app = App(title="Điểm môn học", width=400, height=300)

box = Box(app, border=True, layout="grid")

box1 = Box(box, border=True, grid=[0,0,2,1])

title_text = Text(box1, text="Điểm môn học")

box2 = Box(box, border=True, grid=[0,1,2,1], layout="grid")

box3 = Box(box2, border=True, grid=[0,0], layout="grid")

text = Text(box3, text="Môn", grid=[0,0])

text1 = Text(box3, text="Toán", grid=[0,1])

text3 = Text(box3, text="Văn", grid=[0,2])

text4 = Text(box3, text="Anh", grid=[0,3])

box4 = Box(box2, border=True, grid=[1,0], layout="grid")

text5 = Text(box4, text="Điểm", grid=[0,0])

text6 = Text(box4, text="8", grid=[0,1])

text7 = Text(box4, text="9", grid=[0,2])

text8 = Text(box4, text="10", grid=[0,3])

box5= Box(box, border=True, grid=[0,2,2,1])

tb = (8 + 9 + 10) / 3

average_text = Text(box5, text=f"Điểm trung bình: {tb}")

app.display()
