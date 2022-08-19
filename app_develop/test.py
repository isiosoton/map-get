import mail

y = mail.main(1)

while True:
    x = mail.main(1)
    print(x["subject"])



    if x != y and x["subject"]=="serch addres": #xとyが同じならwile文そのまま実行
        break
print("whileから抜けたよ")
