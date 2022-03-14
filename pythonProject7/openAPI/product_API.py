import sys
import argparse
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

API_URL = 'https://dapi.kakao.com/v2/vision/product/detect'
MYAPP_KEY = 'a7b67eb75e39a57c2ef640b5fffb81dd'

def detect_product(img):
    file = {'image': open(img, 'rb')}
    header = {'Authorization' : 'KakaoAK %s' % MYAPP_KEY}
    response = requests.post(API_URL,
                             headers=header,
                             files=file)
    # print(response)

    json_result = response.json()
    return json_result


if __name__ == "__main__":

    for i in range(1, 128, 10):
        path='./KoreanEnglishman/scene ('+str(i)+').png'
        detection_result = detect_product(path)
        print(detection_result)

    # for x in detection_result['result']['objects']:
    #     print(x['class'])
    #
    # print(detection_result)
