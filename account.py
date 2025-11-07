import os
import time
import sys
import pyfiglet

# Color Codes
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green

def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(23.0 / 8000)

# Display Information
to(
    f"""\x1b[1;92m
             
   ###    ########  ##    ##  #######  ##       ########  
  ## ##   ##     ## ###   ## ##     ## ##       ##     ## 
 ##   ##  ##     ## ####  ## ##     ## ##       ##     ## 
##     ## ########  ## ## ## ##     ## ##       ##     ## 
######### ##   ##   ##  #### ##     ## ##       ##     ## 
##     ## ##    ##  ##   ### ##     ## ##       ##     ## 
##     ## ##     ## ##    ##  #######  ######## ########  


AUTHOR   : \x1b[1;93mARNOLD HARDY x 🌝 \x1b[1;92mISHAN TURK   
Tools   : \x1b[1;93mSafeUm Account Creator Updated     \x1b[1;92m  
\x1b[1;92mBESTU    : \x1b[1;93mITZ CHUZA 🐥          
\x1b[1;92mVERSION  : \x1b[1;93m.0      \x1b[1;95m          
𝐋𝐎𝐆𝐎 𝐊𝐀 𝐊𝐘𝐀 𝐇 𝐔𝐍𝐊𝐀 𝐓𝐎 𝐊𝐀𝐌 𝐇 𝐇𝐈 𝐉𝐀𝐋𝐍𝐀\x1b[1;91m"""
)

# New logo for YEi Tech Monto
ab = pyfiglet.figlet_format("YEi Tech Monto")
print(G + ab)

def slow(T): 
    for r in T + '\n':
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(30 / 2000)

# Welcome message
slow(R + """ðŸ’‹ Welcome To Arnold's Safeum Account Creator ðŸ’‹.
---------------------------------------------------
""")

# Automatically open youtube channel
os.system("am start -a android.intent.action.VIEW -d https://youtube.com/@yeitechmonto?si=x3TitGB6gk2P34cj")

from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps

try:
    from websocket import create_connection
except:
    os.system('pip install websocket-client')
    from websocket import create_connection

failed = 0
success = 0
retry = 0
accounts = []

# Function to create Safeum accounts
def work():
    global failed, success, retry
    username = choice('qwertyuioplkjhgfdsazxcvbnm') + ''.join(choices(list('qwertyuioplkjhgfdsazxcvbnm1234567890'), k=12))
    try:
        con = create_connection("wss://193.200.173.45/Auth", header={
            "app": "com.safeum.android",
            "host": None,
            "remoteIp": "193.200.173.45",
            "remotePort": str(8080),
            "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
            "time": "2023-04-30 12:13:32",
            "url": "wss://51.79.208.190/Auth"
        }, sslopt={"cert_reqs": CERT_NONE})
        
        con.send(dumps({
            "action": "Register",
            "subaction": "Desktop",
            "locale": "en_IN",
            "gmt": "+05",
            "password": {
                "m1x": "0041211f085f41fd8f54fa31d143dbd5e667852fe3464dc7f3e87e690c34b60a",
                "m1y": "a9b5fdd814bfd1911b2c5c9e33b4893fce6ebadb79167d8061117d42212e0861",
                "m2": "d50ceeb76c61694191f3949d4a9b36e2580cda6d347b567aadebd4010c79a590",
                "iv": "4c62a6e3671c237a85822fd70aacc0b5",
                "message": "44196cc12b128049c065446b718e4a9f5d05692c7a1e73598a9742e837b44d3368bbefb10481a9a6a96db6f4a1ed92fa2da5dcd5e5509b675ebf7a3cea7ecdc58259b9eae540b8439802a3d6f21d721e"
            },
            "magicword": {
                "m1x": "24c73a89c085b08eb368ca8e71c48b5911dccf9acacd1020053977141c2544e7",
                "m1y": "af9242eaf65beeb119f461fcbced6ec052a2b6dbdf8f99eb6b3d36e580919f8c",
                "m2": "5b3005f7c235b80232d72960bc10429e2a4493287af3561dcb6d80e198806f9c",
                "iv": "16bc901405c8b4cd0da1646fd0f5a6df",
                "message": "097d09edbfc3e3ced1a6a35d9e52f72e"
            },
            "magicwordhint": "0000",
            "login": str(username),
            "devicename": "Xiaomi 220733SPH",
            "softwareversion": "1.1.0.1640",
            "nickname": "uzrurzrizirz",
            "os": "AND",
            "deviceuid": "b0c55c7c17fddd4b",
            "devicepushuid": "*eL-cSO7HSqWTPH08tbDvrT:APA91bEsZSuqtqy6-F2hDOsB17-Sght-cXJxc091gLZwtkQaQI_vTpYkBJWip4UsQSNveMUVIWMguiW48dFzakUf9BwCCq7dZbadcBvWSPXcLKXt7DQ4_IivMKC36CiORqDp8yT52Y1C",
            "osversion": "and_12.0.0",
            "id": "1177898800"
        }))
        
        gzip = decompress(con.recv()).decode('utf-8')
        if '"status":"Success"' in gzip:
            success += 1
            accounts.append(username + f':{G}creator (ARNOLD){R}')
            with open('SafeumAccounts.txt', 'a') as f: 
                f.write(username + f":{G}creator (ARNOLD){R}\n")
        else:
            failed += 1
    except:
        retry += 1

# Start account creation
start = ThreadPoolExecutor(max_workers=1000)
while True:
    start.submit(work)
    print('\n\n\n' + ' ' * 25 + f'Success password will be {G}@toxic_tanji{R}\n\n\n' + ' ' * 25 + f'Failed : {R}' + str(failed) + '\n\n\n' + ' ' * 25 + f'ReTry : {R}' + str(retry))
    if int(success) > int(0): 
        print("\n Accounts :  " + "\n".join(accounts))
    os.system("clear")  # Clear the screen