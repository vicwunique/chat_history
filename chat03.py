
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:     # 使用 'utf-8-sig' 去掉奇怪空格/符號(ex:\ufeff)
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    for line in lines:
        s = line.split(' ')
        time = s[0][:5]
        name = s[0][5:]
        print(time, name , ':', s[1])

def main():
    lines = read_file('input03.txt')
    convert(lines)

main()
