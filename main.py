import os
import math
import random
import smtplib
print("WELCOME TO MY OTP VERIFICATION")
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP + "  Is your OTP"
msg=otp

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("duncankimunya6@gmail.com", "nwdzijfpwczlhydz")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")