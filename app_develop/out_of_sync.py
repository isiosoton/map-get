import re
addres = "千葉県 千葉市 花見川区 朝日ケ丘 1 丁目 1"



def replace_hyphen(text, replace_hyphen):
    """全ての横棒を半角ハイフンに置換する
    Args:
        text (str): 入力するテキスト
        replace_hyphen (str): 置換したい文字列
    Returns:
        (str): 置換後のテキスト
    """
    hyphens = '-˗ᅳ᭸‐‑‒–—―⁃⁻−▬─━➖ーㅡ﹘﹣－ｰ𐄐𐆑 '
    hyphens = '|'.join(hyphens)
    return re.sub(hyphens, replace_hyphen, text)


tiba = ["千葉県千葉市稲毛区稲毛３丁目７−３０","千葉県千葉市稲毛区稲毛3-7","千葉県千葉市稲毛区稲毛町５丁目269−１","千葉市稲毛区稲毛町５ー２６９ー１","千葉県浦安市北栄1-15-9","千葉県千葉市美浜区真砂五丁目１５−１","千葉県千葉市美浜区真砂5丁目15−1","千葉県千葉市美浜区真砂５丁目１５番１","千葉県千葉市美浜区真砂５-１５−１","千葉県千葉市美浜区真砂６丁目１−１"]
saitama = ["埼玉県さいたま市大宮区大門町2丁目1-1","埼玉県さいたま市大宮区大門町２ー1-１","埼玉県さいたま市大宮区大門町2-1-1","さいたま市大宮区大門町２－１－１","埼玉県川口市栄町3-14-3","埼玉県さいたま市南区沼影1-20-1","埼玉県さいたま市南区沼影一丁目20-1","さいたま市南区沼影１丁目20-1","埼玉県さいたま市南区沼影１丁目２０番地１号","埼玉県さいたま市大宮区大門町６丁目５"]
addres = addres.split('県')
if len(addres) == 2:
    addres_pre = addres[0]
    addres_shi = addres[1]
for addres in tiba: 
    addres = list(addres)
    for i,j in enumerate(addres):
        #print(i,j)
        if j.isdecimal():
            addres.insert(i, "-")
            break
    addres = "".join(addres)
    kisoku_a = [["一","1"],["二","2"],["三","3"],["四","4"],["五","5"],["六","6"],["七","7"],["八","8"],["九","9"]]
    for i in kisoku_a:
        addres = addres.replace(i[0],i[1])
    # 変換
    addres = addres.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
    addres = replace_hyphen(addres, replace_hyphen='-')
    print(addres)
    addres = (addres.replace("丁目", "-"))
    
    
    
    #print(addres.replace('県', '\n').replace("市", '\n').replace("区", '\n').replace('\d', '\n').replace('-', '\n').replace('番', '\n').split('\n'))






#print("千葉県千葉市花見川区朝日ヶ丘-1-1-13".replace('県', '\n').replace("市", '\n').replace("区", '\n').replace('\d', '\n').replace('-', '\n').split('\n'))