import sys
import time
import datetime
import requests
# probably should not import both time and datetime


MyFile = r'C:\SysJust\XQLite\XS\signal\aaronclearfile.txt'
MyText = " "
MyDate = " "
initialLines = 0


def GetDateTime(): #設定GetDateTime函式
    MyDate = time.strftime("%x %I:%M %p") #定義時間格式
    return MyDate+" "


def lineNotifyMessage(token, msg): #設定lineNotifyMessage函式
    
#以下設定訊息內容
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }


    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers= headers, params= payload)
    return r.status_code


def notifyData(showIndex): #設定notifyData函式並帶入
    #以下設定抓取所有訊息
    
    with open (MyFile, "r",) as myfile:
        Lines = myfile.readlines()
        lenLines = len(Lines)
        
        print("notify len lines : " + str(lenLines)) #顯示行數
        print("show index : " + str(showIndex)) #顯示行數
        print("Show Data : " + str(Lines[(showIndex -1)])) #顯示新增文字


        messageBasket = str(Lines[(showIndex -1)]).split(" ") #把字串指定給messageBasket


        messagebasketlen = len(messageBasket) #把計算好的長度指定給messagebasketlen
        
  
        #以下把訊息messageBasket 累加排列給message 
        
        message = "\r\n"
        message += messageBasket[0] + " " + messageBasket[1] + "\r\n" 
        message += messageBasket[2] + " " + messageBasket[3] + "\r\n" 
        message += messageBasket[4] + " " + messageBasket[5] + " " 
        message += messageBasket[6] + "\r\n" + messageBasket[7] + " " 
        message += messageBasket[8] + "\r\n" + messageBasket[9] + " "
        message += messageBasket[10] + " "
              
       
        #message = messageBasket[0] + " "
        #message += messageBasket[1] + "\r" + messageBasket[2] + "  " 
        #message += messageBasket[3] + "\r\n" + messageBasket[4] + " " 
        #message += messageBasket[5] + " " + messageBasket[6] + "\r\n" 
        #message += messageBasket[7] + " " + messageBasket[8] + "\r\n" 
        #message += messageBasket[9] + " " + messageBasket[10] + " "
        
        #呼叫lineNotifyMessage函式並帶入使用權限,訊息
        lineNotifyMessage("SdgWSvDJDIzInlwR3NJIisfos1cI5lbL5do5cEbmasw", message)


def ReadFile(initLines): #設定ReadFile函式
    #開啟檔案D:\signal\aaronfile.txt並讀取行數帶入
      
    with open (MyFile, "r") as myfile:
        try:
            # MyText2=myfile.read().replace('\n',' ')
            Lines = myfile.readlines()
            lenLines = len(Lines)
            # count = 0
            # for line in Lines:
            #     count += 1
            #     print("line "+ str(count) +"= " + line.replace('\n', ''))
        finally:


            print("initLines = " + str(initLines)) #顯示行數


            cur_date_time = GetDateTime() #指定cur_date_time為呼叫GetDateTime函式


            if (initLines == lenLines): #判定是否有增加行數
                # file hasn't changed...print to screen only
                print("No Change = " + cur_date_time)
                time.sleep(1.3) #等待1.3sec
                ReadFile(lenLines)
            else: #判定有增加行數
                # print to screen and printer
                diffLine = lenLines - initLines


                print ("Has Diffrence : " + cur_date_time)
                print ("Diff Line : " + str(diffLine))


                if (initLines != 0):
                    for i in range(0, diffLine):
                        lineIndex = initLines + (i+1)
                        print ("Line Index = " + str(lineIndex))
                        notifyData(lineIndex)


                time.sleep(1.3) #等待1.3sec
                ReadFile(lenLines) #呼叫ReadFile函式


            myfile.close()


ReadFile(initialLines) #執行ReadFile函式
