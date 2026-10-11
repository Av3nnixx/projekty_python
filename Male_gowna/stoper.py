
#vibecode
import tkinter as tk

DURATION = 90  # czas w sekundach

# --- Kolory / design ---
BG_COLOR = "#1e1e2f"
CARD_COLOR = "#2a2a3d"
ACCENT_COLOR = "#4cd964"
ACCENT_COLOR_RUNNING = "#ff6b6b"
TEXT_COLOR = "#f5f5f5"
SUBTEXT_COLOR = "#9a9ab0"

running = False 
remaining = DURATION


def format_time(seconds):
    m = seconds // 60
    s = seconds % 60
    return f"{m:01d}:{s:02d}"


def tick():
    global remaining, running
    if remaining > 0 and running:
        remaining -= 1
        time_label.config(text=format_time(remaining))
        if remaining == 10:
            root.bell()
            time_label.config(fg=ACCENT_COLOR_RUNNING)
        root.after(1000, tick)
    else:
        running = False
        time_label.config(text="Gotowe!", fg=ACCENT_COLOR)
        status_label.config(text="Kliknij, aby zacząć ponownie")
        card.config(highlightbackground=ACCENT_COLOR)


def start_timer(event=None):
    global running, remaining
    if running:
        return
    running = True
    remaining = DURATION
    time_label.config(fg=TEXT_COLOR)
    status_label.config(text="Trwa odliczanie...")
    card.config(highlightbackground=ACCENT_COLOR_RUNNING)
    tick()


# --- Okno główne ---
root = tk.Tk()
root.title("Timer 55s")
root.geometry("340x420")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# --- Karta ---
card = tk.Frame(
    root,
    bg=CARD_COLOR,
    highlightthickness=3,
    highlightbackground=ACCENT_COLOR,
    bd=0,
)
card.place(relx=0.5, rely=0.5, anchor="center", width=280, height=340)

title_label = tk.Label(
    card,
    text="ODPOCZYNEK",
    font=("Helvetica", 14, "bold"),
    bg=CARD_COLOR,
    fg=SUBTEXT_COLOR,
)
title_label.pack(pady=(30, 5))

time_label = tk.Label(
    card,
    text=format_time(DURATION),
    font=("Helvetica", 52, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
)
time_label.pack(pady=10)

status_label = tk.Label(
    card,
    text="Kliknij przycisk, aby zacząć",
    font=("Helvetica", 10),
    bg=CARD_COLOR,
    fg=SUBTEXT_COLOR,
)
status_label.pack(pady=(0, 20))

start_button = tk.Button(
    card,
    text="START",
    font=("Helvetica", 14, "bold"),
    bg=ACCENT_COLOR,
    fg="#1e1e2f",
    activebackground="#3fb955",
    activeforeground="#1e1e2f",
    bd=0,
    relief="flat",
    padx=30,
    pady=12,
    cursor="hand2",
    command=start_timer,
)
start_button.pack(pady=10)

root.mainloop()