from distutils.command.install_egg_info import safe_name
# import img2pdf
import chromedriver_binary
import time
import map_chiba_sewage
import map_chiba_street
import map_saitama_street
import map_saitama_sewage
import coordinates
import out_of_sync
import make_pdf

def map_picture(addres):

    addres_list = out_of_sync.main(addres)

    spots = ["千葉市","さいたま市"]

    # shi = "さいたま市"
    # ku = "浦和区"
    # tyomei = "高砂"
    # tyome = "３丁目"
    # gaiku = "15"

    # shi = "千葉市"
    # ku = "花見川区"
    # tyomei = "朝日ケ丘"
    # tyome = "１丁目"
    # gaiku = "1"

    shi = addres_list[0]
    ku = addres_list[1]
    tyomei = addres_list[2]
    tyome = addres_list[3]
    gaiku = addres_list[4]

    nums = 6

    logs = {"spot":False,"sewage":False,"street":False}

    if shi in spots:
        logs["spot"] = True
        nums = spots.index(shi)
        log = "ログデータ"
        safe_comment = "該当地域の地図画像です。"
        if nums == 0:
            tiba_object = map_chiba_sewage.change_data(ku,tyomei,tyome,gaiku)
            logs["sewage"] = tiba_object["picture"]
            if tiba_object["spot"]:
                logs["street"] = map_chiba_street.chiba_street(tiba_object)
            else:
                logs["spot"] = tiba_object["spot"]

        elif nums == 1:
            jusyo = shi + ku + tyomei + tyome + gaiku
            zahyo = coordinates.coordinates(jusyo)
            if zahyo["accept"]:
                latitude = zahyo["ido"]
                longitude = zahyo["keido"]
                logs["sewage"] = map_saitama_sewage.road(longitude, latitude)
                logs["street"] = map_saitama_street.road(longitude, latitude)
            else:
                logs["spot"] = False
        if logs["sewage"]:
            make_pdf.main("sewage")
        if logs["street"]:
            make_pdf.main("street")
    return logs

if __name__ == '__main__':
    tiba = ["千葉県千葉市稲毛区稲毛３丁目７−３０","千葉県千葉市稲毛区稲毛3-7","千葉県千葉市稲毛区稲毛町５丁目269−１","千葉市稲毛区稲毛町５ー２６９ー１","千葉県浦安市北栄1-15-9","千葉県千葉市美浜区真砂五丁目１５−１","千葉県千葉市美浜区真砂5丁目15−1","千葉県千葉市美浜区真砂５丁目１５番１","千葉県千葉市美浜区真砂５-１５−１","千葉県千葉市美浜区真砂６丁目１−１"]
    saitama = ["埼玉県さいたま市大宮区大門町2丁目1-1","埼玉県さいたま市大宮区大門町２ー1-１","埼玉県さいたま市大宮区大門町2-1-1","さいたま市大宮区大門町２－１－１","埼玉県川口市栄町3-14-3","埼玉県さいたま市南区沼影1-20-1","埼玉県さいたま市南区沼影一丁目20-1","さいたま市南区沼影１丁目20-1","埼玉県さいたま市南区沼影１丁目２０番地１号","埼玉県さいたま市大宮区大門町６丁目５"]
    all_list = tiba + saitama
    all_object = []
    for i in all_list:
        all_object.append(map_picture(i))
    print(all_object)
    # print(map_picture(saitama[3]))
    # https://www.sonicweb-asp.jp/saitama_g/map?theme=th_45#pos=139.649195,35.857156
    # https://www.sonicweb-asp.jp/saitama_g/map?theme=th_45139.64919535.857156

