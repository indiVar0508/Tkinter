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
        for f in (StartPage, PageOne, PageTwo):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_grid(StartPage)

    def show_grid(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Start Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text='next', command=lambda: controller.show_grid(PageOne))
        button1.pack()
        button2 = tk.Button(self, text='last', command=lambda: controller.show_grid(PageTwo))
        button2.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='PageOne', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text='back', command=lambda: controller.show_grid(StartPage))
        button1.pack()
        button2 = tk.Button(self, text='next', command=lambda: controller.show_grid(PageTwo))
        button2.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='PageTwo', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text='Start', command=lambda: controller.show_grid(StartPage))
        button1.pack()
        button2 = tk.Button(self, text='Back', command=lambda: controller.show_grid(PageOne))
        button2.pack()

app = SeaofBTCapp()
app.mainloop()