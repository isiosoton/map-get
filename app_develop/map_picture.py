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

    spots = ["千葉市","さいたま市"]

    ken = "埼玉県"
    shi = "さいたま市"
    ku = "浦和区"
    tyomei = "高砂"
    tyome = "３丁目"
    gaiku = "15"

    # ken = "千葉県"
    # shi = "千葉市"
    # ku = "花見川区"
    # tyomei = "朝日ケ丘"
    # tyome = "１丁目"
    # gaiku = "1"

    nums = 6

    logs = {"spot":False,"sewage":False,"street":False}

    if shi in spots:
        logs["spot"] = True
        nums = spots.index(shi)
        log = "ログデータ"
        safe_comment = "該当地域の地図画像です。"
        if nums == 0:
            logs["street"] = map_chiba_street.chiba_street(ku,tyomei+tyome,gaiku)
            gaiku = gaiku.translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))
            gaiku += "番"
            if tyome == None:
                tyome = "丁目なし"
                gaiku += "地"
            logs["sewage"] = map_chiba_sewage.chiba_sewage(ku,tyomei,tyome,gaiku)
        elif nums == 1:
            jusyo = ken + shi + ku + tyomei + tyome + gaiku
            zahyo = coordinates.coordinates(jusyo)
            if zahyo["accept"]:
                latitude = zahyo["ido"]
                longitude = zahyo["keido"]
                logs["sewage"] = map_saitama_sewage.road(longitude, latitude)
                logs["street"] = map_saitama_street.road(longitude, latitude)
            else:
                logs["spot"] = False

        # with open("./pdf/output.pdf","wb") as f:
        #     f.write(img2pdf.convert(['./picture/image.png']))
        # file = os.path.abspath("./picture/image.png")
        
        # # 絶対パスを指定して、ファイルに書き込み
        # image1 = Image.open(file, "r")
        # # image1 = Image.open(rfile)
        # im_pdf = image1.convert("RGB")
        # im_pdf.save("./pdf/output.pdf","r")

    return logs

    # https://www.sonicweb-asp.jp/saitama_g/map?theme=th_45#pos=139.649195,35.857156
    # https://www.sonicweb-asp.jp/saitama_g/map?theme=th_45139.64919535.857156

