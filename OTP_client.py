import hashlib

#Create initial key
key = "808670FF00FF00FF08812".encode('utf-8')

def create_otp(input_key):
    
    #Create hash of the key
    key_hash = str(hashlib.sha256(input_key).hexdigest())
    
    global key
    
    #Set global key variable to the hash of the key
    #This will be used for the next password generation
    key = key_hash.encode('utf-8')

    #Creates a string OTP of key hash with the first 6 digits
    otp = str(int(key_hash,16))[:6]
    
    return otp

def prompt_user():
    cont = True

    while cont == True:
        #Get user input 
        user = input('Press 1 to generate password \nPress 2 to exit program \n')

        if user == str(1):
            print('\n' + str(create_otp(key)) + '\n')

        elif user == str(2):
            cont = False

        else:
            print('Invalid input \n')

prompt_user()
        

