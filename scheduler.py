import schedule
import time
import datetime

def job(t):
    print("I'm working...", t)
    return


schedule.every().minute.do(job, datetime.datetime.now())

while True:
    schedule.run_pending()
    time.sleep(60)  # wait one minute