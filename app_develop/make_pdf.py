from email.mime import image
import imp
import imp
from PIL import Image, ImageFilter
import os.path

def main(file_name):
    file_path_png = "./picture/" + file_name + ".png"
    picture_file = os.path.abspath(file_path_png)
    image1 = Image.open(picture_file).convert("RGB")
    # 絶対パスを指定して、ファイルに書き込み
    # print(type(image1))
    file_path_pdf = "./pdf/" + file_name + ".pdf"
    image1.save(file_path_pdf)

if __name__ == "__main__":
    # main(["sewage","street"])
    main("sewage")