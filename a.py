import compile
from tkinter import *


def start():
    file = open('code.dscr', 'w')
    file.write(entry.get('1.0', 'end-1c'))
    file.close()
    compile.run(open('code.dscr', 'r'))


window = Tk()
window.geometry('800x600')
window.title('DSCR')

entry = Text(window)
entry.place(x=0, y=25, width=800, height=575)

run = Button(window, text='>', command=start)
run.place(x=775, y=0, width=25, height=25)

window.mainloop()
