import threading
import time
import random
import queue

class DataStore:
    def __init__(self):
        self.data = 1
        # self.lock = threading.Lock()

    def put(self, data):
        # with self.lock:
            self.data = data

    def get(self):
        return self.data
        # with self.lock:
        #     if self.data:
        #         return self.data.pop(0)
        #     return None

class Producer(threading.Thread):
    def __init__(self, data_store, stop_event):
        super(Producer, self).__init__()
        self.data_store = data_store
        self.stop_event = stop_event

    def run(self):
        while not self.stop_event.is_set():
            data = random.randint(1, 10)
            self.data_store.put(data)
            print(f"Produced: {data}")
            time.sleep(1)
            if data > 5:
                print("Game Over")
                # self.stop_event.set()

class Consumer(threading.Thread):
    def __init__(self, data_store, stop_event):
        super(Consumer, self).__init__()
        self.data_store = data_store
        self.stop_event = stop_event

    def run(self):
        while not self.stop_event.is_set():
            data = self.data_store.get()
            if data:
                print(f"Consumed: {data}")
            if data > 7:
                self.stop_event.set()
                self.stop_event.clear()
                time.sleep(1)
                consumer = Consumer(self.data_store, self.stop_event)
                consumer.daemon = True
                consumer.start()
                print(f"Restart Consumer.....")
            time.sleep(3)
            print(f"End.....")

if __name__ == "__main__":
    data_store = DataStore()
    # data_store = queue.Queue()
    stop_event = threading.Event()

    producer = Producer(data_store, stop_event)
    consumer = Consumer(data_store, stop_event)

    producer.daemon = True
    consumer.daemon = True

    producer.start()
    consumer.start()

    print("Hello World")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        stop_event.set()
        producer.join()
        consumer.join()
