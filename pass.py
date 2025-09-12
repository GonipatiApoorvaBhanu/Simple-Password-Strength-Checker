import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
symbol="@#$%^&*_+}{<>}"
all=lower+upper+num+symbol
length=12
password="".join(random.sample(all,length))
print("Generated Passsword is" ,password)

