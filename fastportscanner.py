# -*- coding: utf-8 -*- 
"""
Created on Tuesday February 19 21:54 2021

@author: root_sphinx
"""
import threading
import socket
import os
import json

os.system("apt install figlet")
os.system("clear")
os.system("figlet Sphinx")
print("""
Bu Araç Sayesinde Port Taraması Yapabilirsiniz
""")
target = 'www.google.com'
#ip = socket.gethostbyname(target)

def portscan(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)#
    
    try:
        con = s.connect((target,port))
        
        print('Port :',port,"is open.")
        
        con.close()
    except:
        pass
r = 1
for x in range(1,100):


    t = threading.Thread(target=portscan,kwargs={'port':r})
    
    r += 1
    t.start()
