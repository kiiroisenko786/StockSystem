from tkinter import *
import pandas as pd

# Indices as dataframe, Sheet 1 is main sheet, Sheet 2 has 5 for testing
indices = pd.read_excel('tickers2.xlsx', sheet_name='Sheet 1')

# Tickers is a list of symbols as strings from the 'Symbol' column
# of the dataframe 'indices'
tickers = sorted(indices['Symbol'])
timeFrames = ['HOURLY', 'DAILY', 'WEEKLY']

setTickers = ['', '', '', '', '']
stockRotations = [
     ['', ''],
     ['', ''],
     ['', ''],
     ['', ''],
     ['', '']
]

root = Tk()
root.title("Simple Stock Signal System")
root.geometry("750x720")
root.resizable(False, False)

clicked1   = StringVar(root)
clicked2   = StringVar(root)
clicked3   = StringVar(root)
clicked4   = StringVar(root)
clicked5   = StringVar(root)
timeFrame1 = StringVar(root)

def callback1(*args):
     pass

clicked1.set(tickers[0])
setTickers[0] = clicked1.get()
stockRotations[0][0] = clicked1.get()
clicked1.trace("w", callback1)
timeFrame1.set(timeFrames[0])

clicked2.set(tickers[1])
setTickers[1] = clicked2.get()
stockRotations[1][0] = clicked2.get()
print(setTickers)
# clicked2.trace("w", callback1)
clicked3.set(tickers[2])
clicked4.set(tickers[3])
clicked5.set(tickers[4])


drop1 = OptionMenu(root, clicked1, *tickers)
drop1.config(width=22, bg="green", foreground="white")
drop1.place(x=0, y=0)

button1 = Button(root, text="Get chart")
button1.columnconfigure(0, weight=0)
button1.place(x=0, y=35)

dropTf1 = OptionMenu(root, timeFrame1, *timeFrames)
dropTf1.config(width=10, bg="blue", foreground="white")
dropTf1.place(x=72, y=32)

drop2 = OptionMenu(root, clicked2, *tickers)
drop2.config(width=20, bg="green", foreground="white")
drop2.place(x=0, y=80)

button2 = Button(root, text="Get chart")
button2.columnconfigure(0, weight=0)
button2.place(x=0, y=110)

# drop3 = OptionMenu(root, clicked3, *listOfIndices)
# drop3.config(width=20, bg="green", foreground="white")
# drop3.grid(row=4, column=0)
# button3 = Button(root, text="Get chart")
# button3.columnconfigure(0, weight=0)
# button3.grid(row=5, column=0, sticky=W)

# drop4 = OptionMenu(root, clicked4, *listOfIndices)
# drop4.config(width=20, bg="green", foreground="white")
# drop4.grid(row=6, column=0)
# button4 = Button(root, text="Get chart")
# button4.columnconfigure(0, weight=0)
# button4.grid(row=7, column=0, sticky=W)

# drop5 = OptionMenu(root, clicked5, *listOfIndices)
# drop5.config(width=20, bg="green", foreground="white")
# drop5.grid(row=8, column=0)
# button5 = Button(root, text="Get chart")
# button5.columnconfigure(0, weight=0)
# button5.grid(row=9, column=0, sticky=W)



# exitButton = Button(root, text="Exit", command=root.destroy)
# exitButton.config(width=10, bg="red", foreground="white")
# exitButton.columnconfigure(0, weight=0)
# exitButton.grid(row=10, column=10, sticky=S+E)
# drop.pack()


mainloop()