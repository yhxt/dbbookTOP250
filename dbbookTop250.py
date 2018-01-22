import requests
from lxml import etree
import time

for a in range(2):
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    url='https://book.douban.com/top250?start={}'.format(a*25)
    data=requests.get(url,headers = headers).text
    s=etree.HTML(data)

    file=s.xpath('//*[@id="content"]/div/div[1]/div/table')
    for div in file:
        title=div.xpath('./tr/td[2]/div[1]/a/@title')[0]
        href=div.xpath('./tr/td[2]/div[1]/a/@href')[0]
        pf=div.xpath('./tr/td[2]/div[2]/span[2]/text()')[0]
        num=div.xpath('./tr/td[2]/div[2]/span[3]/text()')[0].strip('(').strip().strip(')')
        scrible=div.xpath('./tr/td[2]/p[2]/span/text()')[0]
        time.sleep(1)
        if len(scrible)>0:
            print (title,href,pf,num,scrible)
        else:
            print (title,href,pf,num)
