import tkinter as tk

root = tk.Tk()
root.title("Tom & Jerry Chase")
root.geometry("700x300")
root.resizable(False, False)

canvas = tk.Canvas(root, width=700, height=300, bg="#78c257")
canvas.pack()

# Track details
canvas.create_rectangle(0, 200, 700, 300, fill="#5c3a21", width=0)
canvas.create_line(0, 200, 700, 200, fill="#ffffff", dash=(8, 8), width=3)

# Timer display
timer_text = canvas.create_text(350, 40, text="Time: 0.0s", font=("Arial", 16, "bold"), fill="white")

# Characters
tom = canvas.create_text(60, 160, text="🐱", font=("Segoe UI Emoji", 40))
jerry = canvas.create_text(320, 170, text="🐭🧀", font=("Segoe UI Emoji", 30))

frame = 0
total_frames = 200  # 200 steps * 50ms = 10.0 seconds

def update_chase():
    global frame
    frame += 1
    elapsed = frame * 0.05
    canvas.itemconfig(timer_text, text=f"Time: {elapsed:.1f}s / 10.0s")

    if frame < total_frames:
        canvas.move(tom, 2.7, 0)
        canvas.move(jerry, 1.4, 0)
        root.after(50, update_chase)
    else:
        canvas.delete(tom)
        canvas.delete(jerry)
        canvas.create_text(580, 160, text="💥 CAUGHT! 🐱🍽️", font=("Segoe UI Emoji", 34))
        canvas.itemconfig(timer_text, text="Time: 10.0s — Caught!", fill="#ffe600")

root.after(50, update_chase)
root.mainloop()