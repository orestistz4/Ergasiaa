import urllib.request
from bs4 import BeautifulSoup

#url='https://www.imdb.com'
url=input('Please input the website:')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

#kill all script and style elements
for script in soup(['script','style']):
    script.extract()
#pairnw to text
text = soup.get_text()
#ftiaxnw mia lista pou 8a periexei olo to text ths html xwris ta scripts,styles
lines=[]
for i in text:
    lines.append(i)
nlines=[]
#epeidh to text mou periexei polla kena kai new lines
#ta afairw
#wste sth lista mou na exw mono xarakthres
for k in lines:
    if k=='\n' or k==' ':
        continue
    nlines.append(k)

#metraw tous xarakthres kai ta vazw se ena dictionary
dicti = {}
for i in nlines:
    if i not in dicti:
        dicti[i]=nlines.count(i)
    else:
        continue
#vriskw to maximum value sto dictionary mou
maximum = max(dicti,key=dicti.get)
print('The most frequent character is:'+str(maximum)+' and it occured '+str(dicti[maximum])+' times.')    
