import paho.mqtt.client as mqtt
import paho.mqtt.client as paho

broker="172.17.0.1"
port=1883

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")

client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)
#establish connection
ret= client1.publish("test/topic","asd")                   #publish


def on_disconnect(client, userdata, rc):
   print("client disconnected ok")

client1.on_disconnect = on_disconnect
client1.disconnect()
