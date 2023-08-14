import zmq
import random
import sys
import time


# Client broadcasts the message (ie. map)
class Client:
    def __init__(self, port):
        self.port = port
        context = zmq.Context()
        self.socket = context.socket(zmq.PUB)
        self.socket.bind("tcp://*:%s" % port)

    def run(self):
        while True:
            map_id = random.randrange(9999, 10005)
            data = random.randrange(1, 215) - 80
            print("%d %d" % (map_id, data))
            self.socket.send(b"%d %d" % (map_id, data))
            time.sleep(1)


if __name__ == '__main__':
    port = sys.argv[1]
    print(port)

    client = Client(port)
    client.run()
