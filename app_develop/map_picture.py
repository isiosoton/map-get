from asyncio.windows_events import NULL
import chromedriver_binary
import time
import map_chiba_sewage
import map_chiba_street

map_spots = {"spots":["千葉市","さいたま市"], "items":["下水","道路"]}

shi = "千葉市"
item = "道路"

ku = "花見川区",
tyomei = "朝日ケ丘"
tyome = "１丁目"
gaiku = "1"


nums = [NULL,NULL]

if shi in map_spots["spots"] and item in map_spots["items"]:
    nums[0] = map_spots["spots"].index(shi)
    nums[1] = map_spots["items"].index(item)
    if nums == [0,0]:
        gaiku = gaiku.translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))
        print(gaiku)
        gaiku += "番"
        if tyome == NULL:
            tyome = "丁目なし"
            gaiku += "地"
        map_chiba_sewage.chiba_sewage(ku,tyomei,tyome,gaiku)
    elif nums == [0,1]:
        map_chiba_street.chiba_street(ku,tyomei+tyome,gaiku)
    elif nums == [1,0]:
        print("未実装")
    elif nums == [1,1]:
        print("未実装")
    
        
else:
    log = "対象外地域"
    print(log)

