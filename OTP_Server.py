import hashlib
import numpy as np

class OTP_Server(object):
    key = "808670FF00FF00FF08812".encode('utf-8')
    lookUpTable = np.zeros(1000000)

    def __init__(self):
        lookUpTable = create_lookup_table(key)
        print("Please intput password:")


    def create_lookup_table(self, key):
        print('stub')

    def create_otp(self, input_key):

        key_hash = str(hashlib.sha256(input_key).hexdigest())

        global key

        key = key_hash.encode('utf-8')

        #Creates a string OTP of key hash with the first 6 digits
        otp = str(int(key_hash,16))[:6]

        return otp
