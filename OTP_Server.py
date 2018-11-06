import hashlib
import numpy as np


key = "808670FF00FF00FF08812".encode('utf-8')
passwordIndex = 0
#lookUpTable = np.zeros(1000000)


#lookUpTable = create_lookup_table(key)
cont = True

while cont != False:
    userFindPassword = input("Please intput password: ")

    while(passwordIndex < 1000000):
        if(create_otp(key) == userFindPassword):
            userCheckPassword = input("Please get the next password and input it here: ")
            if(create_otp(key) == userCheckPassword)



# create_lookup_table(self, key):
#    print('stub')

def create_otp(input_key):
    key_hash = str(hashlib.sha256(input_key).hexdigest())

    global key

    key = key_hash.encode('utf-8')

    #Creates a string OTP of key hash with the first 6 digits
    otp = str(int(key_hash,16))[:6]

    return otp
