import requests
from bs4 import BeautifulSoup

def read(word):
    url = f'https://tw.dictionary.search.yahoo.com/search;_ylt=Awrtgeger3hkCoQFOI99rolQ;_ylu=Y29sbwMEcG9zAzEEdnRpZAMEc2VjA3Nj?p={word}&ei=UTF-8&context=gsmcontext%3A%3Alimlangpair%3A%3Aen_zh-hant&fr=sfp'

    html = requests.get( url )
    bs = BeautifulSoup(html.text,'lxml')
    data = bs.find('div', id='web')
    try:
        eng = data.find_all('div',class_='fz-16 fl-l dictionaryExplanation')
        ps = data.find_all('div',class_='pos_button fz-14 fl-l mr-12')
        kk = data.find('div',class_='compList d-ib')
        a=('音標:'+kk.text+'\n')

        for j in range(len(ps)):
            a=a+('詞性:'+ps[j].text+'\n')
            a=a+('中文:'+eng[j].text+'\n)
        a=a+'詳細內容:'+url
        return(a)
    except:
        return('查無此單字')
