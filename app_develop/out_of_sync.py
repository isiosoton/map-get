import re
bunsyo ="千葉県千葉市花見川区朝日ケ丘1丁目1"

bunkatsu = re.split('\d+', bunsyo) #1文字以上の任意の数字で分割
print(bunkatsu)

import re
def divide_addess(address):
  matches = re.match(r'(...??[都道府県])((?:旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|東村山|武蔵村山|羽村|十日町|上越|富山|野々市|大町|蒲郡|四日市|姫路|大和郡山|廿日市|下松|岩国|田川|大村)市|.+?郡(?:玉村|大町|.+?)[町村]|.+?市.+?区|.+?[市区町村])(.+)' , address)
  print(matches[1])
  print(matches[2])
  print(matches[3])
if __name__ == '__main__':
  address = "千葉県千葉市花見川区朝日ケ丘1丁目1"
  divide_addess(address)



import re

s_nums = '千葉県千葉市花見川区朝日ケ丘1丁目1'
pat = '(...??[都道府県])((?:旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|東村山|武蔵村山|羽村|十日町|上越|富山|野々市|大町|蒲郡|四日市|姫路|大和郡山|廿日市|下>松|岩国|田川|大村|宮古|富良野|別府|佐伯|黒部|小諸|塩尻|玉野|周南)市|(?:余市|高市|[^市]{2,3}?)郡(?:玉村|大町|.{1,5}?)[町村]|(?:.{1,4}市)?[^町]{1,4}?区|.{1,7}?[市町村])(.+)'

print(re.split(pat, s_nums))



adres = "千葉県千葉市花見川区朝日ケ丘1丁目1"
matches = re.match('東京都|北海道|(?:京都|大阪)府|.{2,3}県' , address)
matches = matches.group()
print(matches)
ku_number = adres.find("区")
ku_number = adres[:ku_number+1]
print(ku_number)
shi_number = adres.find("市")
shi_number = adres[:shi_number+1]
print(shi_number)







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
item = "道路"

ku = "花見川区"
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
    elif nums[0] == 1:
        jusyo = ken + shi + ku + tyomei + tyome + gaiku
        # print(jusyo)
        zahyo = coordinates.coordinates(jusyo)
        latitude = zahyo["ido"]
        longitude = zahyo["keido"]
        # print(zahyo)
        if nums[1] == 0:
            print("未実装")
        else:
            print("未実装")
else:
    log = "対象外地域"
    print(log)