import schedule
import time


def switch_case_time(duration):
    switcher = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five"
    }
    print switcher.get(duration, "Invalid duration")


def one():
    minutes_inp = input("Every minute scheduler")
    schedule.every(minutes_inp).minutes.do(job, 'this is ' + minutes_inp + ' minutes')


def two():
    minutes_inp = input("Every minute scheduler")
    schedule.every(minutes_inp).minutes.do(job, 'this is ' + minutes_inp + ' minutes')


def three():
    minutes_inp = input("Every minute scheduler")
    schedule.every(minutes_inp).minutes.do(job, 'this is ' + minutes_inp + ' minutes')


def four():
    minutes_inp = input("Every minute scheduler")
    schedule.every(minutes_inp).minutes.do(job, 'this is ' + minutes_inp + ' minutes')


def five():
    minutes_inp = input("Every minute scheduler")
    schedule.every(minutes_inp).minutes.do(job, 'this is ' + minutes_inp + ' minutes')


def job():
    print("I'm working...")


while True:
    schedule.run_pending()
    time.sleep(60)  # wait one minute pip
