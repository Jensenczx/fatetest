__author__ = 'chenjensen'
#-*-coding:utf-8-*-
import re
import urllib2
from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tagname=0
        self.infolist=[]
    def handle_starttag(self, tag, attrs):
        if tag=='p':
            self.tagname = tag
    def handle_endtag(self, tag):
        if tag=='b' and self.tagname=='p':
            self.tagname='p'
        else:
            self.tagname=None
    def handle_data(self, data):
       if self.tagname=='p':
                self.infolist.append(data)
class xzSrcub():
    def __init__(self):
        pass
    def getresult(self,man,woman):
        urlstr='http://www.d1xz.net//astro/peidui/'+man+'-'+woman+'.aspx'
        parser = MyHTMLParser()
        try:
            response=urllib2.urlopen(urlstr)
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code
            elif hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
        else:
            doc=response.read()
            page=doc.decode("gbk")
            try :
                parser.feed(page)
            except :
                pass
            finally:
                list = parser.infolist[:-1]
                parser.close()
                return list
