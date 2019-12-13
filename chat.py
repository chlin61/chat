

def read_file(filename):
    lines=[]
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(Line):
    new=[]
    person = None # 如果首次讀入的不是預設的人名，則不將對話存入
    for line in Line:
        if line in ['Allen','Tom']:
            person = line
            continue
        if person: # 如果有讀取到人名 就開始寫入到list
            new.append(person + ': ' + line)
    return new

def write_file(filename,Line):
    with open(filename,'w',encoding='utf-8') as f:
        for line in Line:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

if __name__ == '__main__':
	main()

