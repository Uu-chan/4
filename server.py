import zmq # ZeroMQ
from datetime import datetime # для вывода времени

port = '11010' # порт, который будет биндиться, на который слать сообщения

context = zmq.Context() # создание контекста
socket = context.socket(zmq.PUB) # выбор роли "публикация" в паттерне pub-sub 
socket.bind('tcp://*:%s' % port) # бинд порта - ассоциация сокета с конкретным портом

while True: # бесконечный цикл
    messagedata = input('Сообщение: ') # ввод
    socket.send_string(messagedata) # отправка сообщения
    print('%s - [отправленно]\n' % datetime.now()) # вывод даты, когда сообщение было отправлено, для истории