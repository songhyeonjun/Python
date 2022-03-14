import sys
import argparse
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

API_URL = 'https://dapi.kakao.com/v2/vision/multitag/generate'
MYAPP_KEY = 'b8b4f7372b3b310b3cca48bfe7fb2d8d'

def tag(image_url):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)
               }

    try:
        data = { 'image_url' : image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        resp.raise_for_status()
        result = resp.json()['result']
        if len(result['label_kr']) > 0:
            if type(result['label_kr'][0]) != str:
                result['label_kr'] = map(lambda x: str(x.encode("utf-8")), result['label_kr'])
            print("이미지를 대표하는 태그는 \"{}\"입니다.".format(','.join(result['label_kr'])))
        else:
            print("이미지로부터 태그를 생성하지 못했습니다.")

    except Exception as e:
        print(str(e))
        sys.exit(0)

if __name__ == "__main__":
    img_list = ['https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMjZfMTAz%2FMDAxNjQ1ODU3NzY1MjQ2.lzFib2qnr2nwiA9gYsUpL875ib3IUTRAGcylrLNM4wIg.F_mcTuHBhGyW3YZHQElKn4JLEBxSZNjpyRbXMo4TENIg.PNG.bunnyarom%2F12.png&type=l340_165',
                "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAzMDJfMzAg%2FMDAxNjQ2MTk3Mzg3MjE5.lqSLbN8SSG7I_rkC2CjfPVTJ6S_2ThlVpoTs5tJhUpgg.Gh4TEc2V8xc2UBurVL8CBUXp9_mtG9c8IBUubVZzz90g.PNG.j7qt4%2F%25BF%25B5%25C1%25BE%25B5%25B5%25B0%25ED%25BE%25E7%25C0%25CC%25BA%25D0%25BE%25E7_%25281%2529.png&type=a340",
                "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA4MTBfMjUg%2FMDAxNjI4NTY0Nzk4ODQx.GzTgt7EY2D4FgUbLwYHItcuPBmao02tjNm1-YHl6Cscg.7i7BcPa4Md3V7cD28ep3JPM05LehNI-aZa-f8f9knGsg.JPEG.jewelry70%2F1628564769768.jpg&type=a340"
                ]
    result_list = []
    for img in img_list:
        tag(img)
    parser = argparse.ArgumentParser(description='Classify Tags')
    parser.add_argument('image_url', type=str, nargs='?',
        default="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMjZfMTAz%2FMDAxNjQ1ODU3NzY1MjQ2.lzFib2qnr2nwiA9gYsUpL875ib3IUTRAGcylrLNM4wIg.F_mcTuHBhGyW3YZHQElKn4JLEBxSZNjpyRbXMo4TENIg.PNG.bunnyarom%2F12.png&type=l340_165",
        help='image url to classify')

    args = parser.parse_args()

    tag(args.image_url)