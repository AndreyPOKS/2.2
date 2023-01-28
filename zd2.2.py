import tkinter as tk





win = tk.Tk()
win.config()
win.title("Автобус/POKS44b")
win.geometry("1000x600+100+200")
win.resizable(False, False)
pole1 = tk.Entry(win, )
lbl1 = tk.Label(win, text="скорость").grid(row=1, column=0)
pole1.grid(row=0, column=0)
pole2 = tk.Entry(win, )
lbl2 = tk.Label(win, text="макс.кол-во").grid(row=1, column=1)
pole2.grid(row=0, column=1)
pole3 = tk.Entry(win, )
lbl3 = tk.Label(win, text=" макс.скорость").grid(row=1, column=2)
pole3.grid(row=0, column=2)
pole4 = tk.Entry(win, )
lbl4 = tk.Label(win, text="кол-во пасс").grid(row=1, column=3)
pole4.grid(row=0, column=3)
pole5 = tk.Entry(win, )
lbl5 = tk.Label(win, text="свобод.мест").grid(row=1, column=4)
pole5.grid(row=0, column=4)
pole6 = tk.Entry(win, )
lbl1 = tk.Label(win, text="места").grid(row=1, column=5)
pole6.grid(row=0, column=5)
pole7 = tk.Entry(win, )
lbl1 = tk.Label(win, text="фамилии").grid(row=1, column=6, columnspan=2)
pole7.grid(row=0, column=6)
btkfam1 = tk.Button(win, text="+")
btkfam3 = tk.Label(win, text="или")
btkfam2 = tk.Button(win, text="-")
btkfam1.grid(row=2, column=6, sticky="W")
btkfam3.grid(row=2, column=6,)
btkfam2.grid(row=2, column=6, sticky="E")
btk1 = tk.Button(win, text="Начать",)
btk1.grid(row=0, column=7)





win.mainloop()
