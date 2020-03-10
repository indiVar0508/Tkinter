import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# from matplotlib.figure import  Figure
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

# from pandas.plotting import register_matplotlib_converters
# register_matplotlib_converters()

import urllib
import json

import pandas as pd
import numpy as np

import tkinter as tk
from tkinter import ttk

f = plt.figure()
# a = f.add_subplot(111)

LARGE_FONT = ('Times New Roman', 12)
NORM_FONT = ('Times New Roman', 10)
SMALL_FONT = ('Times New Roman', 8)
style.use('ggplot')
t = 1
a = plt.subplot2grid((6,4), (0, 0), rowspan=5, colspan=4)
# a1 = plt.subplot2grid((6,4), (4, 0), rowspan=1, colspan=4, sharex=a)
a2 = plt.subplot2grid((6,4), (5, 0), rowspan=1, colspan=4, sharex=a)

dataLink = 'https://pythonprogramming.net/yahoo_finance_replacement'
dataset = urllib.request.urlopen(dataLink).read().decode()
dataset = dataset.split('\n')
dataset = list(map(lambda x: x.split(','), dataset))
dataset = pd.DataFrame(dataset)
len = dataset.shape[0]
dataset.columns = dataset.loc[0]

def saySomething():
    pop = tk.Tk()
    label = ttk.Label(pop, text='Say Something : ')
    label.pack(side='left', padx=5, pady=5, fill='x')
    e = tk.Entry(pop)
    e.insert(0, 'Nice')
    e.pack(fill='x', padx=5, pady=5)
    e.focus_set()

    def callback():
        value = e.get()
        print(value)
        pop.destroy()

    b = ttk.Button(pop, text='Submit', command=callback)
    b.pack()
    pop.mainloop()

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title('!')
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side='top', fill='x', pady=10)
    B1 = ttk.Button(popup, text='okay', command = popup.destroy)
    B1.pack()
    popup.mainloop()


def animate(i):
    global t
    # filedata = open("sampleData.txt", 'r').read()
    # dataList = filedata.split('\n')
    # xlist, ylist = [], []
    # for eachLine in dataList:
    #     if len(eachLine) > 1:
    #         x, y = eachLine.split(',')
    #         xlist.append(int(x))
    #         ylist.append(int(y))
    # a.clear()
    # a.plot(xlist, ylist, 'b', label='some')
    # a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
    # a.set_title('Graph')




    data = dataset[t:t+200]
    data.loc[:, 'High'] = data['High'].astype(float)
    data.loc[:, 'Low'] = data['Low'].astype(float)
    data.loc[:, 'Volume'] = data['Volume'].astype(float)
    t=(t+10)%len
    data.loc[:, 'Date'] = pd.to_datetime(data['Date'])
    data.loc[:, 'Date'] = data['Date'].apply(lambda x: mdates.date2num(x.to_pydatetime()))
    a.clear()
    a2.clear()
    a.plot(data['Date'], data['High'], 'g', label='High')
    a.plot(data['Date'], data['Low'], 'r', label='Low')
    a2.fill_between(data['Date'], 0, data['Volume'], facecolor='#183A53')


    a.legend(bbox_to_anchor=(0, 1.02, 1, 0.102), loc=3, ncol=2, borderaxespad=0)
    a.set_title('Graph')
    a.xaxis.set_major_locator(mticker.MaxNLocator(5))
    a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    plt.setp(a.get_xticklabels(), visible=False)
    # a.set_yticks([v for v in range(data.Lowastype(int).min(), data.High.astype(int).max(), 50)])



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

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='save setting', command=lambda: popupmsg('Not Supported.!'))
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=quit)
        menubar.add_cascade(label='file', menu=filemenu)

        suggest = tk.Menu(menubar, tearoff=1)
        suggest.add_command(label='Say Something', command=saySomething)
        menubar.add_cascade(label='Suggest', menu=suggest)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}
        for f in (StartPage, BTCe_page):
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
        label = ttk.Label(self, text='Not my Responsibility', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text='Agree', command=lambda: controller.show_grid(BTCe_page))
        button1.pack()
        button2 = ttk.Button(self, text='Disagree', command=quit)
        button2.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='PageOne', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text='back', command=lambda: controller.show_grid(StartPage))
        button1.pack()


class BTCe_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Graph Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text='Go Home', command=lambda: controller.show_grid(StartPage))
        button1.pack()

        # a.plot([1,2,3,4,5,6,7,8], [5,3,2,6,8,4,2,1])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = SeaofBTCapp()
app.geometry('1024x640')
ani = animation.FuncAnimation(f, animate, interval=1500, )
app.mainloop()