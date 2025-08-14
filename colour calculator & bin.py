'''x=10
y=8
print(bin(x))
print(bin(y))
print(bin(x&y),x&y)
print(bin(x|y),x|y)'''

import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("🎨 Colored Calculator")
root.geometry("300x400")
root.configure(bg="#222831")

entry = tk.Entry(root, font="Arial 20", bg="#eeeeee", fg="#222831", bd=10, relief=tk.FLAT, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

button_frame = tk.Frame(root, bg="#393e46")
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

colors = {
    "C": "#ff5722",
    "=": "#00adb5",
    "+": "#00adb5",
    "-": "#00adb5",
    "*": "#00adb5",
    "/": "#00adb5"
}

for row in buttons:
    frame = tk.Frame(button_frame, bg="#393e46")
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn_color = colors.get(btn_text, "#eeeeee")
        btn = tk.Button(frame, text=btn_text, font="Arial 18", bg=btn_color, fg="#222831", relief=tk.FLAT)
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()

