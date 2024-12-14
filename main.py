import random
chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

#length = input('berapa panjang password yang anda inginkan?')
sord = ""
for i in range(10):
    sord += random.choice(chars)
print(sord)
