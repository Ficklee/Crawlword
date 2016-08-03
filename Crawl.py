#coding:utf-8
import lxml
import bs4
from bs4 import BeautifulSoup
import urllib
import urllib2

def VisitURL(given_url):
    visitreq=urllib2.Request(given_url)
    visitresponse=urllib2.urlopen(visitreq)
    visitresponse=unicode(visitresponse.read(),'gbk','ignore')#.encode(encoding="utf-8")
    return lxml.etree.HTML(visitresponse)

filename="Savedata.txt"
baseurl='http://xh.5156edu.com/pinyi.html'
basicdomain='http://xh.5156edu.com/'
#Fdata=open(filename, mode='w')
URL_root=VisitURL(baseurl)
#print URL_root
#print type(URL_root)
pinyinurl=[basicdomain+urls for urls in URL_root.xpath('//td/a/@href')]
#print pinyinurl
wordurl=[]
wordsuffix=[]
word=[]
for one_pinyinURL in pinyinurl:
    print one_pinyinURL
    py_zi_IndexPage=VisitURL(one_pinyinURL)
    Zi_SuffixList=py_zi_IndexPage.xpath('body//a[contains(@href,"/html3/")]/@href')
    Zi_urlList=[basicdomain+suffix for suffix in Zi_SuffixList]
    for Zi_url in Zi_urlList:
        print Zi_url
        Zi_page=VisitURL(Zi_url)
        WordEleList=Zi_page.xpath('body//a[contains(@href,"/html5/")]')
        for wordele in WordEleList:
            Fdata=open(filename, 'a+')
            suffixurl=wordele.xpath('@href')
            SuffixNum=suffixurl[7:-5]
            longurl=basicdomain+suffixurl[0]
            wordurl.append(longurl)
            wText=wordele.text.encode('utf-8')
            print wText
            Fdata.writelines(wText+'\t'+longurl+'\n')
            Fdata.close()




    for y in xrange(len(word)):
        Fdata.writelines(word[y]+'\t'+wordsuffix[y]+'\t'+wordurl[y]+'\n')

'''
testurl=pinyinurl[1]
url_test=VisitURL(testurl)
#print type(url_test)
#print url_test
d1=url_test.xpath('body/table[@id="table1"]//a')[0].text
url01=url_test.xpath('body/table[@id="table1"]//a/@href')[0]
charurl=basicdomain+url01
#print url01
#print type(d1)
#d1=d1.encode('utf-8')
#print d1
zi_page=VisitURL(charurl)
e1=zi_page.xpath('body//a[contains(@href,"/html5/")]')
print e1
print e1[0].text.encode('utf-8')
e1_n=e1[0].xpath('@href')
print e1_n'''
