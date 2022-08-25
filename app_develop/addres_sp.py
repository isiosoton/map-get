# 元の文字列
text = "！＂＃＄％＆＇（）＊＋，－．／０１２３４５６７８９：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿｀>？＠ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝～"

# 変換
x = text.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))

print(x)
# 結果
# '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`>?@abcdefghijklmnopqrstuvwxyz{|}~'


kisoku_a = [["一","1"],["二","2"],["三","3"],["四","4"],["五","5"],["六","6"],["七","7"],["八","8"],["九","9"]]
for i in kisoku_a:
    jusyo = jusyo.replace(i[0],i[1])