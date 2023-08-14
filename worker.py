import sys
import zmq


# Worker catches the message and updates the map

class Worker:
    def __init__(self, ports:list):
        self.ports = ports

        # Socket to talk to server
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)

        # Connect to all ports (ie. publishers)
        for port in self.ports:
            self.socket.connect("tcp://localhost:%s" % port)

    def run(self, filter:bytes):
        self.socket.setsockopt(zmq.SUBSCRIBE, filter)

        # Process 5 updates
        total_value = 0
        for update_nbr in range(5):
            string = self.socket.recv()
            topic, messagedata = string.split()
            total_value += int(messagedata)
            print(topic, messagedata)


if __name__ == '__main__':
    ports = sys.argv[1].split(',')

    worker = Worker(ports)
    worker.run(filter=str.encode("10001"))