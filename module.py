#coding=utf-8
import threading
from socket import *
from queue import *
import ipaddr
import time
from common import *
import requests

tmplist=[]
dirlist=[]
savedir=[]
length= 0 

printLock = threading.Semaphore(1)

class portScan():
    def __init__(self,rlist):
        self.queue = Queue()
        self.rlist = rlist
        
        for i in self.rlist:
            #print(i)
            self.queue.put(i)

    def startScan(self):
        while not self.queue.empty():
            infolist=self.queue.get_nowait()
            ip=str(infolist[0])
            port=int(infolist[1])
            try:
                ss = socket(AF_INET,SOCK_STREAM)
                ss.settimeout(2)
                #print(f'Prepare to test {ip}')
                ss.connect((ip,port))
                if printLock.acquire():
                    print(f'Ip: {ip} Port: {port}')
                    printLock.release()
                ss.close()
            except:
                ss.close()
            finally:
                pass
    def run(self):
        threads=[]
        for t in range(0,Threadnum):
            thread1 = threading.Thread(target=self.startScan)
            threads.append(thread1)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        



class dirScan():
    def __init__(self,infourl):
        self.queue = Queue()
        self.infourl = infourl
        self.thread_count=Threadnum
        self.lock = threading.Lock()
        self.count=1
        for i in self.get_dir(path):
            self.queue.put(i)
    
    def startDir(self):
        global savedir
        
        while self.queue.qsize() > 0:
            try:
                url = self.infourl+str(self.queue.get())
                #headers={'User-Agent ':get_user_agent(),'content-type': 'application/json'}
                headers = {
                    'Accept': '*/*',
                    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; ',
                    'Connection': 'Keep-Alive',
                    'Cache-Control': 'no-cache',
                }
                rep = requests.get(url=url,headers=headers,timeout=5)
                printLock.acquire()
                if str(rep.status_code)[0] in "2,3":
                    print(f"\r\033[33m[{self.count}]url: {url}  staus: {rep.status_code} sucess",end="")
                    savedir.append(url)
                else:
                    print(f"\r\033[33m[{self.count}]url: {url}  staus: {rep.status_code} false",end="")
                self.count+=1
                printLock.release()
            except: 
                pass
            finally:
                pass
                     

    def run(self):
        global savedir
        threads=[]
        savedir=[]
        time.sleep(3)
        for i in range(0,Threadnum):
            thread = threading.Thread(target=self.startDir,daemon=True)
            threads.append(thread)
            thread.start()
        for t in threads:
            t.join()

        
        print("thread close")
        for i in savedir:
            print(i)
        savadir=[]
        print('\033[0m')
        return True



    def get_dir(self,path):
        global dirlist,length
        dirlist=[]
        with open(path,'r',errors="ignore") as f:
            tmplist=f.readlines()
        for i in tmplist:
            dirlist.append(i.strip())
        #print(dirlist)
        length=len(dirlist)
        print("Prepare to run list about: %d"%(length))
        time.sleep(1)
        return dirlist

#dirScan("http://120.77.180.97/").run()
    