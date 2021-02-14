from tkinter import *


def run(code):
    window = Tk()
    window.geometry('800x600')
    window.title('Shell')

    variables = {}
    error, line_num = 0, 1
    window_line = 0.5

    with code as file:
        for line in file:
            try:
                line = line.strip().split()
                if ''.join(line) == '':
                    continue
                elif line[0].startswith('#'):
                    continue
                elif 'equals' in line:
                    variables[line[0]] = line[2]
                elif line[0] == 'say':
                    error_text = Label(window, text=[variables[i.strip('[]')] if i.startswith('[') and i.endswith(']') else i for i in line[1:]])
                    error_text.place(x=0, y=window_line * 20, height=20)
                    window_line += 1
            except Exception:
                error_text = Label(window, text=f'Error in Line {line_num}:', fg='red')
                error_text.place(x=0, y=window_line * 20, height=20)
                window_line += 1

                error_line = Label(window, text=" ".join(line), fg='red')
                error_line.place(x=0, y=window_line * 20, height=20)
                window_line += 1

                error = 1
                break

    done = Label(window, text=f'Exit Code {error}')
    done.place(x=0, y=window_line * 20, height=20)
    window_line += 1
