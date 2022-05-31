import time
from datetime import datetime

pathDict={'token_test':r'C:\SysJust\signal\aaronclearfile.txt'}

startTime=133500
endTime=133510

while True:
    
    if int(time.strftime("%H%M%S"))>startTime and int(time.strftime("%H%M%S"))<=endTime:
        print('stop')
        break
    
    for token in pathDict.values():
        with open(token,'w+') as fw:
            fw.write('')
        
    print('{} {}'.format(datetime.now().strftime("%H:%M:%S"),'clear'))
    time.sleep(10)