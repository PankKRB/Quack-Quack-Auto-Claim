import subprocess
import time

b = 123

if b == 123:
    print('XIN CHÀO ADMIN')
else:
    print('XIN CHÀO KHÁCH HÀNG')

if b == 123:
    a = 7
    with open('trung.txt', 'w') as file:
        file.write(str(a))
    while True:
        quackquack_process = subprocess.Popen(['python', 'quackquack.py'])
        quackquack_process.terminate()
else:
    while True:
        quackquack_process = subprocess.Popen(['python', 'quackquackv3.py'])
        quackquack_process.terminate()
