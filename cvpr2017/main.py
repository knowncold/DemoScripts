import re
from bs4 import BeautifulSoup
import requests

r = requests.get('http://openaccess.thecvf.com/CVPR2017.py')

soup = BeautifulSoup(r.text)
papers = soup.find_all(href=re.compile(".pdf"))
count = 0
for i in papers:
    if 'supplemental' in str(i):
        name = str(i)[40:len(str(i))-10]
        url = 'http://openaccess.thecvf.com/content_cvpr_2017/supplemental/' + name
        print name
    else:
        name = str(i)[34:len(str(i))-9]
        url = 'http://openaccess.thecvf.com/content_cvpr_2017/papers/' + name
        print name
    f = open(name,'wb')
    pdf = requests.get(url)
    if pdf.status_code == 200:
        f.write(pdf.content)
        f.close()
    else:
        print name
        print url
        print "***************\nFAILED"
    count += 1
    print str(count) + '/1026'
