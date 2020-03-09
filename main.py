import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import  Figure

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ('Times New Roman', 12)
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default='icon.ico')
        tk.Tk.wm_title(self, 'Amazing.! Title')
        # tk.Tk.iconphoto(self, False, tk.PhotoImage('icon.png'))

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        for f in (StartPage, PageOne, PageTwo, PageThree):
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
        label = ttk.Label(self, text='Start Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text='next', command=lambda: controller.show_grid(PageOne))
        button1.pack()
        button2 = ttk.Button(self, text='last', command=lambda: controller.show_grid(PageTwo))
        button2.pack()
        button3 = ttk.Button(self, text='Graph Page', command=lambda: controller.show_grid(PageThree))
        button3.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='PageOne', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text='back', command=lambda: controller.show_grid(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text='next', command=lambda: controller.show_grid(PageTwo))
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

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Graph Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text='Go Home', command=lambda: controller.show_grid(StartPage))
        button1.pack()

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        a.plot([1,2,3,4,5,6,7,8], [5,3,2,6,8,4,2,1])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)







app = SeaofBTCapp()
app.mainloop()