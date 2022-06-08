import sys
import time
import datetime
import requests
# probably should not import both time and datetime

MyFile = r'D:\signal\aaronclearfile.txt'
MyText = ""
MyDate = ""
initialLines = 0

def GetDateTime():
    MyDate = time.strftime("%x %I:%M %p")
    return MyDate+" "

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers= headers, params= payload)
    return r.status_code

def notifyData(showIndex):
    with open (MyFile, "r") as myfile:
        Lines = myfile.readlines()
        lenLines = len(Lines)

        print("notify len lines : " + str(lenLines))
        print("show index : " + str(showIndex))
        print("Show Data : " + str(Lines[(showIndex - 1)]))

        messageBasket = str(Lines[(showIndex - 1)]).split(" ")

        messagebasketlen =len(messageBasket)

        message = messageBasket[0] + '\r\n' 
        message += messageBasket[1] + " " + messageBasket[2] + '\r\n' 
        message += messageBasket[3] + " " + messageBasket[4] + '\r\n' 
        message += messageBasket[5] + " " + messageBasket[6] + '\r\n' 
        message += messageBasket[7] + " " + messageBasket[8] + '\r\n' 
        message += messageBasket[9] + " " + messageBasket[10]

        lineNotifyMessage("iL0m0ydmAYHrmtemXvlvBl4AhMcxLrAfd0sth2fOmxG", message)

def ReadFile(initLines):
    with open (MyFile, "r") as myfile:
        try:
            # MyText2=myfile.read().replace('\n','  ')
            Lines = myfile.readlines()
            lenLines = len(Lines)
            # count = 0
            # for line in Lines:
            #     count += 1
            #     print("line "+ str(count) +"= " + line.replace('\n', ''))
        finally:

            print("initLines = " + str(initLines))

            cur_date_time = GetDateTime()

            if (initLines == lenLines):
                # file hasn't changed...print to screen only
                print("No Change = " + cur_date_time)
                time.sleep(5)
                ReadFile(lenLines)
            else:
                # print to screen and printer
                diffLine = lenLines - initLines

                print ("Has Diffrence : " + cur_date_time)
                print ("Diff Line : " + str(diffLine))

                if (initLines != 0):
                    for i in range(0, diffLine):
                        lineIndex = initLines + (i+1)
                        print ("Line Index = " + str(lineIndex))
                        notifyData(lineIndex)

                time.sleep(5)
                ReadFile(lenLines)

            myfile.close()

ReadFile(initialLines)