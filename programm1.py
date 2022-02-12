import tkinter as name
ekran = name.Tk()
ekran.geometry('1920x1080')
FISH = "Saydullayev Sadriddin Sanjar O'g'li" 

msg = name.Message(ekran, text = FISH)
msg.config(bg = "red", fg = 'yellow', font = ('times', 32, 'bold'), width = 600, padx = 1920, pady = 1080)

msg.pack()

ekran.mainloop()