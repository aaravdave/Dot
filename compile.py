variables = {}

with open(f'{__name__}.dscr') as file:
    for line in file:
        line = line.strip().split()
        if ''.join(line) == '':
            continue
        elif line[0].startswith('#'):
            continue
        elif 'equals' in line:
            variables[line[0]] = line[2]
        elif line[0] == 'say':
            for i in line[1:]:
                print(variables[i.strip('[]')] if i.startswith('[') and i.endswith(']') else i, end=' ')
            print()
