# https://docs.docker.com/samples/library/eclipse-mosquitto/

docker run -it -p 1883:1883 -p 9001:9001 -v mosquitto.conf:/home/luranga/mosquito/config/mosquitto.conf -v /home/luranga/mosquito/data -v /home/luranga/mosquito/log eclipse-mosquitto

mosquitto_sub -t 'test/topic' -v
mosquitto_pub -t 'test/topic' -m 'hello world'

