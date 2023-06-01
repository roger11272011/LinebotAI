import requests
from bs4 import BeautifulSoup

def read(word):
    url = f'https://tw.dictionary.search.yahoo.com/search;_ylt=Awrt4Gt6H3Bk8tYEtyV9rolQ;_ylc=X1MDMTM1MTIwMDM4MQRfcgMyBGZyA3NmcARmcjIDc2ItdG9wBGdwcmlkA1UxRW5YNnhTUzFLQUF3NmlLTzAuSEEEbl9yc2x0AzAEbl9zdWdnAzEwBG9yaWdpbgN0dy5kaWN0aW9uYXJ5LnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzMEcXVlcnkDeW91BHRfc3RtcAMxNjg1MDY5NzE3?p={word}&fr2=sb-top&fr=sfp'

    html = requests.get( url )
    bs = BeautifulSoup(html.text,'lxml')
    data = bs.find('div', id='web')
    try:
        eng = data.find_all('div',class_='fz-16 fl-l dictionaryExplanation')
        ps = data.find_all('div',class_='pos_button fz-14 fl-l mr-12')
        kk = data.find('div',class_='compList d-ib')
        return(word)
        return('音標:',kk.text)

        for j in range(len(ps)):
            return('詞性:',ps[j].text)
            return('中文:',eng[j].text)
    except:
        return('查無此字')
