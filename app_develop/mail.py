import base64
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
        message_detail = (
            service.users()
            .messages()
            .get(userId="me", id=message_id["id"])
            .execute()
        )
        #pp.pprint(message_detail)
        item = next((m for m in message_detail['payload']['headers'] if m['name'] == 'From'), None)
        if item:
            print("From:" + item['value'])
        body = decode_base64url_data(message_detail['payload']['parts'][0]['body']['data'])
        mese = message_detail['payload']['headers']
        z = "0"
        for i in range(len(mese)):
            if mese[i]["name"] == "Subject":
                z = mese[i]["value"]
        print(z)
        #print(message_detail['internalDate'])
        internaldate = message_detail['internalDate']
        return {"subject":z, "body":body, "internalDate":internaldate}
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