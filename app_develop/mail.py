import base64
import json
import pprint as pp
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from gmail_credential import get_credential


def decode_base64url_data(data):
    """
    base64url のデコード
    """
    decoded_bytes = base64.urlsafe_b64decode(data)
    decoded_message = decoded_bytes.decode("UTF-8")
    return decoded_message


def list_message(service, user_id, count):
    addres_datas = open('./secret/addres.json', 'r')
    addres_datas = json.load(addres_datas)
    addres = addres_datas["mailaddres"]
    message_ids = (
        service.users()
        .messages()
        .list(userId=user_id, maxResults=count)
        .execute()
    )

    if message_ids["resultSizeEstimate"] == 0:
        logger.warning("no result data!")
        return []

    # message id を元に、message の内容を確認
    for message_id in message_ids["messages"]:
        try:
            message_detail = (
                service.users()
                .messages()
                .get(userId="me", id=message_id["id"])
                .execute()
            )
        except:
            print('下書き中によるエラー')
            return {"addres":"0", "subject":"0", "body":"0", "internalDate":"0"}
        item = next((m for m in message_detail['payload']['headers'] if m['name'] == 'From'), None)
        if item:
            print("From:" + item['value'])
        # pp.pprint(message_detail)
        body = "0"
        z = "0"
        w = "0"
        if 'data' in message_detail['payload']['parts'][0]['body']:
            body = decode_base64url_data(message_detail['payload']['parts'][0]['body']['data'])
            mese = message_detail['payload']['headers']
            for i in range(len(mese)):
                if mese[i]["name"] == "Subject":
                    z = mese[i]["value"]
                elif mese[i]["name"] == "Return-Path":
                    w = mese[i]["value"]
                    w = w.strip("<>")
            if w == "0":
                w = addres
        internaldate = message_detail['internalDate']
        return {"addres":w, "subject":z, "body":body, "internalDate":internaldate}
        #print(body)

# メイン処理
def main(count):
    creds = get_credential()
    service = build("gmail", "v1", credentials=creds, cache_discovery=False)
    # メール一覧 [{'body': 'xxx', 'subject': 'xxx', 'from': 'xxx'},]
    return list_message(service, "me", count)


# プログラム実行部分
if __name__ == "__main__":
    messages_ = main(1)
    print(messages_)