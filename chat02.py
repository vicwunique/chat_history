
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:     # 使用 'utf-8-sig' 去掉奇怪空格/符號(ex:\ufeff)
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):        # 設計"文字/貼圖/圖片"的計數功能
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('Allen 總共說了', allen_word_count, '個字')
    print('Allen 另外傳了', allen_sticker_count, '張貼圖、', allen_image_count, '張圖片')
    print('Viki 總共說了', viki_word_count, '個字')
    print('Viki 另外傳了', viki_sticker_count, '張貼圖、', viki_image_count, '張圖片')

def main():
    lines = read_file('input02.txt')
    convert(lines)

main()
