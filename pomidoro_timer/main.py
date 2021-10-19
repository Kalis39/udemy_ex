from tkinter import *


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.1
reps = 0
num_ticks = 0
timer = None

def reset_timer():
    global reps
    global num_ticks
    num_ticks = 0
    reps = 0
    timer_label.config(text="Timer")
    tick_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)

def start_timer():
    global reps
    reps += 1
    if reps > 8:
        return
    if reps in range(1, 8, 2):
        count_down(WORK_MIN * 60)
        timer_label.config(text="WORK", fg=GREEN)
    elif reps in range(2, 8, 2):
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=PINK)
    else:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=RED)

def count_down(count):
    global timer

    count_min = int(count / 60)
    count_sec = int(count % 60)

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global num_ticks
        if reps in range(3, 10, 2):
            num_ticks += 1
            tick_label.config(text=num_ticks * "✓")

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer,highlightthickness=0)
reset_button.grid(column=2, row=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

tick_label = Label(font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
