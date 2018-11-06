import matplotlib.pyplot as plt
import hashlib

key = "808670FF00FF00FF08812".encode('utf-8')

def create_otp(input_key):
    
    #Hash of the key
    key_hash = str(hashlib.sha256(input_key).hexdigest())
    
    global key
    
    #Update global key variable
    key = key_hash.encode('utf-8')

    #Creates a string OTP of key hash with the first 6 digits
    otp = str(int(key_hash,16))[:6]
    
    return otp

#Empty list for OTPs
passwords = []

#Create 1 million OTPs
for i in range(1000000):
    
    #Add OTP to list
    passwords.append(create_otp(key))
    
    i += 1

#Check for back-to-back duplicates
duplicates = 0

for j in range(1, len(passwords)):
    if passwords[j] == passwords[j-1]:
        duplicates += 1

print('Back-to-back duplicates in 1 million passwords: ' + str(duplicates))

#Empty list for counting number of collisions
collision_counter = []

for i in range(100):
    password_set = set(passwords[0:i*10000])
    
    collision_counter.append((i*10000) - len(password_set))

plt.figure(1)
plt.plot(range(100), collision_counter, color='red', linestyle=':')
plt.title('Collisions of OTPs')
plt.xlabel('Number of OTPs (tens of thousands)')
plt.ylabel('Number of Collisions')
plt.show()
plt.savefig('collision_graph.png')