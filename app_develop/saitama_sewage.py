import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.sonicweb-asp.jp/saitama_g/map?theme=th_90#pos=139.62260560261188,35.90632537222594")

#同意画面を取得し、それの同意をクリック
time.sleep(2)
iframe = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(iframe)
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='agree_btn_area']/ul/li[1]/a").click()


#住所検索をクリック
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='gazetteerLinkaddress_list']").click()


#位置検索(さいたま市役所を検索します)
time.sleep(2)
addres = driver.find_element(By.XPATH, "//*[@id='slct_address_list_add1']")
addres_select = Select(addres)
addres_select.select_by_visible_text("浦和区")

time.sleep(2)
addres = driver.find_element(By.XPATH, "//*[@id='slct_address_list_add2']")
addres_select = Select(addres)
addres_select.select_by_visible_text("ト")











#候補の検索画面から探したいものをクリック
time.sleep(5)





#印刷画面をクリック
driver.find_element(By.XPATH, "//*[@id='map_btn']/div[1]/a[2]").click()


#スクショをとる&保存
FILENAME = "image.png"
# get width and height of the page
w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")

# set window size
driver.set_window_size(w,h)

# Get Screen Shot
driver.save_screenshot(FILENAME)

#写真をPDF化する
#さっきインストールしたライブラリをインポート
import img2pdf,os
from PIL import Image
#Pythonのファイルパス指定は色々と面倒ですが、
#下記のようにパスの頭にrをつけるとうまくいきます
#ベースとなる画像を置いてあるフォルダパス
base_Image = r"C:\Test\PDF_Test\image"
#pdfを作成したいフォルダパス
Create_pdf = r"C:\Test\PDF_Test\pdf"
#画像の名前（拡張子含む）
Image_Name = "image1.jpg"
#pdf化したあとのファイルパス（拡張子含む）
pdf_name = Create_pdf + "\\" + str(Image_Name) + ".pdf"
#chdirでカレントディレクトリを移動
os.chdir(base_Image)
#Pillowモジュールを使用し画像の読み込み
img = Image.open(Image_Name)
#画像を回転 必要があれば使用
img = img.rotate(-90, expand = True)
#pdfファイルへ変換
cov_pdf = img2pdf.convert(Image_Name)
#pdfファイルを読み込み（pdf_nameで指定したpdfがない場合、pdf_nameをファイル名として新規にpdfファイルを作成）
file = open(pdf_name , "wb")
#pdfファイルを書き込み
file.write(cov_pdf)
#開いているファイルを閉じる
img.close()
file.close()





#メールを送信
#  Gmail APIのスコープを設定
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# メールの内容を作成
msg = MIMEMultipart()

#  メール本文の作成
def create_message(sender, to_email, subject, message_text):
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
def main():
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
    to_email = 'intern.ohg.24b@gmail.com' # 受信者のアドレス
    subject = 'メール送信自動化テスト'
    message_text = 'メール送信の自動化テストをしています。テストでーーーーーす'

    # ファイルを添付
    path = "image.png"
    with open(path, "rb") as f:
        part = MIMEApplication(
            f.read(),
            Name=basename(path)
        )
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(path)
    msg.attach(part)


    message = create_message(sender, to_email, subject, message_text)
    #  Gmail APIを呼び出してメール送信
    send_message(service, 'me', message)

#  プログラム実行
if __name__ == '__main__':
    main()