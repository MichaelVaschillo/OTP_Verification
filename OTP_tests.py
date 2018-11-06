import OTP_client as cl
import matplotlib.pyplot as plt

passwords = []

for i in range(1000000):
    
    passwords.append(cl.create_otp(cl.key))
    
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