import hashlib

key = "808670FF00FF00FF08812".encode('utf-8')

def create_otp(input_key):
    
    key_hash = str(hashlib.sha256(input_key).hexdigest())
    
    global key
    
    key = key_hash.encode('utf-8')

    #Creates a string OTP of key hash with the first 6 digits
    otp = str(int(key_hash,16))[:6]
    
    return otp

