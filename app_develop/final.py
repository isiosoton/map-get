import test
import map_picture
import send_mail

while True:
    x = test.test()
    print(x)
    message_text = map_picture.map_picture(x["body"])
    send_mail.main(x["addres"],message_text)