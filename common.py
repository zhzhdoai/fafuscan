from config import *
import ipaddr
import random

def glist(tgtports):
    tmplist=[]
    if '-' in tgtports:
        Portlist=[]
        tmplist.append(tgtports.split('-')[0])
        tmplist.append(tgtports.split('-')[1])
        for p in range(int(tmplist[0]),int(tmplist[1])+1):
            Portlist.append(p)
        return Portlist
    else:
        Portlist=tgtports.split(',')
        return Portlist
            
def tupleIp(mip,ports):
    Portlist=glist(ports)
    tlist=[]
    if '/' in mip:     
        hosts = ipaddr.IPv4Network(mip).iterhosts()
        for i in hosts:
            for j in Portlist:
                tlist.append((str(i),int(j)))
    else:
        for j in Portlist:
            tlist.append((str(mip),int(j)))
    return tlist
       
def get_user_agent():
    return User_Agents[random.randint(0,len(User_Agents)-1)]





