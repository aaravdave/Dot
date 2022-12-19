def parse(t):
    if t.startswith('"') and t.endswith('"'):
        t = t.strip('"')
    else:
        callback('TokenError', 'Token unable to be parsed.')
    return t


def add(c):
    if c[-1] == 'string':
        callback('SyntaxError', 'String not closed correctly.')
    compiled.append(c[1:])


def callback(e, m):
    quit(f'''Callback on {e}, line {linenum if linenum == 'unknown' else linenum + 1}
{token if linenum == 'unknown' else lines[linenum]}
Invalid syntax: {m}
''')


with open('main.dot') as file:
    lines = []
    for line in file:
        lines.append(line.strip())

compiled = []
linenum = 0
for line in lines:
    if line:
        memory = ['run']
        form = ''
        for char in line + ' ':
            if char == ' ' and form and memory[-1] != 'string':
                memory.append(form.strip())
                form = ''
                continue
            if char in ['"', "'"]:
                if memory[-1] == 'string':
                    memory[-1] = '"' + form + '"'
                    form = ''
                else:
                    memory.append('string')
                continue
            form += char
            if form.strip() == '//':
                if len(memory) > 1:
                    add(memory)
                break
        else:
            add(memory)
    linenum += 1

linenum = 'unknown'
memory = ['run']
for line in compiled:
    for token in line:
        if memory[-1] == 'say':
            print(parse(token))
            memory.pop(-1)
        elif 'if' in memory:
            if token == '{':
                memory = memory[:memory.index('if')]
                memory.append(token)
                continue
            memory.append(token)
        elif token == '}':
            if memory[-1].endswith('{'):
                memory.pop(-1)
            else:
                callback('SyntaxError', 'Bracket not started correctly.')
        elif token == 'else':
            pass
        else:
            if token:
                memory.append(token)
if memory != ['run']:
    callback('SyntaxError', 'Bracket not closed correctly.')
