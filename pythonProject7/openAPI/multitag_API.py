import sys
import argparse
from collections import Counter
from tkinter import messagebox

import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

API_URL = 'https://dapi.kakao.com/v2/vision/multitag/generate'
# API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
MYAPP_KEY = 'b9ca7e6fcb8da3719636ca6542de8a8a'

def multi_tag(img):
    file = {'image': open(img, 'rb')}
    header = {'Authorization' : 'KakaoAK %s' % MYAPP_KEY}
    response = requests.post(API_URL,
                             headers=header,
                             files=file)
    # print(response)

    json_result = response.json()
    return json_result


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='..')
    # parser.add_argument('image_file', type=str, nargs='?', default="alone.png",
    #                     help='image file ')
    #
    # args = parser.parse_args()
    # label_result = multi_tag(args.image_file)

    for i in range(1, 128, 10):
        path='./KoreanEnglishman/scene ('+str(i)+').png'
        label_result = multi_tag(path)
        print(label_result)