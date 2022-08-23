import imp
import chromedriver_binary
import time
import map_chiba_sewage
import map_chiba_street
import saitama_road
import saitama_sewage
import coordinates

map_spots = {"spots":["千葉市","さいたま市"], "items":["下水","道路"]}

ken = "埼玉県"
shi = "さいたま市"
item = "道路"
ku = "浦和区"
tyomei = "高砂"
tyome = "３丁目"
gaiku = "15"

# ken = "千葉県"
# shi = "千葉市"
# item = "下水"
# ku = "花見川区"
# tyomei = "朝日ケ丘"
# tyome = "１丁目"
# gaiku = "1"


nums = [None,None]

if shi in map_spots["spots"] and item in map_spots["items"]:
    nums[0] = map_spots["spots"].index(shi)
    nums[1] = map_spots["items"].index(item)
    if nums == [0,0]:
        gaiku = gaiku.translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))
        print(gaiku)
        gaiku += "番"
        if tyome == None:
            tyome = "丁目なし"
            gaiku += "地"
        map_chiba_sewage.chiba_sewage(ku,tyomei,tyome,gaiku)
    elif nums == [0,1]:
        map_chiba_street.chiba_street(ku,tyomei+tyome,gaiku)
    elif nums[0] == 1:
        jusyo = ken + shi + ku + tyomei + tyome + gaiku
        zahyo = coordinates.coordinates(jusyo)
        latitude = zahyo["ido"]
        longitude = zahyo["keido"]
        if nums[1] == 0:
            saitama_sewage.road(longitude, latitude)
            # print("未実装")
        else:
            saitama_road.road(longitude, latitude)
            # print("未実装")
else:
    log = "対象外地域"
    print(log)

# https://www.sonicweb-asp.jp/saitama_g/map?theme=th_45#pos=139.649195,35.857156
# https://www.sonicweb-asp.jp/saitama_g/map?theme=th_45139.64919535.857156

