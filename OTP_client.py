import hashlib

key = "808670FF00FF00FF08812".encode('utf-8')

def create_otp(input_key):
    
    key_hash = str(hashlib.sha256(input_key).hexdigest())
    
    global key
    
    key = key_hash.encode('utf-8')

    #Creates a string OTP of key hash with the first 6 digits
    otp = str(int(key_hash,16))[:6]
    
    return otp

def prompt_user():
    cont = True
    while cont == True:
        user = input('Press 1 to generate password \nPress 2 to exit program \n')

        if int(user) == 1:
            print('\n' + str(create_otp(key)) + '\n')
        elif int(user) == 2:
            cont = False
        else:
            print('Invalid input')

prompt_user()
        

