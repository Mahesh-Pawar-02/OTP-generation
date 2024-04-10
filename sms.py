import random
generatorotp=random.randint(0000000,100000)
username = input("Username : ")
print('Hello..!',username)
print('Here is your otp for login',generatorotp)
password = input("Enetr the otp to login:")

if password == str(generatorotp):
    print('Login Success...!')

else:
    password != str(generatorotp)
    print('Login Denied...!')