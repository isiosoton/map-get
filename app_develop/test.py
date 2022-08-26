import mail

def test():
    y = mail.main(1)
    x = y

    while True:
        x = mail.main(1)
        print(x["subject"])



        if x["internalDate"] != y["internalDate"] and x["subject"]=="map": #xとyが同じならwile文そのまま実行
            break
    print("whileから抜けたよ")

    return x

# test()