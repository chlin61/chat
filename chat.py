

def read_file(filename):
    lines=[]
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(Line):
    new=[]
    for line in Line:
        if line in ['Allen','Tom']:
            person = line
            continue
        new.append(person + ': ' + line)
    #print(Line)
    return new

def write_file(filename,Line):
    with open(filename,'w',encoding='utf-8') as f:
        for line in Line:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

main()
