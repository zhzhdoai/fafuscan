
#coding=utf-8
from cmd import Cmd
import re
import os
from common import *
from module import *
from sqlscript import *

logo ="""\033[34m
  __        __       ____                  
 / _| __ _ / _|_   _/ ___|  ___ __ _ _ __  
| |_ / _` | |_| | | \___ \ / __/ _` | '_ \ 
|  _| (_| |  _| |_| |___) | (_| (_| | | | |
|_|  \__,_|_|  \__,_|____/ \___\__,_|_| |_|

Date: 2019-9-8
Author: osword                                           
Author_blog: http://zhzhdoai.github.io

\033[32mHelp
＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
    portscan:                                                  
        - 扫描网段端口存活：portscan 120.77.180.0/24 -p 80        
        - 扫描单个主机端口：portscan 127.0.0.1 -p 1-9999 或 80,139  
    dirscan:
        - 扫描某个网站目录: dirscan http://120.77.180.97/
    hrefscan:
        - 爬取网页参数链接：hrefscan http://www.baidu.com/
    clear:
        - 刷新当前界面：clear
＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
"""

#logo=base64.b64decode(logo)

class shell(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt="fafuScan >>> "
        self.intro = logo+'\033[0m'
    def do_EOF(self,line):
        return True 
    def do_portscan(self,line):
        tgthost = re.split(r'( *-p *)',line,3)[0]
        tgtports = re.split(r'( *-p *)',line,3)[2]
        portScan(tupleIp(tgthost,tgtports)).run()
    def do_hrefscan(self,line):
        sqlscript(line).getHref()
    def do_dirscan(self,line):
        dirScan(line).run()
    def do_clear(self,line):
        os.system('clear')
        os.system('python3 ./cmdScan.py')        
if __name__ == '__main__':
    try:
        shell().cmdloop()
    except:
        pass
    
