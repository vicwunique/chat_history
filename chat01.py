
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:     # 使用 'utf-8-sig' 去掉奇怪空格/符號(ex:\ufeff)
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None       # 先宣告 person 其值為 None (預設值為"無")
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:      # 如果 person 已經有值 (避免第一行沒有出現人名)
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input01.txt')        # 讀取
    lines = convert(lines)                  # 轉換(convert)
    write_file('output01.txt', lines)       # 寫入

main()
