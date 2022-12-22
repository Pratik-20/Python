from tkinter import *


root = Tk()
root.title("String Reverser")
root.geometry("700x400")
root.config(background="#dae6f6")


def string_reverser():
    word = enter_text.get()
    a = word[::-1]
    right = str(a)

    cs = Label(root, text="Reversed String is:", font=("poppins", 20), bg="#dae6f6", fg="#364971")
    cs.place(x=100, y=250)
    spell.config(text=right)


heading = Label(root, text="String Reverser", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50, 0))

enter_text = Entry(root, justify="center", width=30, font=("poppins", 25), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

button = Button(root, text="Check", font=("arial", 20, "bold"), fg="white", bg="red", command=string_reverser)
button.pack()

spell = Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971")
spell.place(x=350, y=250)

root.mainloop()
