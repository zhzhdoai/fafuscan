import requests
from bs4 import BeautifulSoup
import threading
from config import *
from urllib.parse import urlparse
hList = []

class sqlscript():

    def __init__(self,url):
        self.url = url
        

    def getHref(self):
        global hList
        sess = requests.session()
        text = sess.get(url=self.url,headers=headers).text
        soup = BeautifulSoup(text,'lxml')
        href = soup.find_all('a')
        for t in href:
            parse = urlparse(t['href'])
            if len(parse.query) >= 3:
                print('\033[33m'+parse.scheme+"://"+parse.netloc+parse.path+'?'+parse.query)
        print('\033[0m')
    



# if __name__ == "__main__":
#     sqlscript('https://www.lacaixafellowships.org/index.aspx').getHref()


#　http://esjindex.org/search.php