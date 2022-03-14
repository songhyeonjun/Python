from tkinter import *
from multitag_API import *
from product_API import *

if __name__ == '__main__':

    # for i in range(1, 128, 10):
    #     path='./KoreanEnglishman/scene ('+str(i)+').png'
    #     label_result = multi_tag(path)
    #     print(label_result)

    product_list=[]
    for i in range(1, 128, 10):
        path = './KoreanEnglishman/scene (' + str(i) + ').png'
        detection_result = detect_product(path)
        product_list.append(detection_result)


    p_count_list=[]
    for x in product_list:
        count = 0
        for y in x['result']['objects']:
            print(y['class'])
            count+=1
        p_count_list.append(count)
        print('----------')

    print(p_count_list)

    multitag_list=[]
    for i in range(1, 128, 10):
        path='./KoreanEnglishman/scene ('+str(i)+').png'
        label_result = multi_tag(path)
        multitag_list.append(label_result)

    m_count_list=[]
    for x in multitag_list:
        count = 0
        for y in x['result']['label_kr']:
            print(y)
            count+=1
        m_count_list.append(count)
        print('---------')

    print(m_count_list)

    t_count_list=[]
    for i in  range(len(p_count_list)):
        t_count_list.append(p_count_list[i]+m_count_list[i])

    print('------------------------')
    print(t_count_list)
    max_index=t_count_list.index(max(t_count_list))
    print(max_index)
