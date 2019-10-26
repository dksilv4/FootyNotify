from datetime import datetime
from threading import Timer
import schedule
import time


def job(t):
    print("I'm working...", t)
    return


schedule.every().day.at("01:00").do(job, 'It is 01:00')

while True:
    schedule.run_pending()
    time.sleep(60)  # wait one minute
sublist = open('SubList.txt', 'r').read().split('\n')

for sub in sublist:
    x = sub.split(', ')
    print(x)


def hello_world():
    print("hello world")


class Verify:
    def __init__(self, message):
        # if message.from in sublist:
        #     pass
        if ''.join(message.lower()) == 'crystal palace':
            pass
            # send message to confirm sub
            # if confirmed add number to sub list with code

    def example(self):
        pass


if __name__ == '__main__':
    x = datetime.today()
    y = x.replace(day=x.day + 1, hour=15, minute=29, second=0, microsecond=0)
    delta_t = y - x

    secs = delta_t.seconds + 1

    t = Timer(secs, hello_world)
    t.start()
    pass
