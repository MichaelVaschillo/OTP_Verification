import hashlib
import numpy as np



key = "808670FF00FF00FF08812".encode('utf-8')
passwordIndex = 0
#lookUpTable = np.zeros(1000000)

def create_otp(input_key):
    key_hash = str(hashlib.sha256(input_key).hexdigest())

    global key

    key = key_hash.encode('utf-8')

    #Creates a string OTP of key hash with the first 6 digits
    otp = str(int(key_hash,16))[:6]

    global passwordIndex
    passwordIndex = passwordIndex+1
    #print(otp)
    return otp


#lookUpTable = create_lookup_table(key)
#cont = True

while True:
    userFirstPassword = input("Please input password: ")
    if(userFirstPassword == create_otp(key)):
        print("Correct password")
    else:
        correct = False
        revertKey = key
        revertIndex = passwordIndex
        while(passwordIndex < 1000000 and correct == False):
            if(userFirstPassword == create_otp(key)):
            #if(create_otp(key) == userFirstPassword):
                userSecondPassword = input("Please get the next password and input it here: ")
                if(create_otp(key)) == userSecondPassword:
                    print("Correct password")
                    correct = True
                else:
                    print("Incorrect password please generate the next password and try again")
                    key = revertKey
                    passwordIndex = revertIndex
                    correct = True
                    #cont = False
        if(passwordIndex >= 1000000):
            print("Incorrect password")
            key = revertKey
            passwordIndex = revertIndex
        #key = revertKey





# create_lookup_table(self, key):
#    print('stub')
