import pickle
import os
import os.path
from tkinter.messagebox import NO
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from apiclient import errors
from os.path import basename



#  Gmail APIのスコープを設定
SCOPES = ['https://www.googleapis.com/auth/gmail.send']


#  メール本文の作成
def create_message(msg, sender, to_email, subject, message_text):
    #メール送信先
    msg['to'] = to_email
    # メール送信元
    msg['from'] = sender
    # メールのタイトル(件名)
    msg['subject'] = subject
    # ファイルを添付
    msg.attach(MIMEText(message_text))

    encode_message = base64.urlsafe_b64encode(msg.as_bytes())
    return {'raw': encode_message.decode()}

#  メール送信の実行
def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)

#  メインとなる処理
def main(to_email,judge):
    # メールの内容を作成
    msg = MIMEMultipart()
    #  アクセストークンの取得
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    #  メール本文の作成
    sender = 'intern.ohg.24b@gmail.com' # 送信者のアドレス
    #to_email = 'intern.ohg.24b@gmail.com' # 受信者のアドレス
    subject = '地図送信'
    # message_text = 'メール送信の自動化テストをしています。テストでーーーーーす'



    # メッセージの設定
    # {"spot":False,"sewage":False,"street":False}
    message_text = None
    if judge["spot"]:
        if judge["sewage"] and judge["street"]:
            message_text = "該当地域の地図画像です。"
            msg = post_picture(msg,"./picture/sewage.png")
            msg = post_picture(msg,"./picture/street.png")
        else:
            if judge["sewage"]:
                meg = post_picture("./picture/sewage.png")
            else:
                message_text = "下水道の地図が取得できませんでした。"

            if judge["street"]:
                msg = post_picture(msg,"./picture/street.png")
            else:
                message_text = "道路の地図が取得できませんでした。"
    else:
        message_text = "地域が取得できませんでした。"
    # if "該当地域の地図画像です。" == message_text:



    message = create_message(msg,sender, to_email, subject, message_text)
    #  Gmail APIを呼び出してメール送信
    send_message(service, 'me', message)

def post_picture(msg,path):
    # ファイルを添付
    # path = "./picture/image.png"
    with open(path, "rb") as f:
        part = MIMEApplication(
            f.read(),
            Name=basename(path)
        )
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(path)
    msg.attach(part)
    return msg

#  プログラム実行
if __name__ == '__main__':
    # main("intern.ohg.24b@gmail.com","送信テスト")
    main("intern.ohg.24b@gmail.com",{"spot":True,"sewage":True,"street":True})

