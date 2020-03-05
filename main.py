import tkinter as tk

LARGE_FONT = ('Verdana', 12)
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side='top', fill='both', expand=True)

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky='nsew')
        self.show_grid(StartPage)

    def show_grid(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def qf(x):
    print(x)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Start Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text='click here', command=lambda: qf('hello'))
        button1.pack()

app = SeaofBTCapp()
app.mainloop()