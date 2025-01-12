import random

karakterler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk= int(input ("Sifrenin uzunlugunu belirleyin!"))
parola=""

for i in range(uzunluk):
    parola+=random.choice(karakterler)

print("Parola:"+parola)

