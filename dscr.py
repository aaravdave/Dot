import compile, os
from tkinter import *


def start():
    file = open(f'files/{variable.get()}.dscr', 'w')
    file.write(entry.get('1.0', 'end-1c'))
    file.close()
    compile.run(open('files/code.dscr', 'r'))


window = Tk()
window.geometry('800x600')
window.title('DSCR')

entry = Text(window)
entry.place(x=20, y=25, width=800, height=575)
line_numbers = Text(window, state=DISABLED)
line_numbers.place(x=0, y=25, width=20, height=575)

run = Button(window, text='>', command=start)
run.place(x=775, y=0, width=25, height=25)

options = sorted([i.split('.')[0] for i in os.listdir('files')])

variable = StringVar(window)
variable.set(options[0])

choose_file = OptionMenu(window, variable, *options)
choose_file.place(x=675, y=0, width=100, height=25)

while True:
    line_numbers.configure(state=NORMAL)
    line_numbers.delete('1.0', END)
    line_numbers.insert(END, '\n'.join(str(i + 1) for i in range(entry.get('1.0', END).count('\n'))))
    line_numbers.configure(state=DISABLED)
    window.update()
