from guizero import App, PushButton, Box, Text

app = App(title="Trụ đèn giao thông", width=200, height=350)

box = Box(app, layout="grid")

state = "Đỏ" 
countdown = 10 #thêm biến này để đếm ngược mỗi lần đổi đèn

def change_light():
    global state, countdown
    countdown = 10 #reset countdown mỗi lần change light
    if state == "Đỏ":
        state = "Vàng"
        red.bg = "gray"
        yellow.bg = "yellow"
        green.bg = "gray"
    elif state == "Vàng":
        state = "Xanh"
        red.bg = "gray"
        yellow.bg = "gray"
        green.bg = "green"
    else:
        state = "Đỏ"
        red.bg = "red"
        yellow.bg = "gray"
        green.bg = "gray"

red = PushButton(box, text="", grid=[0,0], width=8, height=3)
yellow = PushButton(box, text="", grid=[0,1], width=8, height=3)
green = PushButton(box, text="", grid=[0,2], width=8, height=3)
button = PushButton(app, text="Chuyển đèn", command=change_light)

red.bg = "red"
yellow.bg = "gray"
green.bg = "gray"
countdown_text = Text(app,f"Chuyển sau: {countdown}s")

def countdown_timer(): #hàm này để kích hoạt chức năng đếm ngược
    global countdown
    if countdown > 0:
        countdown_text.value = f"Chuyển sau: {countdown}s"
        countdown -= 1
        app.after(1000, countdown_timer) #sử dụng app.after để gọi lại hàm này 1 giây 1 lần
    else:
        change_light()
        countdown_timer()  # bắt đầu đếm ngược lại

change_light() # Gọi change light lúc bắt đầu
countdown_timer() # bắt đầu đếm ngược

app.display()