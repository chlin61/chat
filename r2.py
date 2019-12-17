

def read_file(filename):
    lines=[]
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(Line):
    s=[]
    Allen_talk_count = 0
    Allen_sc = 0
    Allen_tc = 0
    viki_talk_count = 0
    Viki_sc = 0
    Viki_tc = 0
    #person = None # 如果首次讀入的不是預設的人名，則不將對話存入
    for line in Line:
        s = line.split(' ')
        name = s[1]
        time = s[0]
        if name =='Allen':
            if s[2] == '貼圖':
                Allen_sc += 1
            elif s[2] == '圖片':
                Allen_tc += 1
            else:
                for m in s[2:]:
                    Allen_talk_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                Viki_sc += 1
            elif s[2] == '圖片':
                Viki_tc += 1
            else:
                for m in s[2:]:
                    viki_talk_count += len(m)
    print('Allen講了', Allen_talk_count, '個字', '貼圖', Allen_sc, '有幾張' )
    print('且圖片有', Allen_tc, '張')
    print('Viki講了', viki_talk_count, '個字', '貼圖', Viki_sc, '有幾張' )
    print('且圖片有', Viki_tc, '張')
       # if line in ['Allen','Tom']:
        #    person = line
         #   continue
        #if person: # 如果有讀取到人名 就開始寫入到list
         #   new.append(person + ': ' + line)
    #return new

def write_file(filename,Line):
    with open(filename,'w',encoding='utf-8') as f:
        for line in Line:
            f.write(line + '\n')

def main():
    lines = read_file('[LINE]Viki.txt')
    convert(lines)
    #write_file('output.txt', lines)

if __name__ == '__main__':
	main()

