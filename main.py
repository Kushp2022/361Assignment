import tkinter as tk
from tkinter import messagebox
import random

# List of motivational quotes
QUOTES = [
    "You are doing great. Keep it up!",
    "Stay focused and never give up.",
    "Progress, not perfection.",
    "Your hard work will pay off.",
    "One Pomodoro at a time!"
]

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Productivity App")
        self.timer_running = False
        self.time_left = 25 * 60  # 25 minutes

        # Timer Label
        self.timer_label = tk.Label(root, text="1:00", font=("Helvetica", 48))
        self.timer_label.pack(pady=10)

        # Start Button
        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.pack(pady=5)

        # Note Entry
        self.note_label = tk.Label(root, text="Session Notes:", font=("Helvetica", 12))
        self.note_label.pack()
        self.note_entry = tk.Text(root, height=4, width=40)
        self.note_entry.pack()

        # Submit Notes Button
        self.submit_button = tk.Button(root, text="Save Note", command=self.save_note)
        self.submit_button.pack(pady=5)

        # Quote Label
        self.quote_label = tk.Label(root, text="", font=("Helvetica", 10), fg="green")
        self.quote_label.pack(pady=10)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.countdown()

    def countdown(self):
        if self.time_left > 0:
            minutes, seconds = divmod(self.time_left, 60)
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
            self.time_left -= 1
            self.root.after(1000, self.countdown)
        else:
            self.timer_label.config(text="Time's up!")
            self.timer_running = False
            self.show_quote()

    def save_note(self):
        note = self.note_entry.get("1.0", tk.END).strip()
        if note:
            with open("session_notes.txt", "a") as file:
                file.write(f"{note}\n{'-'*40}\n")
            messagebox.showinfo("Saved", "Your session note has been saved.")
            self.note_entry.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Empty", "Please write a note before saving.")

    def show_quote(self):
        quote = random.choice(QUOTES)
        self.quote_label.config(text=f"✨ {quote}")

# Run the app
root = tk.Tk()
app = PomodoroApp(root)
root.mainloop()
