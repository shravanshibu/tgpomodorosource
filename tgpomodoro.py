from tkinter import *
import math
from winsound import PlaySound, SND_FILENAME

# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_canvas, text="00:00")
    main_label.config(text="Timer", bg="#4aa96c", font=(FONT_NAME, 25), fg=GREEN)
    tick_label.config(text="", bg="#4aa96c", font=(FONT_NAME, 25), fg=GREEN)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    reps += 1
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_min)
        main_label.config(text="Long Break", bg="#4aa96c", font=(FONT_NAME, 25), fg=PINK)
        PlaySound('Bell Sounds.wav', SND_FILENAME)
    elif reps % 2 == 0:
        count_down(short_break_min)
        main_label.config(text="Break", bg="#4aa96c", font=(FONT_NAME, 25), fg=YELLOW)
        PlaySound('Bell Sounds.wav', SND_FILENAME)
    else:
        count_down(work_min)
        main_label.config(text="Work", bg="#4aa96c", font=(FONT_NAME, 25), fg=GREEN)
        PlaySound('Bell Sounds.wav', SND_FILENAME)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_canvas, text=f"{count_minute}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        tick_label.config(text=mark, bg="#4aa96c", font=(FONT_NAME, 25), fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("The Promodora")
window.config(padx=100, pady=100, bg="#4aa96c")

main_label = Label(text="Timer", bg="#4aa96c", font=(FONT_NAME, 25), fg=GREEN)
main_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=223, bg="#4aa96c", highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_pic)
timer_canvas = canvas.create_text(103, 130, text="00:00", fill=YELLOW, font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

button_start = Button(text="Start", command=start)
button_start.grid(row=3, column=0)

tick_label = Label(bg="#4aa96c", fg=GREEN, font=(FONT_NAME, 25))
tick_label.grid(row=4, column=1)

button_reset = Button(text="Reset", command=reset)
button_reset.grid(row=3, column=2)

credit_label = Label(text="Credits : Tech Grab | techgrab.online | Websites - Mobile Apps - Software | +919947650110", bg="#4aa96c",
                     fg="#ffffff", font=(FONT_NAME, 8))
credit_label.grid(row=6, column=1)

mainloop()
