import os

from pdf2image import convert_from_path,convert_from_bytes
import cv2
import pytesseract
from pathlib import Path
import glob2
from PIL import Image
import numpy as np
import requests
from bs4 import BeautifulSoup

try:
    #f = open("log_allscrip.txt", "a+")
    page = requests.get("https://structure.mil.ru/structure/forces/hydrographic/info/notices.htm")
    if (page.ok):
        print("Sucess")
        #responsecode_success('India', 'MainResponsecode', page.status_code)
        # print("Sucessfull", page.status_code)
    else:
        print("Fail")
        #responsecode_unsuccess('India', 'MainResponsecode', page.status_code)
    # print("Unsucessfull", page.status_code)

    soup = BeautifulSoup(page.content, "html.parser")

    for link in soup.find_all('a'):
        if not link.endswith('.pdf'):
            print(link.get('href'))
            continue
        #print(link.get('href'))


    #mydivs = soup.find_all("div", {"class": "docs"})
    #for i in mydivs:
        #print(i.get('href'))
        #print(i['href'])
    #print(mydivs)

        #print(i.find('a').contents[0])
        #print(i.)
        #print(i)
    #print(href)


except Exception as e:
    print(e)

path = r'C:\Users\nanip\PycharmProjects\Navarea_Scripts3\venv\Scripts\ImageDoc'
def pdf2img():
    try:
        images = convert_from_path(r'D:/temp/ENGV_2124.pdf',300,poppler_path=r'C:\Users\nanip\PycharmProjects\Navarea_Scripts3\venv\Scripts\poppler-0.68.0_x86\poppler-0.68.0\bin')
        print(len(images))
        for i, image in enumerate(images):
            fname = path+ '\image'+str(i)+'.jpeg'
            image.save(fname, "jpeg")
    except Exception as e:
        print("No pdf Found",e)
    else:
        print("Am Sucess")

pdf2img()


pagestr = ''
try:
    img_path=r'C:\Users\nanip\PycharmProjects\Navarea_Scripts3\venv\Scripts\ImageDoc'
    filenames = glob2.glob(img_path + '/*')
    print(len(filenames))
    print(filenames)
    for imgfi in filenames:
        img = Image.open(imgfi)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.image_to_string(img)
        text = pytesseract.image_to_string(img)+'#'
        pagestr+=text
except Exception as e:
    print(e)
print(pagestr)
