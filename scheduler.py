import schedule
import time

#TODO: enter some code to select how long and based on how long, select a choice from the switch case

def switch_case_time(choice):
    switcher = {
        1: "one",
        2: "two",
        3: "three"
    }
    print switcher.get(choice, "Invalid duration")


def minute():
    minutes_inp = input("Every minute scheduler")
    schedule.every(minutes_inp).minutes.do(job, 'this is ' + minutes_inp + ' minutes')


def hour():
    minutes_inp = input("Every hour scheduler")
    schedule.every(minutes_inp).hours.do(job, 'this is ' + minutes_inp + ' hours')


def day():
    minutes_inp = input("Every day scheduler")
    schedule.every(minutes_inp).days.do(job, 'this is ' + minutes_inp + ' days')


def job():
    print("I'm working...")


while True:
    schedule.run_pending()
    time.sleep(60)  # wait one minute pip
