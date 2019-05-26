import os
import send2trash
import time
def sss(count):
    for i in range(count):
        print(' ',end='')
empty=0
desktop = "C:\\Users\\dmhsk\\Desktop\\"
safes = open(desktop + "safe.txt").read().split('\n')
for file in os.listdir(desktop):
    if file in safes:
        continue
    send2trash.send2trash(desktop+file)
    print("삭제:",file)
    empty=1
lefttime=0
if empty==0:
    print('\n\n')
    sss(51)
    print("삭제 대상 없음\n\n\n")
    lefttime=3
else:
    lefttime=5
for i in range(lefttime):
    sss(52)
    print("종료",lefttime-i,"초 전")
    time.sleep(1)
    
    
