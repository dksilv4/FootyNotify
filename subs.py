subs = []
sublist = open('SubList.txt', 'r').read().split('\n')
for sub in sublist:
    x = sub.split(', ')
    subs.append(x)


def subscribe(no, code):
    number = '\n{}, {}'.format(no, code)
    subs = open('SubList.txt', 'a+')
    subs.write(number)


def check_sub(num):
    for subscriber in subs:
        if num == subscriber[0]:
            print(subscriber[0])
            print('FOUND')
            return True

        return False


subscribe('07748278829', 'CPUK')
