# -*- coding: utf8 -*-
import datetime
from bs4 import BeautifulSoup
import urllib.request
from datetime import date
import calendar

my_date = date.today()
day = str(calendar.day_name[my_date.weekday()])
date = str(datetime.date.today())

link = "http://www.defimedia.info"

content = str(urllib.request.urlopen(link).read().decode('utf8'))

soup = BeautifulSoup(content,"html.parser")

#print( soup.prettify())
filex =open('news/'+day+'-'+date+'.txt','w+')

info=[]
newline=[]
sx=list(range(141,145))+list(range(148,152))+list(range(155,159))+list(range(162,166))+list(range(169,173))+list(range(176,180))+list(range(183,187))+\
list(range(190,194))+list(range(197,201))+list(range(203,208))#+list(range(213,215))+list(range(218,220))
skip=[26,35,44,53,62,71,80,83,89,98,99,100]+sx


y=0
for link in soup.find_all('a'):
    var=''
    if y in newline:
        var='\n'
    if  y>17 and y not in skip and y not in range(100,140):
        info.append((link.text).replace('\\n','').replace('Téléplus','').replace('Politique','').replace('DEFIMEDIA.INFO','').replace('lire la suite','').strip(' ')+'  '+var)    
    #print(y, link.text)   
    y+=1
for i in range(len(info)):
    #if i<70:
    filex.write(info[i])
filex.close()
print('***TERMINATED***')
