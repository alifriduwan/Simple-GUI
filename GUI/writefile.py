## writefile
from datetime import datetime

'''filename = 'data.txt'
with open(filename, 'a') as file :
    file.write('\n'+'Rumbuttan: 100')'''


def writetext(quantity,total):
## function save data
    stamp = datetime.now()
    stamp = stamp.replace(year=stamp.year+543)  ## เปลีายนจาก ค.ศ. เป็น พ.ศ.
    stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
    filename = 'data.txt'
    with open(filename, 'a',encoding='utf-8') as file :
        file.write('\nวัน-เวลา: {} จำนวนเงาะ(กิโลกรัม) {} จำนวนเงินที่ต้องชำระ {} บาท'.format(stamp,quantity,total))


## writetext(90,9000)
## writetext(91,9000)
## writetext(92,9000)
## ritetext(93,9000)