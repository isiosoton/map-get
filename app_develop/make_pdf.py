import imp
import imp
from PIL import Image, ImageFilter
import os.path

def main():
    # with open("./pdf/output.pdf","wb") as f:
    #     f.write(img2pdf.convert(['./picture/image.png']))
    file_path = "./picture/image.png"
    picture_file = os.path.abspath(file_path)
    # print(picture_file)
    # 絶対パスを指定して、ファイルに書き込み
    image1 = Image.open(file_path).convert("RGB")
    # image1 = Image.open(file_path, "r")
    # image1 = Image.open(r+picture_file)
    # im_pdf = image1
    image1.save("./pdf/image.pdf","r")

if __name__ == "__main__":
    main()