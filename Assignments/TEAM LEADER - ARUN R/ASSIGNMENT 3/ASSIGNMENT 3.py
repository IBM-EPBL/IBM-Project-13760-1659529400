import wiotp.sdk.device
import time
import os
import datetime
import random





myConfig = {





    "identity": {





      

  "orgId": "hj5fmy",



        "typeId": "Devicel"

,



 

       "deviceId": "67890"

client.connect()



    "auth": {



        "token": "87654321"




    if(m=="motoron"):




    elif(m=="motoroff"):



    print(" ")


client.connect()









def myCommandCallback(cmd):





    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])





    m=cmd.data['co
    def jls_extract_def():
        return


    jls_extract_var = jls_extract_def()
    client.commandCallback = jls_extract_var
    client.disconnect()

        print ("Motor is switched on")

    elif(m=="motoroff"):

        print ("Motor is switched OFF")
    print(" ")


while True:

    soil-random.randint (0, 100)

    temp=random.randint (-20,125)

    hum=random.randint (0,100)

    myData={'soil moisture': soil, 'temperature': temp, 'humidity':hum}

    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)

    print("Published data Successfully: %s", myData)

    time.sleep (2)
    jls_extract_var = myCommandCallback
    client.commandCallback = jls_extract_var
    client.disconnect()