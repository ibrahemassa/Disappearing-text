from tkinter import *

stopped = 0


def on_text_change(event):
    text.config(height=max(2, text.get("1.0", END).count('\n') + 1))


def check_input():
    global stopped
    current_text = text.get("1.0", END)
    if current_text == check_input.previous_text:
        stopped += 1
        if stopped >= 5:
            restart()
    else:
        stopped = 0
    check_input.previous_text = current_text
    root.after(1000, check_input)


def restart():
    text.delete("1.0", END)


root = Tk()
root.title('Dangerous writing!')
root.minsize(800, 500)

label = Label(text='If you stop writing for 5 seconds your text will get deleted!!!',
              font=('Helvetica', 20),
              fg='DarkRed')
label.pack()

text = Text(root, borderwidth=1, font=('Helvetica', 16))
text.pack(fill=BOTH, expand=True)
text.bind("<KeyRelease>", on_text_change)

check_input.previous_text = text.get("1.0", END)

check_input()

root.mainloop()
