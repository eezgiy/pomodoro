from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
counter = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text ="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")

    global counter
    counter = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global counter
    counter += 1

    if counter % 8 == 0:
        timer_label.config(text = "LONG BREAK")
        count_down(LONG_BREAK_MIN * 60)

    elif counter != 0 and counter % 2 == 0:
        timer_label.config(text = "SHORT BREAK")
        count_down(SHORT_BREAK_MIN * 60)
    
    else: 
        timer_label.config(text = "STUDY TIME")
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_minute = math.floor(count / 60)
    count_second = count % 60

    if count_second < 10:
        count_second =f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")

    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)

    else:
        start_timer()

        mark=""
        work_sessions = math.floor(counter/2)

        for _ in range (work_sessions):
            mark += "✔"
        
        check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)



canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)

timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)


timer_label = Label(text="Timer",fg=GREEN,bg=YELLOW,highlightthickness=0,font=(FONT_NAME,30,"bold"))
timer_label.grid(row=0,column=1)

check_label = Label(fg=GREEN,bg=YELLOW,highlightthickness=0,font=(FONT_NAME,15,"bold"))
check_label.grid(row=3,column=1)

start_button = Button(text="Start",bg="white",command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",bg="white",command=reset_timer)
reset_button.grid(row=2,column=2)

window.mainloop()