# GUI

from tkinter import *   ## import * is นำแพ็คเกทตัวหลักของ tkinter
from tkinter import ttk, messagebox ## import theam of tkinter
from datetime import datetime
from xmlrpc.client import DateTime

############################################################

def writetext(quantity,total):
## function save data
    stamp = datetime.now()
    stamp = stamp.replace(year=stamp.year+543)  ## เปลีายนจาก ค.ศ. เป็น พ.ศ.
    stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
    filename = 'data.txt'
    with open(filename, 'a',encoding='utf-8') as file :
        file.write('\nวัน-เวลา: {} จำนวนเงาะ(กิโลกรัม) {} จำนวนเงินที่ต้องชำระ {} บาท'.format(stamp,quantity,total))

############################################################

GUI = Tk()
GUI.geometry('500x575')
GUI.title('DevByAlifriduwan')


L1 = Label(GUI, text='โปรแกรมคำนวณราคาเงาะ', font=('Angsana New',30,'bold'))
L1.pack()   ## .place(x,y) , .grid(row=0,column=0)

File = PhotoImage(file='BasicPython2/A-0056.png')
IMG = Label(GUI, image=File,text='')
IMG.pack()

L2 = Label(GUI, text='กรุณากรอกจำนวนเงาะ(กิโลกรัม)', font=('Angsana New',17))
L2.pack()

v_quantity = StringVar() ## ตัวแปรที่ใช้เก็บข้อมูลของช่องกรอก

E1 = ttk.Entry(GUI, textvariable=v_quantity, font=('impact',25))    ## กรอกเสร็จ นำเอาข้อมูลที่กรอกมาเก็บไว้ที่ตัวแปร v_quantity
E1.pack()

def Calculate():
    quantity = v_quantity.get()
    quantity = float(quantity)
    price = 20
    cal = float(quantity) * price
    print('จำนวน {} กิโลกรัม ราคารวม {} บาท'.format(quantity,(quantity*price)))
    messagebox.showinfo('ยอดที่ลูกค้าต้องชำระ(บาท)' ,'เงาะ {} กิโลกรัม ราคาทั้งหมด:{:,.2f} บาท'.format(quantity,cal))

    writetext(quantity,cal)


'''## EN DATE
    ##stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    ## THAI DATE
    stamp = datetime.now()
    stamp = stamp.replace(year=stamp.year+543)  ## เปลีายนจาก ค.ศ. เป็น พ.ศ.
    stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
   

    ## function save data
    filename = 'dataRumbuttan.txt'
    with open(filename, 'a',encoding='utf-8') as file :
        file.write('\nวัน-เวลา: {} จำนวนเงาะ(กิโลกรัม) {} จำนวนเงินที่ต้องชำระ {} บาท'.format(stamp,quantity,quantity*price))
'''

B1 = ttk.Button(GUI, text='คำนวณ', command=Calculate)
B1.pack(ipadx=15,ipady=10,pady=20)

    
GUI.mainloop()
