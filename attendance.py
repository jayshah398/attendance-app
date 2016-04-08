__author__ = 'denrico'

import time as t
import shelve

s = shelve.open('my_students', writeback=True)

while True:
    entry = input('Begin scanning or enter q to quit: ')

    try:
        q = s.close()
        break

    except ValueError:
        print('ID not found; scan again.')

    else:
        print(s[entry]['name'] + ' scanned in at ' + t.strftime('%H:%M\n', t.localtime()))
        s[entry]['attendance'].append(t.time())



