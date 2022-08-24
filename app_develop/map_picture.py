from distutils.command.install_egg_info import safe_name
import os
from PIL import Image
# import img2pdf
import imp
import chromedriver_binary
import time
import map_chiba_sewage
import map_chiba_street
import map_saitama_street
import map_saitama_sewage
import coordinates

def map_picture(addres):

    map_spots = {"spots":["千葉市","さいたま市"], "items":["下水","道路"]}

    # ken = "埼玉県"
    # shi = "さいたま市"
    # item = "道路"
    # ku = "浦和区"
    # tyomei = "高砂"
    # tyome = "３丁目"
    # gaiku = "15"

    ken = "千葉県"
    shi = "千葉市"
    item = "下水"
    ku = "花見川区"
    tyomei = "朝日ケ丘"
    tyome = "１丁目"
    gaiku = "1"

    ken = "大阪府"

    nums = [None,None]

    if shi in map_spots["spots"] and item in map_spots["items"]:
        nums[0] = map_spots["spots"].index(shi)
        nums[1] = map_spots["items"].index(item)
        log = "ログデータ"
        safe_comment = "該当地域の地図画像です。"
        try:
            if nums == [0,0]:
                gaiku = gaiku.translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))
                gaiku += "番"
                if tyome == None:
                    tyome = "丁目なし"
                    gaiku += "地"
                if map_chiba_sewage.chiba_sewage(ku,tyomei,tyome,gaiku):
                    log = safe_comment
            elif nums == [0,1]:
                if map_chiba_street.chiba_street(ku,tyomei+tyome,gaiku):
                    log = safe_comment
            elif nums[0] == 1:
                jusyo = ken + shi + ku + tyomei + tyome + gaiku
                zahyo = coordinates.coordinates(jusyo)
                latitude = zahyo["ido"]
                longitude = zahyo["keido"]
                if nums[1] == 0:
                    if map_saitama_sewage.road(longitude, latitude):
                        log = safe_comment
                else:
                    if map_saitama_street.road(longitude, latitude):
                        log = safe_comment
        except:
            log = "地図取得に失敗しました。"

        # with open("./pdf/output.pdf","wb") as f:
        #     f.write(img2pdf.convert(['./picture/image.png']))
        # file = os.path.abspath("./picture/image.png")
        
        # # 絶対パスを指定して、ファイルに書き込み
        # image1 = Image.open(file, "r")
        # # image1 = Image.open(rfile)
        # im_pdf = image1.convert("RGB")
        # im_pdf.save("./pdf/output.pdf","r")
        return log

    else:
        log = "対象外地域により送信できませんでした。"
        return log

    # https://www.sonicweb-asp.jp/saitama_g/map?theme=th_45#pos=139.649195,35.857156
    # https://www.sonicweb-asp.jp/saitama_g/map?theme=th_45139.64919535.857156

