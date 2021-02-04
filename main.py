variables = {}

with open('code.txt') as file:
    for line in file:
        line = line.strip().split()
        if line[0].startswith('#') or line == '':
            continue
        elif 'equals' in line:
            variables[line[0]] = line[1]
        elif line[0] == 'say':
            for i in line[1:]
                if i.startswith('[') and i.endswith(']'):
                    print(variables[i.strip('[]')] if i.startswith('[') and i.endswith(']') else i, end=' ')
            print()
