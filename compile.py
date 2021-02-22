from tkinter import *

window = Tk()
window.geometry('800x600')
window.title('Shell')

variables = {}
error, line_num = 0, 1
window_line = 0.5

if_in = ''


def check_var(string):
    return variables[string.strip('[]')] if string.startswith('[') and string.endswith(']') else string


def eval_condition(line):
    if line[1] == 'equals':
        return check_var(line[0]) == check_var(line[2])
    elif ' '.join(line[1:3]) == 'not equals':
        return check_var(line[0]) != check_var(line[3])


def return_error(line):
    global variables, error, line_num, window_line

    error_text = Label(window, text=f'Error in Line {line_num}:', fg='red')
    error_text.place(x=0, y=window_line * 20, height=20)
    window_line += 1

    error_line = Label(window, text=" ".join(line), fg='red')
    error_line.place(x=0, y=window_line * 20, height=20)
    window_line += 1

    error = 1


def run(code):
    global variables, error, line_num, window_line, if_in
    current_condition = []

    with code as file:
        for line in file:
            try:
                line = line.strip().split()
                if ''.join(line) == '' or len(line) != 0 and line[0].startswith('#'):
                    continue
                elif 'if' == line[0]:
                    if_in = 'if'
                    current_condition = line[1:]
                    continue
                elif 'end' == ''.join(line):
                    if if_in == '':
                        return_error(line)
                        break
                    else:
                        if_in = ''
                if if_in == '' or if_in == 'if' and eval_condition(current_condition):
                    if 'equals' in line:
                        variables[line[0]] = line[2]
                    elif line[0] == 'say':
                        text = Label(window, text=[check_var(i) for i in line[1:]])
                        text.place(x=0, y=window_line * 20, height=20)
                        window_line += 1
            except Exception as e:
                return_error(line)
                break
            line_num += 1

    done = Label(window, text=f'Exit Code {error}')
    done.place(x=0, y=window_line * 20, height=20)
    window_line += 2
