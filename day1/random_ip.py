import random

section1 = random.randint(0, 255)
section2 = random.randint(0, 255)
section3 = random.randint(0, 255)
section4 = random.randint(0, 255)

random_ip = str(section1) + '.' + str(section2) + '.' + str(section3) + '.' + str(section4)
print(random_ip)
