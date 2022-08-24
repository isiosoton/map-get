import test
import map_picture
import send_mail

while True:
    x = test.test()
    map_picture.map_picture(x["body"])
    send_mail.main(x["addres"])