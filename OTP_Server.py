import hashlib
import numpy as np



key = "808670FF00FF08812".encode('utf-8')
passwordIndex = 0
#lookUpTable = np.zeros(1000000)

def create_otp(input_key):
    #Create hash of the key
    key_hash = str(hashlib.sha256(input_key).hexdigest())

    global key

    #Set global key variable to the hash of the key
    #This will be used for the next password generation
    key = key_hash.encode('utf-8')

    #Creates a string OTP of key hash with the first 6 digits
    otp = str(int(key_hash,16))[:6]

    global passwordIndex
    passwordIndex = passwordIndex+1
    #print(otp)
    return otp



#will loop forever since server must always be active
while True:
    #intitial password request
    userFirstPassword = input("Please input password: ")
    if(userFirstPassword == create_otp(key)):
        #if its a match to the next key then yay, access granted
        print("Correct password")
    else:
        #--------temp variables-------------------------------------
        correct = False
        revertKey = key                 #Saves current key incase we need to revert
        revertIndex = passwordIndex     #Saves current passwordIndex incase we need to revert
        #----------------------------------------------------------

        #Seach ahead for password
        while(passwordIndex < 1000000 and correct == False):
            if(userFirstPassword == create_otp(key)):
                #If found ask user for confirmation password
                userSecondPassword = input("Please get the next password and input it here: ")
                #If password is correct, give access
                if(create_otp(key)) == userSecondPassword:
                    print("Correct password")
                    correct = True
                else:
                    #If password is incorect start all over again
                    print("Incorrect password please generate the next password and try again")
                    key = revertKey
                    passwordIndex = revertIndex
                    correct = True
                    #cont = False
        #if first password never found deny access and start over again
        if(passwordIndex >= 1000000):
            print("Incorrect password please generate the next password and try again")
            key = revertKey
            passwordIndex = revertIndex
        #key = revertKey
