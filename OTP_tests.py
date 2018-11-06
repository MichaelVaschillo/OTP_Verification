import matplotlib.pyplot as plt
import hashlib

key = "808670FF00FF00FF08812".encode('utf-8')

def create_otp(input_key):
    
    key_hash = str(hashlib.sha256(input_key).hexdigest())
    
    global key
    
    key = key_hash.encode('utf-8')

    #Creates a string OTP of key hash with the first 6 digits
    otp = str(int(key_hash,16))[:6]
    
    return otp

passwords = []

for i in range(1000000):
    
    passwords.append(create_otp(key))
    
    i += 1

collision_percentage = []

for i in range(100):
    password_set = set(passwords[0:i*10000])
    
    collision_percentage.append((i*10000) - len(password_set))

plt.figure(1)
plt.plot(range(100), collision_percentage, color='red', linestyle=':')
plt.title('Collisions of OTPs')
plt.xlabel('Number of OTPs (tens of thousands)')
plt.ylabel('Number of Collisions')
plt.show()
plt.savefig('collision_graph.png')