from string import printable
import requests
import time
import winsound
from datetime import datetime

filename=r'C:\SysJust\signal\aaronclearfile.txt'

tokenDict={'I3egjAOmZ5MnrInhQcrYrjoY0XntYOiLqss5fFZY4kc'}

stockListBull={''}
stockListBear={''}
startCount=0
endCount=0
fileCount=0
stopTime=134500

def lineNotifyMessage(token, msg):
    
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
        }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code


while True:
    
    try:
        print('{} {}'.format(datetime.now().strftime("%H:%M:%S"),'no signal'))

        

        with open(filename,'r') as fr:
            
            fileCount = len(open(filename).readlines())
            endCount=fileCount
            
            for line in fr.readlines()[startCount:endCount+1]:
                
                text=line.split(' ')
                
                if text[0]=='bull':
                    
                    if text[1] not in stockListBull:
                        stockListBull.add(text[1])
                        lineMessage = \
                            '\n宥\n機器人當沖單 做多\n{0} {1}'.format(text[1],text[2].replace('\n',''))

                        for token in tokenDict.values():
                            lineNotifyMessage(token, lineMessage)
                else:
                    
                    if text[1] not in stockListBear:
                        stockListBear.add(text[1])
                        lineMessage = \
                            '\n宥\n機器人當沖單 做空\n{0} {1}\n倍數:{2}'.format(text[1],text[2].replace('\n',''))
                
                for token in tokenDict.values():
                    lineNotifyMessage(token, lineMessage)    
                
            startCount=fileCount

                        
        time.sleep(1)
        
    except:
        print('exception')